# World Well-Being Forum

Official website project for the World Well-Being Forum.

## Mission

An integrated vision of human and planetary well-being through health, humanitarian action, environmental protection, education, technology and international collaboration.

## Core areas

- Health & Well-Being
- Clean Water & Environment
- Food & Essentials
- Education
- Technology for Good
- Humanitarian Action
- Community Development

## Global focus

India, New Zealand and the development of international partnerships. Aspirations and areas of focus must not be presented as established offices or completed projects.

## Development

This project preserves the original static HTML architecture. It has no JavaScript package dependencies. Python 3 is required for the local server and build. Node/npm is optional for the command aliases.

```sh
npm run dev
npm run build
npm run preview
```

Without npm, use `python3 scripts/build.py` to build and `python3 -m http.server 4173 --directory dist` to preview.

## Project structure

- Root `.html` files: editable page content, including legacy entry points.
- `assets/style.css`: shared responsive design.
- `assets/script.js`: accessible navigation, enquiry selection and preview form handling.
- `assets/landscape.jpg`: landscape hero.
- `scripts/build.py`: generates directory routes, validates links and produces `dist/`.
- `.openai/hosting.json`: private Sites deployment configuration.

Clean directory routes (`/about/`, `/our-work/`, `/founder/`, etc.) are generated from root HTML. Edit root HTML, then build. Keep shared header/footer changes consistent across root pages. Existing `.html` URLs remain available.

## Content guidelines

Focus on practical community impact. Distinguish completed service, current work and future initiatives. The supplied narrative informs founder content; underlying certificates and original CV were not supplied. Avoid unsupported health claims or unverified medical titles. Do not present naturopathy as a cancer treatment or substitute for medical care. Use Sadhna Dixit, Founder & Visionary Leader.

A genuine founder portrait and original brand assets are still needed. The supplied composite was treated as visual inspiration; its synthetic portrait and program scenes were not presented as documentary photographs. The hero landscape illustrates the setting, not a Forum project.

## Accessibility

Semantic landmarks, skip navigation, keyboard access, visible focus indicators, labelled forms, responsive type and reduced-motion support are included. The decorative landscape uses a CSS background. The build checks local links, assets, form actions and anchors. Manual desktop/mobile, keyboard, 200% zoom and contrast review is recommended before public launch; automated link checks do not establish WCAG conformance.

## Forms and donations

GitHub Pages is the static hosting provider. There is no form or payment backend. Submission buttons are disabled in HTML, and an additional JavaScript guard prevents form submissions. No contact data is sent or acknowledged as received. Connect a verified service before enabling enquiries or newsletter subscriptions. Donation links lead to a transparent support enquiry; no payment processor or verified donation destination was supplied.

## Images and brand

Deep green, deep blue, white and warm neutral surfaces. Georgia headings and system sans-serif body copy avoid external font dependencies.

Landscape: Lake Tekapo and Southern Alps, Rebecca Clarke / Unsplash.
Source: https://unsplash.com/photos/a-large-body-of-water-surrounded-by-mountains-6LKdV82t42U
License: https://unsplash.com/license

The existing `hero.jpg` social-preview image and metadata were retained. Replace only with an approved sharing asset. Prefer optimized WebP/AVIF for future assets; avoid large originals. Obtain permission for identifiable photographs.

## Deployment

Run the build, verify responsive layouts and accessibility, check metadata and links, confirm authentic imagery, validate founder details and current program status, and confirm working contact and donation destinations. Deploy the contents of `dist/`. The generated sitemap uses SITE_URL; the Pages workflow supplies the configured GitHub Pages URL.

© World Well-Being Forum. All rights reserved, except third-party imagery under its respective license.

## GitHub Pages and pull requests

The site remains entirely static. `.github/workflows/pages.yml` checks pull requests and automatically publishes pushes to `main` using GitHub Pages Actions. Pull requests never deploy and have read-only repository permissions. Only the deployment job receives Pages write and OIDC permissions.

The intended Pages address is https://world-wellbeing-forum.github.io/website/. Enable **Settings → Pages → Source → GitHub Actions**. Merge the pull request to trigger the first deployment; later merges deploy automatically. The workflow can also be run manually on `main`.

The build rewrites navigation, images, CSS background URLs and form actions for the configured base path. It also generates a matching sitemap, robots file and `.nojekyll`. Private Sites configuration and repository files are excluded from the published artifact.

```sh
python3 scripts/check_build.py
BASE_PATH=/website SITE_URL=https://world-wellbeing-forum.github.io/website python3 scripts/build.py
```

`check_build.py` exercises both root hosting and `/website` hosting and checks every emitted local navigation link and referenced asset. For local preview at `/`, run the normal build again. For a custom domain, the workflow uses the Pages configuration to select the URL and path automatically.

GitHub Pages has no form or payment backend. Forms clearly report that online submissions are unavailable. Donations remain an informational support enquiry until a verified destination is supplied. The private Sites deployment is retained separately; this workflow does not update or delete it.
