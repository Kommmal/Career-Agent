from agents import function_tool


@function_tool
def get_career_roadmap(field: str) -> list[str]:
    roadmaps = {
        "data science": ["Learn Python", "Pandas", "Statistics", "Machine Learning", "Deep Learning"],
        "web development": ["HTML", "CSS", "JavaScript", "React", "Node.js", "MongoDB"],
        "cybersecurity": ["Networking Basics", "Linux", "Cryptography", "Penetration Testing", "Ethical Hacking"],
        "ui ux design": ["Design Principles", "Wireframing", "Figma", "User Research", "Prototyping", "Design Systems"],
        "mobile development": ["Java/Kotlin (Android)", "Swift (iOS)", "Flutter/Dart", "Firebase", "App Deployment"],
        "cloud computing": ["AWS/GCP Basics", "EC2 & S3", "Docker", "Kubernetes", "DevOps Practices"],
        "game development": ["C#", "Unity Engine", "Game Physics", "Animation", "Level Design"],
        "ai ml engineering": ["Python", "Numpy & Pandas", "Scikit-learn", "TensorFlow/PyTorch", "Model Deployment"],
    }
    return roadmaps.get(field.lower(), ["No roadmap found"])


@function_tool
def suggest_jobs(field: str) -> list[str]:
    jobs = {
        "data science": ["Data Analyst", "Machine Learning Engineer", "Data Scientist"],
        "web development": ["Frontend Developer", "Backend Developer", "Full Stack Developer"],
        "cybersecurity": ["Security Analyst", "Penetration Tester", "Cybersecurity Engineer"],
        "ui ux design": ["UI Designer", "UX Researcher", "Product Designer"],
        "mobile development": ["Android Developer", "iOS Developer", "Flutter Developer"],
        "cloud computing": ["Cloud Engineer", "DevOps Engineer", "Site Reliability Engineer"],
        "game development": ["Game Developer", "Unity Developer", "Game Designer"],
        "ai ml engineering": ["AI Engineer", "ML Engineer", "Deep Learning Specialist"],
    }
    return jobs.get(field.lower(), ["No jobs found"])
