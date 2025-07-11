# 🧠 AI-based Feature Design Workflow (create-prd → generate-tasks)

This project uses an AI-assisted workflow to plan and prepare feature development using `.mdc` rules and natural language prompts.

It supports both frontend and backend features, regardless of language or stack (React, Python, Rust, Elixir, etc.).

---

## 🧩 1. Start with the PRD (Product Requirements Document)

📄 **File:** `create-prd.mdc`  
🎯 **Goal:** Define what the feature is, who it's for, and why it matters.

### ✅ Steps:

1. Prompt the AI:
   ```
   I want to build a fullstack ToDo list app using Python and React. Please generate a PRD.
   ```

2. AI asks clarifying questions to understand the feature's goals, scope, and requirements.

3. You answer the questions in plain English.

4. AI generates a comprehensive PRD including:
   - Overview, goals, and user stories
   - Functional requirements (using MoSCoW)
   - Non-goals, success metrics, and risk assessment
   - High-level technical and design context

5. File is saved as:
   ```
   docs/prd-[feature-name].md
   ```

---

## ✅ 2. Generate the Task List for Development

📄 **File:** `generate-tasks_py.mdc`  
🎯 **Goal:** Break the PRD into a detailed, checkable task list following **outside-in TDD**.

### ✅ Steps:

1. Prompt the AI:
   ```
   Generate a task list based on docs/prd-todo-list.md
   ```

2. The AI will:
   - Analyze the PRD
   - Generate high-level **parent tasks**
   - Wait for your confirmation

3. You reply:
   ```
   Go
   ```

4. The AI will then:
   - Generate granular **sub-tasks** for each parent task, following an outside-in, test-first approach.
   - Create a `Relevant Files` section, listing test files **before** implementation files.
   - Include commands and verification steps for developers.

5. File is saved as:
   ```
   docs/tasks/tasks-[prd-file-name].md
   ```

---

## 🧑‍💻 3. Start Coding

You now have:
- ✅ **PRD** — what & why
- ✅ **Task list** — a step-by-step, test-driven implementation plan

Assign tasks, implement features, track progress — repeat for each new feature.

---

## ✨ Example Prompt (copy/paste)

```
Create a PRD for a ToDo list app using React frontend and FastAPI backend. Later, we'll containerize with Docker and use PostgreSQL.
```

---

## 🔁 Iteration Loop

- Add a new feature idea? → Start again from `create-prd.mdc`
- Changed a requirement? → Update PRD, regenerate the task list
- Need to onboard someone? → Share the PRD + Task List

---

## 🛠 Recommended Tech Stack for ToDo App Example

- **Frontend:** React + Vite
- **Backend:** FastAPI (Python)
- **Database:** PostgreSQL
- **Testing:** React Testing Library, Pytest
- **DevOps:** Docker + docker-compose

---