# Draft Portfolio - Maintenance Guide

Welcome to the Draft Portfolio codebase. This site is built using **Zola** (a static site generator) and styled with **SASS**. The architecture has been recently streamlined to a highly structured, text-heavy "Industrial Orange" aesthetic.

---

## 1. CSS & Theme Architecture

The core styles are entirely located in `sass/main.scss`. **All legacy CSS archives (`sass/archive.scss`) have been deleted** to ensure the codebase remains clean and strictly tied to the active design.

### Core Structure of `main.scss`:
1. **Dynamic Theme Tokens (`:root` & `[data-theme='dark']`)**:
   - The site uses a global Light/Dark mode toggle (saved to `localStorage`).
   - Core colors like `var(--bg-color)`, `var(--text-primary)`, `var(--link-color)`, and `var(--topbar-bg)` dynamically shift when the theme is toggled.
2. **Typography Classes**:
   - `.page-title`: Massive, uppercase editorial titles.
   - `.project-title`: Standard project listing titles.
   - `.project-subtitle`: Muted, secondary text (`var(--text-secondary)`).
   - `.content`: The primary wrapper for **all Markdown text**. It automatically handles paragraph spacing, link colors, typography, and constraints.
3. **Layout Components**:
   - `.topbar`: The fixed navigation header with frosted glass.
   - `.project-page`: The main max-width wrapper (`1024px`) that centers your content and images.

---

## 2. Managing Pages and Layouts

### Standard Projects
You do not need to write raw HTML to add a new project.
1. Create a new folder inside `/content/` (e.g., `/content/new-project/`).
2. Add an `_index.md` file inside that folder.
3. Use the following YAML front matter to select the aesthetic:
   ```yaml
   +++
   title = "Project Title"
   description = "Project subtitle or tagline"
   template = "project-light.html" # Standard industrial text layout
   # OR template = "project-dark.html" for the green CRT terminal aesthetic
   +++
   ```

### The About Page
The About page (`/about`) is **hardcoded** as a Parts List. If you need to update your bio, links, or profile picture, you must edit `templates/about.html` directly. The `content/about/_index.md` file is strictly used by Zola for routing.

### The Homepage
The homepage Parts List is **hardcoded in HTML** to allow for precise control over the layout, ordering, and hover images. 
To add a new project to the homepage, you must manually edit `templates/index.html` and append a new `<a class="part-row">` block. Zola's automatic page iteration is NOT used on the homepage.

### The 404 Page
The `/404.html` page uses a custom `SYS.ERR` terminal readout box. If you add "dead" links to the homepage Parts List (like `PRJ-09`), they should route directly to `@/404.html`.

---

## 3. Running & Building the Site

Because this is a Zola project, you need the Zola CLI installed to run it locally.
- **Local Development**: Run `zola serve` in the terminal. The site will be available at `http://127.0.0.1:8080` and will automatically refresh when you save files.
- **Production Build**: Run `zola build` in the terminal. This will generate the final minified HTML/CSS files into the `public/` directory, ready to be deployed to GitHub Pages, Netlify, or Vercel.

---

## 4. Working with Image Galleries

To ensure that grids remain responsive, masonry-style, and don't break the layout inside project pages, **do not write raw `<div>` grids in your markdown**.

Use the custom Zola shortcode: `{{ gallery(...) }}`.
```markdown
{{ gallery(images=["/img/joint/1.jpg", "/img/joint/2.jpg", "/img/joint/3.jpg"]) }}
```
This will compile into a responsive HTML grid and hook into the fullscreen lightbox functionality.

---

## 4. Strict CSS Rules
- **No Inline Colors**: Do not use `color: black` or `color: blue` in the SCSS. Always use the CSS variables (e.g., `var(--text-primary)`, `var(--accent)`) so styles shift correctly in dark mode.
- **Maintain Specificity**: Ensure you aren't adding redundant classes to `main.scss`. The file has been swept of dead code and duplicate properties.
