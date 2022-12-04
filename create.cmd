:create
    python create.py %1
    cd My Projects/
    cd %1
    git init
    type nul > Readme.md
    git add .
    git commit -m "Initial commit"
    git branch -M main
    git remote add origin https://github.com/rohit133/%1.git
    git push -u origin main
    code .
EXIT /B 0