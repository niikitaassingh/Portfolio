from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
import uvicorn
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# Load credentials from .env file
load_dotenv()

app = FastAPI()

# Mount static files (for CSS and images)
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="static/templates")

# --- YOUR CV DATA ---
profile_data = {
    "name": "Nikita Singh",
    "title": "Data Analyst | Power BI Developer | Python Engineer",
    "email": "nikitasinghh2309@gmail.com",
    "linkedin": "https://linkedin.com/in/nikita-singhh-3943d33",
    "summary": "Data Analyst with 3+ years of experience bridging the gap between Backend Engineering and Data Analytics. With a strong foundation in Python, Django, and SQL, I specialize in building end-to-end data pipelines and creating actionable Power BI dashboards. I don't just visualize data; I architect the pipelines that extract, clean, and transform it."
}

skills = {
    "Data & Analytics": ["Power BI", "SQL", "Python (Pandas, NumPy)", "ETL Pipelines", "Data Modeling", "DAX"],
    "Backend & Engineering": ["Django", "FastAPI", "REST APIs", "PostgreSQL", "MySQL", "Git & CI/CD"]
}

experience = [
    {
        "role": "Data Analyst",
        "company": "Droot Teach",
        "duration": "Mar 2025 – Present",
        "points": [
            "Analyzed VPN platform data (users, servers, sessions) using Python and SQL across 10,000+ active users.",
            "Built and maintained Power BI dashboards tracking server health, country-wise usage, and real-time data consumption.",
            "Designed automated ETL pipelines to extract and transform raw session data into structured analytical datasets."
        ]
    },
    {
        "role": "Software Engineer",
        "company": "Upsquare Technologies",
        "duration": "Jan 2023 – Feb 2025",
        "points": [
            "Designed and managed relational databases (PostgreSQL, MySQL), writing complex analytical queries.",
            "Built and integrated 20+ RESTful APIs using Django REST Framework.",
            "Built CI/CD pipelines using Jenkins and GitLab for continuous deployment."
        ]
    },
    {
        "role": "Python Django Intern",
        "company": "Pysquad Informatics LLP",
        "duration": "Jun 2022 – Nov 2022",
        "points": [
            "Worked on end to end development of Django based application",
            "Used mysql to store and retrieve data",
            "Used rest framework to create APIs"
        ]
    }
]

projects = [
    {
        "title": "HRMS Backend API & Database Design",
        "tech": ["Python", "Django REST Framework", "PostgreSQL"],
        "description": "Architected the backend and database schemas for an enterprise Human Resource Management System (HRMS). Developed secure RESTful endpoints for employee onboarding, department tracking, and leave management workflows, optimizing relational queries for fast data retrieval.",
        "images": ["hrms_img.png"],
        "github": "https://github.com/niikitaassingh/hrms-management-system",
        "category": "backend"
    },
    {
        "title": "Property Rental Management API & Dashboard",
        "tech": ["Python", "Django", "Django REST Framework", "MySQL"],
        "description": "Engineered the RESTful backend API and database architecture for a Property Rental Management System. Developed robust endpoints for user authentication, real-time property listings, and rental application workflows, with query filters tracking occupancy, applications, and tenant status.",
        "images": ["propery_img.png"],
        "github": "https://github.com/niikitaassingh/Property-Rental",
        "category": "backend"
    },
    {
        "title": "HR Talent Analytics Portal",
        "tech": ["Power BI", "HR Analytics", "Data Cleaning", "DAX"],
        "description": "Comprehensive talent acquisition and workforce performance dashboard. Visualized employee attrition, department-wise headcount distribution, performance scores, and hiring funnel efficiency.",
        "images": ["hr_dashboard_1.png", "hr_dashboard_2.png", "hr_dashboard_3.png", "hr_dashboard_4.png"],
        "category": "powerbi"
    },
    {
        "title": "Global Sales & Revenue Intelligence Dashboard",
        "tech": ["Power BI", "Data Modeling", "DAX", "SQL"],
        "description": "Interactive Power BI dashboard tracking global sales KPIs, regional profitability, and product performance. Developed complex DAX measures for year-over-year growth and dynamic filtering.",
        "images": ["sales_dashboard_1.png", "sales_dashboard_2.png", "sales_dashboard_3.png", "sales_dashboard_4.jpeg"],
        "category": "powerbi"
    },
    {
        "title": "Meta Ads Campaign Marketing Analytics",
        "tech": ["Power BI", "Marketing Analytics", "ETL Pipelines", "SQL"],
        "description": "Campaign performance and ROAS analytics dashboard. Consolidated data from Meta Ads Manager to track Click-Through Rates (CTR), Conversion Rates, and Cost Per Acquisition (CPA) across ad sets.",
        "images": ["meta_dashboard_1.png", "meta_dashboard_2.png", "meta_dashboard_3.png"],
        "category": "powerbi"
    },
    {
        "title": "Real Estate Market Analysis & House Valuation Report",
        "tech": ["Power BI", "Data Analysis", "Python (Pandas)", "GIS Mapping"],
        "description": "Dynamic house pricing and geographic market report. Integrated GIS mapping to show average sales prices by zip code, pricing trends over time, and demographic correlation analysis.",
        "images": ["house_report_1.png", "house_report_2.png"],
        "category": "powerbi"
    }
]

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request,
            "profile": profile_data,
            "skills": skills,
            "experience": experience,
            "projects": projects
        }
    )

