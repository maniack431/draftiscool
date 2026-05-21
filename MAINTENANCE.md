# Draft Portfolio - Maintenance Guide

Welcome to the Draft Portfolio codebase. This site is built using **Zola** (a static site generator) and styled with **SASS**. The architecture has been refined to make ongoing updates as frictionless as possible.

---

## 1. CSS & Theme Architecture

The core styles are located in `sass/main.scss`. All unused, experimental, and legacy CSS from older iterations of the site have been moved to `sass/archive.scss` to keep the main stylesheet extremely clean.

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

## 2. Adding New Projects

You do not need to write raw HTML to add a new project. Zola handles the templating via global master templates.

1. Create a new folder inside `/content/` (e.g., `/content/new-project/`).
2. Add an `_index.md` file inside that folder.
3. Use the following YAML front matter to select the aesthetic:
   ```yaml
   +++
   title = "Project Title"
   description = "Project subtitle or tagline"
   template = "project-light.html" # Use project-light.html for standard projects
   # OR use template = "project-dark.html" for the specialized CRT terminal aesthetic
   +++
   ```
4. Write your text in standard Markdown. It will automatically be styled beautifully by the `.content` CSS class.

---

## 3. Working with Image Galleries

To ensure that grids remain responsive, masonry-style, and don't break the layout, **do not write raw `<div>` grids in your markdown**.

Instead, use the custom Zola shortcode: `{{ gallery(...) }}`.

### Example Usage in Markdown:
```markdown
{{ gallery(images=["/img/joint/1.jpg", "/img/joint/2.jpg", "/img/joint/3.jpg"]) }}
```
This single line will automatically compile into the full, responsive, hover-animated HTML grid layout, and instantly hook into the fullscreen lightbox functionality.

---

## 4. Strict CSS Rules
- **No Inline Colors**: Do not use `color: black` or `color: blue` in the SCSS. Always use `var(--text-primary)`, `var(--text-secondary)`, or `var(--link-color)` so your styles don't break when a user activates Dark Mode.
- **Maintain Specificity**: If a style isn't applying, check if a broader utility class (like `.nav-link` or `.content`) is overriding it with an `!important` tag before resorting to extreme CSS selectors.
