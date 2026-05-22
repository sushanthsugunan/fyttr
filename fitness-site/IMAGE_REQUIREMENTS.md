# Image Requirements for Fitness Website

## Complete Image Checklist with Specifications

All images should be placed in the `static/images/` directory as specified.

---

### 1. **Logo & Branding**

| Image Name | Location | Size | Format | Purpose | Notes |
|---|---|---|---|---|---|
| logo.svg | static/images/ | 50×50 px | SVG | Website header logo | Transparent background, scale-friendly |
| favicon.ico | static/images/ | 32×32 px | ICO | Browser tab icon | Display next to page title |

---

### 2. **Hero Section**

| Image Name | Location | Size | Format | Purpose | Notes |
|---|---|---|---|---|---|
| hero.jpg | static/images/ | 1920×1080 px | JPG | Hero background image | High quality, fitness-related (gym/trainer) |

---

### 3. **About Section**

| Image Name | Location | Size | Format | Purpose | Notes |
|---|---|---|---|---|---|
| profile.jpg | static/images/ | 500×600 px | JPG | Profile picture | Professional headshot, clean background |

---

### 4. **Certifications Section - NEW LOGOS REQUIRED**

| Image Name | Location | Size | Format | Purpose | Notes |
|---|---|---|---|---|---|
| diploma-logo.png | static/images/ | 300×200 px | PNG | Diploma certification logo | Should represent "Advance Diploma in Fitness Training" |
| nutritionist-logo.png | static/images/ | 300×200 px | PNG | Nutritionist certification logo | Should represent nutrition/diet expertise |
| karate-logo.png | static/images/ | 300×200 px | PNG | Karate certification logo | Should represent martial arts/karate |
| kalaripayattu-logo.png | static/images/ | 300×200 px | PNG | Kalaripayattu certification logo | Should represent traditional martial art |

---

### 5. **Programs Section**

| Image Name | Location | Size | Format | Purpose | Notes |
|---|---|---|---|---|---|
| program1.jpg | static/images/programs/ | 600×400 px | JPG | Fat Loss Transformation | People doing cardio/weight loss workout |
| program2.jpg | static/images/programs/ | 600×400 px | JPG | Strength Training Mastery | Strength training/gym environment |
| program3.jpg | static/images/programs/ | 600×400 px | JPG | Home Based Training | Home workout/minimal equipment setup |

---

## Directory Structure

```
static/images/
├── logo.svg (50×50)
├── favicon.ico (32×32)
├── hero.jpg (1920×1080)
├── profile.jpg (500×600)
├── diploma-logo.png (300×200) ⭐ NEW
├── nutritionist-logo.png (300×200) ⭐ NEW
├── karate-logo.png (300×200) ⭐ NEW
├── kalaripayattu-logo.png (300×200) ⭐ NEW
└── programs/
    ├── program1.jpg (600×400)
    ├── program2.jpg (600×400)
    └── program3.jpg (600×400)
```

---

## Image Specifications & Best Practices

### For JPG Files (Photos):
- **Quality**: 85-90% compression
- **Color Profile**: sRGB
- **Recommended Tool**: Photoshop, GIMP, or online compressors
- **Use for**: Photos, backgrounds, real people

### For PNG Files (Logos):
- **Background**: Transparent (RGBA)
- **Quality**: Lossless compression
- **Recommended Tool**: Adobe Illustrator, Canva, or Figma
- **Use for**: Logos, icons, graphics with transparency

### For SVG Files (Scalable):
- **Vector Format**: Automatically scales to any size
- **Color**: Can be customized with CSS
- **Recommended Tool**: Adobe Illustrator or online editors
- **Use for**: Logo (maintains quality at all sizes)

---

## Certification Logos Recommendations

### 1. **Diploma Logo** (diploma-logo.png - 300×200)
- Design: Diploma/certificate rolled scroll icon
- Colors: Should complement brand (incorporate red/cyan)
- Style: Professional, modern
- Content: Diploma symbol with "Advance Fitness Training" text or just the diploma

### 2. **Nutritionist Logo** (nutritionist-logo.png - 300×200)
- Design: Plate/bowl with healthy food items
- Colors: Green tones complementing brand
- Style: Modern, clean
- Content: Healthy foods, nutrition-focused

### 3. **Karate Logo** (karate-logo.png - 300×200)
- Design: Karate gi (uniform), belt, or martial stance
- Colors: Traditional karate (white/red/blue)
- Style: Dynamic, powerful
- Content: Shotokan Karate symbol or belt

### 4. **Kalaripayattu Logo** (kalaripayattu-logo.png - 300×200)
- Design: Traditional Indian martial art pose/weapon
- Colors: Warm Indian tones (saffron/gold)
- Style: Traditional yet modern
- Content: Kalaripayattu warrior stance or traditional weapon

---

## Important Notes

⚠️ **Before Final Deployment:**
1. Ensure all images are optimized for web (compressed but good quality)
2. Replace placeholder images with actual content
3. Test on different devices (mobile, tablet, desktop)
4. Verify all image paths are correct in static/images/ directory
5. Check that PNG logos have transparent backgrounds
6. Ensure responsiveness - images should look good on all screen sizes

---

## File Size Guidelines

| Format | Typical Size | Max Recommended |
|---|---|---|
| Logo (SVG) | 10-50 KB | 100 KB |
| Logo (PNG) | 50-200 KB | 300 KB |
| Hero Image (JPG) | 150-300 KB | 500 KB |
| Program Images (JPG) | 100-200 KB | 300 KB |
| Profile Photo (JPG) | 100-200 KB | 300 KB |

---

## Quick Setup Instructions

1. Create the directory structure as shown above
2. Add all images to their respective locations
3. Ensure filenames match exactly (case-sensitive)
4. Test the website locally to verify all images load
5. Use browser DevTools to check for any broken image links (404 errors)

---

**Status**: ✅ Website is now configured to display professional logos for all certifications
**Next Step**: Replace all placeholder images with actual images matching specifications above
