# Cloudflare Pages Configuration

## Build Configuration
- Build command: (leave empty - static site)
- Build output directory: `/frontend`
- Root directory: `/`

## Environment Variables
Add these in Cloudflare Pages dashboard:
- `NODE_VERSION`: 18
- `API_URL`: https://rtb-planner-backend.onrender.com (update after Render deployment)

## Custom Headers (_headers file)
/*
  X-Frame-Options: DENY
  X-Content-Type-Options: nosniff
  X-XSS-Protection: 1; mode=block
  Referrer-Policy: strict-origin-when-cross-origin

## Redirects (_redirects file)
/api/* https://rtb-planner-backend.onrender.com/:splat 200
/* /index.html 200
