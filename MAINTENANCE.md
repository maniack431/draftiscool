# Draft Portfolio - Maintenance Guide

This site is built using **Zola** (a static site generator) and follows an ultra-minimalist, HTML-first design philosophy inspired by minimalist sites like motherfuckingwebsite.com.

---

## 1. Design Philosophy & Styling

- **HTML-First & Lightweight**: No external CSS frameworks, no Google Fonts, no Font Awesome icon bundles, and no JavaScript libraries, lightboxes, or theme switchers.
- **Typography**: Uses the browser's default serif font for a raw, high-performance, and distraction-free reading experience.
- **Layout Container**: All pages are centered within a clean `max-width: 800px; margin: 0 auto; padding: 1rem;` container, ensuring comfortable line lengths on desktop and automatic responsiveness on mobile devices.
- **Navigation & Permanent Footer**:
  - The top navigation in `templates/base.html` provides simple pipe-separated links followed by an `<hr>`.
  - The permanent footer is right-aligned at the bottom of every page:
    ```html
    <hr>
    <footer>
        <p style="text-align: right;">sahib &lt;3</p>
    </footer>
    ```

---

## 2. Image Handling & Grid Rules

### Aspect Ratio & Cropping
- **Default 4:3 Crop**: Full-width project images and gallery grid thumbnails are styled with `aspect-ratio: 4 / 3; object-fit: cover;` to maintain uniform 4:3 framing.
- **Click to Enlarge**: All images are wrapped in `<a href="..." target="_blank">` so clicking any image opens the raw, uncropped file in a new browser tab at its original aspect ratio and full resolution.
- **Small Icons**: Inline utility icons (e.g. Creative Commons license icons) explicitly use `width="20"` so they remain natural size and are never forced into 4:3 blocks.

### The "Humane Enough" Exception
- Images on the **Humane Enough** page (`content/humane_enough/_index.md` via `templates/project-dark.html`) are exempted from the 4:3 crop.
- They render inside `<div class="no-crop">` and maintain their original, uncropped aspect ratios while scaling responsively to screen width.

### Image Grids
Grids are built with standard HTML tables:
- **Markdown Tables**: 3-column `<table>` rows with images wrapped in `.crop` blocks.
- **Gallery Shortcode**: You can also use the custom Zola shortcode in markdown:
  ```markdown
  {{ gallery(dir="/img/path/", images=["1.jpg", "2.jpg", "3.jpg"]) }}
  ```
  This will render a clean, 3-column responsive table with 4:3 cropped cells and click-to-enlarge links.

---

## 3. Templates & Page Directory

- `templates/base.html`: The base HTML shell containing the responsive meta tags, container wrapper, topbar navigation, and permanent right-aligned footer.
- `templates/index.html`: Homepage rendering the `<h1>Work</h1>` heading and a clean list (`<ul>`) of project links (with `<del>` strikethrough for WIP items).
- `templates/about.html`: Minimalist bio paragraph with direct contact/profile links.
- `templates/404.html`: Minimal error page with a direct link back to home.
- `templates/project-light.html`: Standard template for project entries.
- `templates/project-dark.html`: Project template for pages requiring uncropped images (Humane Enough).
- `templates/shortcodes/gallery.html`: 3-column responsive table grid shortcode.

---

## 4. Running & Building the Site

Because this is a Zola project, you need the Zola CLI installed:
- **Local Development**: Run `zola serve` in the terminal to view at `http://127.0.0.1:8080`.
- **Production Build**: Run `zola build` to output the final static site into the `public/` directory.
