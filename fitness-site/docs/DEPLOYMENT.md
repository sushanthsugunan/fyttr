# GitHub Pages Deployment Guide

## ✅ Setup Complete for GitHub Pages

All static files are ready in the `/docs` folder for GitHub Pages deployment.

### File Structure
```
docs/
├── index.html           (Main landing page)
├── css/
│   └── style.css        (All styles, light/dark theme)
├── js/
│   └── script.js        (Tab switching, theme toggle)
└── images/
    ├── logo.svg         (Placeholder - replace with your logo)
    ├── hero.jpg         (Replace with your hero banner)
    ├── profile.jpg      (Replace with your profile photo)
    ├── certificate1.jpg (Replace with your certification)
    └── programs/
        ├── program1.jpg (Replace - Fat Loss)
        ├── program2.jpg (Replace - Strength)
        └── program3.jpg (Replace - Home-Based)
```

### Deployment Steps

#### 1. **Replace Logo**
- Replace `images/logo.svg` with your actual logo (PNG or SVG)
- Update reference in `index.html` if filename changes

#### 2. **Add Required Images**
Place all 5 images in the correct directories:
- `images/hero.jpg` - Hero section banner
- `images/profile.jpg` - Your profile photo
- `images/certificate1.jpg` - Your certification
- `images/programs/program1.jpg` - Program 1 image
- `images/programs/program2.jpg` - Program 2 image
- `images/programs/program3.jpg` - Program 3 image

#### 3. **Update Contact Information**
Edit `index.html` and replace:
- `sushanth@fitness.com` - Your email
- `+91 XXXX XXXX XX` - Your phone number
- `+91 XXXX XXXX XX` - Your WhatsApp number
- `City, State` - Your location

#### 4. **Enable GitHub Pages**
1. Push this `/docs` folder to GitHub
2. Go to Repository Settings → Pages
3. Select "Deploy from a branch"
4. Choose branch: main (or your branch)
5. Select folder: `/docs`
6. Click Save

Your site will be live at: `https://yourusername.github.io/repository-name/`

### Features Included
✅ **Midnight Blue Theme** (#1a2942, #4a90e2, #e8b923)  
✅ **Light/Dark Mode Toggle** - Persists in browser  
✅ **3 Tab Navigation** - Home, Programs, Register  
✅ **Google Form Integration** - All submissions go to your Google Form  
✅ **Fully Responsive** - Works on mobile, tablet, desktop  
✅ **No Backend Required** - 100% static hosting  

### Important Notes
- ⚠️ The register form uses your Google Form (embedded iframe)
- ✅ All data goes directly to your Google Drive
- ✅ Works perfectly on GitHub Pages (static site)
- 📸 Replace all placeholder images before deployment

### Local Testing
To test locally:
1. Open `/docs/index.html` directly in browser, OR
2. Use a local server:
   ```bash
   python -m http.server 8000
   # Then visit: http://localhost:8000/docs/
   ```

---

**Ready to deploy!** Push the `/docs` folder to GitHub and enable GitHub Pages. ✨
