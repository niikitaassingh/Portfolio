# 🌟 Premium Dark Theme Developer & Data Analyst Portfolio

A high-performance, modern, and interactive single-page portfolio website designed for developers, data analysts, and Power BI experts. Built on **FastAPI** (Python), **Jinja2 Templates**, and **Custom Vanilla CSS**, it showcases dynamic client-side filtering, interactive full-screen screenshot lightboxes, and a live secure SMTP contact form.

---

## 🎨 Design & Aesthetic Highlights

- **Obsidian & Slate Theme**: Premium dark interface built using a refined slate color palette (`#070a13`), glassmorphic panels, and neon linear gradients (cyan-to-violet).
- **Polished Typography**: Seamless typography integrating **Outfit** (for high-contrast bold titles) and **Inter** (for high-readability body copy).
- **Dynamic Interaction & Micro-Animations**: Smooth hover effects, glow indicators on buttons/scrollbars, and instant client-side transitions.
- **Aspect Ratio Safeguards**: Custom dashboard container frames ensuring Power BI dashboards and screenshots preserve their aspect ratios without cropping.
- **Fail-Safe Asset Loading**: Advanced JavaScript handlers on images catch CDN or file failures instantly and render beautifully styled **inline SVG placeholders** to keep the page's structure pristine.

---

## 🚀 Key Features

1. **FastAPI & Jinja2 Backend**: Ultra-fast routing rendering dynamic data models cleanly.
2. **Client-Side Project Filtering**: Categorize and filter projects instantly (e.g. `Power BI & Analytics` vs. `Backend & APIs`) without page reloads.
3. **Interactive Lightbox Pop-up**: Click dashboard screenshots or diagrams to view full-resolution, overlay previews. Includes Escape-key close listeners.
4. **Responsive Mobile & Tablet Layout**: Fully custom styling tailored for smaller touch screens, with an auto-collapsing sticky navbar on option selection.
5. **Secure SMTP Form Integration**: AJAX-powered contact form with loading states, secure back-end SMTP handler, and gorgeous visual toast notifications.

---

## 📂 Project Directory Structure

```text
portfolio/
├── main.py                     # FastAPI backend (project/experience models & SMTP routes)
├── requirements.txt            # Python dependencies
├── .env                        # Local SMTP credentials (excluded via gitignore)
├── .gitignore                  # Git untracked files setup
├── venv/                       # Local Python virtual environment
└── static/
    ├── css/
    │   └── style.css           # Premium stylesheet & animations
    ├── images/                 # Local assets (screenshots, profile pictures)
    └── templates/
        └── index.html          # Jinja2-powered main page structure & JavaScript
```

---

## 🔧 Installation & Setup

### 1. Clone the repository
Navigate into your target working directory:
```bash
cd portfolio
```

### 2. Set up a Python Virtual Environment
Initialize and activate your environment:
```powershell
# Windows
python -m venv venv
.\venv\Scripts\activate
```

### 3. Install Dependencies
Install all required libraries listed in `requirements.txt`:
```powershell
pip install -r requirements.txt
```

### 4. Configure Your Environment Variables (`.env`)
Create a `.env` file in the root directory (based on the sample format):
```env
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=your-email@gmail.com
SMTP_PASSWORD=your-16-character-app-password
RECEIVER_EMAIL=your-email@gmail.com
```

> [!IMPORTANT]
> **Generating a Gmail App Password:**
> 1. Go to your Google Account -> **Security** ([myaccount.google.com/security](https://myaccount.google.com/security)).
> 2. Ensure **2-Step Verification** is enabled.
> 3. Search for **"App Passwords"** at the top.
> 4. Choose App: `Mail` and Device: `Other (custom name)` (e.g., `Portfolio`).
> 5. Click **Generate** and copy the **16-character password** (strip any spaces) into your `.env` as the `SMTP_PASSWORD`.

---

## 💻 Running the Server

Make sure to run Uvicorn from inside your active virtual environment.

```powershell
# Run the local development server with auto-reload enabled
.\venv\Scripts\uvicorn main:app --reload
```

Once running, open your browser and navigate to:
🔗 **`http://127.0.0.1:8000/`**

---

## 🛡️ License
Designed and crafted by {{ profile.name }}. All rights reserved.
