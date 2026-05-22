# Fitness Professional Website — Sushanth

## Overview
This project contains a modern, responsive fitness trainer website that supports two workflows:
- Local development with a Flask backend (for testing and optional server-side features)
- Static hosting for GitHub Pages using the `/docs` folder (no backend required)

The static site uses the midnight-blue theme (primary: #1a2942), a persistent light/dark toggle, and an embedded Google Form for client registration.

## Key Features
- Tabbed single-page UI (Home, Programs, Register)
- Midnight-blue theme with light/dark toggle (preference saved in `localStorage`)
- Responsive layout (desktop / tablet / mobile)
- Google Form embedded for registration (no server-side form required for GitHub Pages)
- Simple, dependency-light frontend (CSS variables, vanilla JS)
- Parallel `docs/` static site for GitHub Pages deployment

## Project Structure
```
fitness-site/
├── app.py                          # Flask backend for local development
├── requirements.txt                # Python dependencies (Flask, Werkzeug, ...)
├── README.md                       # This file (updated)
├── plan.md                         # Development plan and specs
├── templates/
│   └── index.html                  # Flask template (uses url_for for local dev)
├── static/
│   ├── css/                        # styles used by Flask dev server
│   │   └── style.css
│   ├── js/
│   │   └── script.js               # theme & tab logic
│   └── images/                      # images for local dev
│       ├── hero.jpg
│       ├── profile.jpg
│       ├── certificate1.jpg
│       ├── logo.svg
│       └── programs/               # program images (program1/2/3)
├── docs/                            # Static site for GitHub Pages (mirror of static/ + index.html)
│   ├── index.html                   # static landing page for GitHub Pages
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   ├── images/
│   │   ├── logo.svg                # placeholder logo included
│   │   └── programs/               # add program images here for GH Pages
│   ├── DEPLOYMENT.md               # Guide for publishing to GitHub Pages
│   └── plan.md                     # docs-specific plan and notes
│   └── .nojekyll
├── forms/
│   └── registration_handler.py     # (optional) server-side handler for local dev
├── models/
│   └── enquiry_model.py            # (optional) DB models
└── database/
    └── enquiries.db                # (optional) SQLite DB for local dev
```

## Setup — Local Development (Flask)
1. Create a virtual environment and activate it:

```powershell
cd c:\Sushanth\fyttr
python -m venv .venv
.venv\Scripts\Activate.ps1
```

2. Install Python dependencies:

```powershell
cd fitness-site
pip install -r requirements.txt
```

3. Run the Flask app:

```powershell
python app.py
```

4. Open `http://localhost:5000` in your browser.

Notes:
- The Flask app is useful for testing server-side flows and the original `/register` POST route. When deploying static to GitHub Pages, the site uses the Google Form instead of the backend handler.

## Static Site — GitHub Pages
The `/docs` folder contains a fully static copy of the site suitable for GitHub Pages. Key files:

- `docs/index.html` — static landing page (relative paths)
- `docs/css/style.css` — theme and responsive styles
- `docs/js/script.js` — theme toggle and tab switching
- `docs/images/` — add your images and `logo.svg` here
- `docs/DEPLOYMENT.md` — step-by-step publish guide
- `docs/.nojekyll` — prevents GitHub Pages from ignoring files that start with `_`

Quick test (serve docs locally):

```powershell
# From repository root
python -m http.server 8000
# Visit: http://localhost:8000/docs/
```

GitHub Pages deployment steps:

1. Commit and push the repository to GitHub.
2. In the repository Settings → Pages, choose branch `main` (or your branch) and folder `/docs`.
3. Save; wait a minute for the site to publish at `https://<your-username>.github.io/<repo>/`.

## Images & Logo
Current repository state:

- `static/images/` contains: `hero.jpg`, `profile.jpg`, `certificate1.jpg`, `logo.svg`, and a `programs/` folder.
- `docs/images/` currently contains `logo.svg` and a `programs/` folder (add other images here before publishing).

Recommended images to place before publishing to GitHub Pages:

- `hero.jpg` — 1920x1080 recommended
- `profile.jpg` — 400x500 recommended
- `certificate1.jpg` — 400x300 recommended
- `programs/program1.jpg`, `programs/program2.jpg`, `programs/program3.jpg` — 600x400 recommended
- `logo.svg` or `logo.png` — header logo (~50x50)

Keep copies in both `static/images/` (for local Flask testing) and `docs/images/` (for the static site) so both environments render correctly.

## Theme & Styling
- Primary: `#1a2942` (midnight blue)
- Secondary: `#4a90e2`
- Accent: `#e8b923`

Theme preference (light/dark) is saved to `localStorage` so users keep their choice across pages.

## Registration Form
The static site embeds your Google Form for registration. Current embedded form URL:

https://forms.gle/j6MpBG2G5pkLznLa9

Notes:
- For GitHub Pages the form handles submissions and stores responses in your Google account.
- If you prefer server-side storage, use the Flask `/register` route and the `forms/registration_handler.py` file locally.

## Technologies
- Backend: Flask 3.0+ (used for local development)
- Frontend: HTML5, CSS3 (variables), JavaScript (vanilla)
- Optional: SQLite3 for local enquiry storage

## Deployment Targets
- Static: GitHub Pages (recommended for this repo)
- Dynamic: Any Python-capable host (Heroku, PythonAnywhere, AWS) if you need server-side features

## To Do / Next Steps
- Add real images to `static/images/` and `docs/images/` before publishing
- Replace `docs/images/logo.svg` with your official logo
- Update contact information in both `templates/index.html` and `docs/index.html`

## License
MIT License — free to use and modify

---

If you'd like, I can now add placeholder images to `docs/images/` and update `docs/index.html` image references, or push these changes to GitHub for you.