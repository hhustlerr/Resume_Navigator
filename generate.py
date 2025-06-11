from jinja2 import Environment, FileSystemLoader
import subprocess
import os
from datetime import date



# Use custom Jinja delimiters to avoid LaTeX conflict
env = Environment(
    loader=FileSystemLoader('.'),
    block_start_string='((%',
    block_end_string='%))',
    variable_start_string='((',
    variable_end_string='))',
    comment_start_string='((#',
    comment_end_string='#))'
)

# Step 1: Fill user data
user_data = {
    "Name": "Doni Singh Agrawal",
    "contact": 
    {
        "email": "donisingh@gmail.com",
        "phone": "+91-87693 88932",
        "linkedin": "https://linkedin.com/in/doni-singh",
        "github": "https://github.com/donisingh7",
        "location": "Jodhpur, India"
    },
    "objective": "Aspiring SDE passionate about AI, DevOps, and scalable systems.",
    "skills": {
        "languages": "Python, JavaScript",
        "frameworks": "React, Firebase",
        "devops": "Docker, GitHub Actions",
        "databases": "MongoDB, MySQL"
    },
    "education": [
        {
            "degree": "M.Tech in Computer Science",
            "institute": "SVNIT Surat",
            "year": "2026",
            "cgpa": "8.00",
            "coursework": "Machine Learning, Distributed Systems"
        },
        {
            "degree": "B.E. in ECE",
            "institute": "MBM University, Jodhpur",
            "year": "2023",
            "cgpa": "8.23",
            "coursework": "Embedded Systems, Control Engineering"
        }
    ],
    "projects": [
        {
            "name": "AI Job Matcher",
            "year": "2024",
            "link": "https://github.com/donisingh7/ai-job-matcher",
            "features": [
                "Built an ML model that recommends jobs based on resume parsing and JD comparison.",
                "Integrated with Streamlit for a user-friendly interface."
            ]
        },
        {
            "name": "Smart Water Monitor",
            "year": "2023",
            "link": "https://github.com/donisingh7/smart-water-monitor",
            "features": [
                "IoT system to track and control water usage using NodeMCU.",
                "Real-time updates pushed to Firebase."
            ]
        }
    ],
    "certifications": [
        "Tableau for Data Analysis - Internshala",
        "Full Stack Web Development - Ducat",
        "AI and ML Advanced - Croma Campus"
    ],
    "last_updated": date.today().strftime("%B %d, %Y")
}

user_data["last_updated"] = date.today().strftime("%B %d, %Y")

# Step 2: Render LaTeX content using correct environment
template = env.get_template('template.tex')
rendered_latex = template.render(user_data)

# Step 3: Save .tex file
with open("resume7.tex", "w", encoding="utf-8") as f:
    f.write(rendered_latex)

# Step 4: Compile to PDF
subprocess.run(["pdflatex", "resume7.tex"])

# Step 5: Clean up
for ext in [".aux", ".log"]:
    try:
        os.remove("resume7" + ext)
    except FileNotFoundError:
        pass
