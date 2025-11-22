@echo off
echo Committing and pushing changes...
git add .
git commit -m "Fix Vercel deployment: update vite.config.js and vercel.json"
git push origin main
echo Done!
pause
