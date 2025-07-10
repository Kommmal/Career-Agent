# 🎓 Career Mentor Agent

The **Career Mentor Agent** is a multi-agent AI-powered assistant that helps users explore and plan career paths based on their interests. It uses a combination of intelligent agents and functional tools to suggest relevant career fields, required skills, and potential job roles.

---

## 🚀 Features

- 🔍 Understands user interests
- 🧭 Suggests relevant career paths (e.g., Web Development, Data Science)
- 🛠️ Provides a skill roadmap using integrated tools
- 💼 Recommends job roles based on the chosen field
- ⚙️ Built using OpenAI Agent SDK + Gemini API

---

## 🧠 Agent Flow Overview

### 🔹 1. Career Agent
- **Purpose**: Determines the best-fit career based on the user’s input.
- **Instructions**: Ask about the user's interest and return a one- or two-word career field name (e.g., "web development").
- **Tools**: None

### 🔹 2. Skill Agent
- **Purpose**: Shares a skill roadmap using the `get_career_roadmap` tool.
- **Instructions**: Return a comma-separated list of skills, starting with the word "Learn".
- **Tools**: `get_career_roadmap(field: str) -> list[str]`

### 🔹 3. Job Agent
- **Purpose**: Suggests relevant job titles using the `suggest_jobs` tool.
- **Instructions**: For each job, prefix it with "You can become a...".
- **Tools**: `suggest_jobs(field: str) -> list[str]`

---

## 🔧 Tools Used

### ✅ `get_career_roadmap(field: str)`
Returns a list of essential skills for a given career field.

**Example:**
```python
["HTML", "CSS", "JavaScript", "React", "Node.js"]
