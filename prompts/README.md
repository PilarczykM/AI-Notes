# 🧠 AI-based Feature Design Workflow (create-prd → create-tdd → generate-tasks)

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

2. AI asks clarifying questions (e.g. user goals, edge cases, success metrics).

3. You answer the questions in plain English.

4. AI generates a full PRD including:
   - Overview, goals
   - Functional requirements
   - User stories, edge cases
   - Non-goals and success metrics

5. File is saved as:
   ```
   docs/prd-todo-list.md
   ```

---

## 🛠 2. Generate the TDD (Technical Design Document)

📄 **File:** `create-tdd.mdc`  
🎯 **Goal:** Define the technical architecture and how the feature will be built.

### ✅ Steps:

1. Prompt the AI:
   ```
   Please generate a TDD based on docs/prd-todo-list.md
   ```

2. AI may ask questions about the tech stack:
   - Which framework? (e.g., FastAPI, PostgreSQL, React)
   - API routes, DB models, deployment style?

3. You answer those questions.

4. AI generates a TDD with:
   - Architecture
   - Component/modules
   - Data models
   - Testing and deployment notes

5. File is saved as:
   ```
   docs/tdd-prd-todo-list.md
   ```

---

## ✅ 3. Generate the Task List for Development

📄 **File:** `generate-tasks.mdc`  
🎯 **Goal:** Break PRD + TDD into clear, checkable dev tasks.

### ✅ Steps:

1. Prompt the AI:
   ```
   Generate a task list based on docs/prd-todo-list.md and docs/tdd-prd-todo-list.md
   ```

2. The AI will:
   - Analyze PRD and TDD
   - Generate high-level **parent tasks**
   - Wait for your confirmation

3. You reply:
   ```
   Go
   ```

4. The AI will then:
   - Generate **sub-tasks** per parent task
   - Create a `Relevant Files` section (e.g., `.py`, `.ex`, `.ts`, `.rs`)
   - Add commands/tests needed for devs

5. File is saved as:
   ```
   tasks/tasks-prd-todo-list.md
   ```

---

## 🧑‍💻 4. Start Coding

You now have:
- ✅ PRD — what & why
- ✅ TDD — how
- ✅ Task list — what to do

Assign tasks, implement features, track progress — repeat for each new feature.

---

## ✨ Example Prompt (copy/paste)

```
Create a PRD for a ToDo list app using React frontend and FastAPI backend. Later, we'll containerize with Docker and use PostgreSQL.
```

---

## 🔁 Iteration Loop

- Add a new feature idea? → Start again from `create-prd.mdc`
- Changed a requirement? → Update PRD, regenerate TDD & tasks
- Need to onboard someone? → Share PRD + TDD + Task List

---

## 🛠 Recommended Tech Stack for ToDo App Example

- **Frontend:** React + Vite
- **Backend:** FastAPI (Python)
- **Database:** PostgreSQL
- **Testing:** React Testing Library, Pytest
- **DevOps:** Docker + docker-compose

---