@app.post("/contact")
async def contact(
    name: str = Form(...),
    email: str = Form(...),
    subject: str = Form(...),
    message: str = Form(...)
):
    # Read SMTP config from .env
    smtp_host = os.getenv("SMTP_HOST", "smtp.gmail.com")
    smtp_port = int(os.getenv("SMTP_PORT", 587))
    smtp_user = os.getenv("SMTP_USERNAME")
    smtp_pass = os.getenv("SMTP_PASSWORD")
    receiver = os.getenv("RECEIVER_EMAIL")

    # Guard: if credentials are not configured yet, return a clear error
    if not smtp_pass or smtp_pass == "YOUR_APP_PASSWORD_HERE":
        return JSONResponse(
            status_code=503,
            content={"success": False, "message": "SMTP is not configured yet. Please add your App Password to the .env file."}
        )

    # Build the email
    msg = MIMEMultipart("alternative")
    msg["Subject"] = f"[Portfolio Inquiry] {subject}"
    msg["From"] = smtp_user
    msg["To"] = receiver
    msg["Reply-To"] = email  # So you can directly reply to the visitor

    html_body = f"""
    <html>
      <body style="font-family: Arial, sans-serif; background: #f4f4f4; padding: 20px;">
        <div style="max-width: 600px; margin: auto; background: #ffffff; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
          <div style="background: linear-gradient(135deg, #06b6d4, #8b5cf6); padding: 30px; text-align: center;">
            <h2 style="color: #ffffff; margin: 0;">New Portfolio Inquiry</h2>
          </div>
          <div style="padding: 30px;">
            <p style="font-size: 16px; color: #333;"><strong>From:</strong> {name} &lt;{email}&gt;</p>
            <p style="font-size: 16px; color: #333;"><strong>Subject:</strong> {subject}</p>
            <hr style="border: none; border-top: 1px solid #eee; margin: 20px 0;">
            <p style="font-size: 15px; color: #555; line-height: 1.7;">{message.replace(chr(10), '<br>')}</p>
            <hr style="border: none; border-top: 1px solid #eee; margin: 20px 0;">
            <p style="font-size: 13px; color: #aaa;">This message was sent via the contact form on your portfolio website.</p>
          </div>
        </div>
      </body>
    </html>
    """

    msg.attach(MIMEText(html_body, "html"))

    try:
        with smtplib.SMTP(smtp_host, smtp_port) as server:
            server.ehlo()
            server.starttls()         # Encrypt the connection
            server.login(smtp_user, smtp_pass)
            server.sendmail(smtp_user, receiver, msg.as_string())

        return JSONResponse(
            status_code=200,
            content={"success": True, "message": "Your message was sent successfully! I'll get back to you soon."}
        )

    except smtplib.SMTPAuthenticationError:
        return JSONResponse(
            status_code=401,
            content={"success": False, "message": "SMTP authentication failed. Please check your App Password in the .env file."}
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"success": False, "message": f"Failed to send message. Error: {str(e)}"}
        )

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)