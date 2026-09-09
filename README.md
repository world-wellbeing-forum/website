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

The existing Netlify Forms integration is retained, and the previous newsletter acknowledgement-only interaction has been replaced with a real Netlify form declaration. Enable form detection and recipient notifications on the existing Netlify host, then verify actual receipt. Sites and local previews do not provide Netlify Forms: submissions are intercepted and clearly marked unavailable, never acknowledged as sent. Connect a functioning backend before launching on another host. Donation links lead to a transparent support enquiry; no payment processor or verified donation destination was supplied.

## Images and brand

Deep green, deep blue, white and warm neutral surfaces. Georgia headings and system sans-serif body copy avoid external font dependencies.

Landscape: Lake Tekapo and Southern Alps, Rebecca Clarke / Unsplash.
Source: https://unsplash.com/photos/a-large-body-of-water-surrounded-by-mountains-6LKdV82t42U
License: https://unsplash.com/license

The existing `hero.jpg` social-preview image and metadata were retained. Replace only with an approved sharing asset. Prefer optimized WebP/AVIF for future assets; avoid large originals. Obtain permission for identifiable photographs.

## Deployment

Run the build, verify responsive layouts and accessibility, check metadata and links, confirm authentic imagery, validate founder details and current program status, and confirm working contact and donation destinations. Deploy the contents of `dist/`. The generated sitemap uses the private Sites origin; update it if moving to a public domain.

© World Well-Being Forum. All rights reserved, except third-party imagery under its respective license.
