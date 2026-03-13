from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

instructions = [
    "GitHub Push Workflow (Windows, VS Code)",
    "", 
    "1. Initialize repository (first time):",
    "   git init", 
    "   git add .", 
    "   git commit -m \"Initial commit\"",
    "   git branch -M main", 
    "   git remote add origin <URL_OF_YOUR_REMOTE_REPO>",
    "   git push -u origin main", 
    "", 
    "2. Regular workflow when code changes or new files: ",
    "   git status", 
    "   git add <files> (or git add . to stage all)",
    "   git commit -m \"describe changes\"", 
    "   git push", 
    "", 
    "3. If you have multiple branches: ",
    "   git checkout -b new-branch", 
    "   git push -u origin new-branch", 
    "", 
    "4. Getting updates from remote: ",
    "   git pull", 
    "", 
    "5. Viewing logs and differences:",
    "   git log --oneline", 
    "   git diff", 
    "", 
    "6. Adding more files later: just stage + commit + push as above.",
    "", 
    "Additional Notes:",
    "- Configure name/email once: git config --global user.name \"Your Name\"", 
    "  git config --global user.email \"you@example.com\"", 
    "- Use VS Code Source Control panel as GUI alternative.",
]

c = canvas.Canvas("GitHub_Workflow.pdf", pagesize=letter)
width, height = letter
textobject = c.beginText(40, height - 40)
textobject.setFont("Times-Roman", 12)
for line in instructions:
    textobject.textLine(line)
c.drawText(textobject)
c.showPage()
c.save()
print("PDF generated as GitHub_Workflow.pdf")
