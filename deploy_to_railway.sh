#!/bin/bash

# RTB Document Planner - Railway Deployment Script
# This script prepares and guides you through Railway deployment

echo "🚂 RTB DOCUMENT PLANNER - RAILWAY DEPLOYMENT"
echo "=============================================="
echo ""

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Step 1: Initialize Git Repository
echo -e "${BLUE}STEP 1: Initializing Git Repository${NC}"
if [ -d .git ]; then
    echo -e "${GREEN}✓ Git repository already initialized${NC}"
else
    git init
    echo -e "${GREEN}✓ Git repository initialized${NC}"
fi
echo ""

# Step 2: Create .gitignore
echo -e "${BLUE}STEP 2: Creating .gitignore${NC}"
cat > .gitignore << 'EOF'
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Database
*.db
*.sqlite
*.sqlite3

# Environment
.env
.env.local

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Logs
*.log

# Uploads
backend/uploads/*
!backend/uploads/.gitkeep

# Temporary files
*.tmp
*.temp
temp/
tmp/
EOF
echo -e "${GREEN}✓ .gitignore created${NC}"
echo ""

# Step 3: Add all files
echo -e "${BLUE}STEP 3: Adding files to Git${NC}"
git add .
echo -e "${GREEN}✓ Files added${NC}"
echo ""

# Step 4: Commit
echo -e "${BLUE}STEP 4: Creating initial commit${NC}"
git commit -m "Initial commit - RTB Document Planner ready for Railway deployment" 2>/dev/null || echo -e "${YELLOW}⚠ No changes to commit or already committed${NC}"
echo ""

# Step 5: Instructions for GitHub
echo -e "${BLUE}STEP 5: Push to GitHub${NC}"
echo -e "${YELLOW}You need to create a GitHub repository first:${NC}"
echo ""
echo "1. Go to: https://github.com/new"
echo "2. Repository name: rtb-document-planner"
echo "3. Description: Professional TVET Session Plans & Schemes of Work Generator"
echo "4. Make it Public or Private (your choice)"
echo "5. DO NOT initialize with README, .gitignore, or license"
echo "6. Click 'Create repository'"
echo ""
echo -e "${YELLOW}After creating the repository, run these commands:${NC}"
echo ""
echo -e "${GREEN}git remote add origin https://github.com/YOUR-USERNAME/rtb-document-planner.git${NC}"
echo -e "${GREEN}git branch -M main${NC}"
echo -e "${GREEN}git push -u origin main${NC}"
echo ""

# Step 6: Railway Instructions
echo -e "${BLUE}STEP 6: Deploy to Railway${NC}"
echo ""
echo "After pushing to GitHub:"
echo ""
echo "1. Go to: https://railway.app"
echo "2. Click 'Login' and sign in with GitHub"
echo "3. Click 'New Project'"
echo "4. Select 'Deploy from GitHub repo'"
echo "5. Choose 'rtb-document-planner'"
echo "6. Click 'Deploy Now'"
echo ""
echo "7. Add PostgreSQL Database:"
echo "   - Click 'New' → 'Database' → 'Add PostgreSQL'"
echo "   - Wait for provisioning"
echo ""
echo "8. Configure your service:"
echo "   - Click on web service"
echo "   - Go to 'Settings'"
echo "   - Verify build command: cd backend && pip install -r requirements.txt"
echo "   - Verify start command: cd backend && uvicorn main:app --host 0.0.0.0 --port \$PORT"
echo ""
echo "9. Generate domain:"
echo "   - Go to 'Settings' → 'Domains'"
echo "   - Click 'Generate Domain'"
echo "   - Copy the URL"
echo ""
echo "10. Update frontend/config.js with your Railway URL"
echo "11. Commit and push changes"
echo "12. Deploy frontend to Cloudflare Pages"
echo ""

# Summary
echo -e "${BLUE}=============================================="
echo "DEPLOYMENT FILES READY!"
echo -e "==============================================${NC}"
echo ""
echo -e "${GREEN}✓ railway.json${NC} - Railway configuration"
echo -e "${GREEN}✓ nixpacks.toml${NC} - Build configuration"
echo -e "${GREEN}✓ Procfile${NC} - Start command"
echo -e "${GREEN}✓ .gitignore${NC} - Git ignore rules"
echo -e "${GREEN}✓ Git repository${NC} - Initialized and committed"
echo ""
echo -e "${YELLOW}Next steps:${NC}"
echo "1. Create GitHub repository"
echo "2. Push code to GitHub"
echo "3. Deploy to Railway"
echo "4. Update frontend config"
echo "5. Deploy frontend to Cloudflare Pages"
echo ""
echo -e "${BLUE}For detailed instructions, see: RAILWAY_DEPLOYMENT_COMPLETE.md${NC}"
echo ""
echo -e "${GREEN}Good luck with your deployment! 🚀${NC}"
