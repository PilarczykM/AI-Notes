# n8n Workflow Automations

This repository contains a collection of automated workflows built using [n8n](https://n8n.io/), an extendable workflow automation tool for developers. These workflows can integrate APIs, services, and logic-based tasks to streamline business processes.

---

## 📌 About n8n

**n8n** (pronounced *"n-eight-n"*) is a fair-code licensed, extendable workflow automation tool that enables you to connect various services using simple visual workflows. You can self-host n8n or run it via Docker, npm, or in the cloud.

---

## 🚀 Getting Started

You can run n8n locally using either **npm** or **Docker**. Choose your preferred method below.

---

### Option 1: Run via npm

#### Requirements:

- [Node.js](https://nodejs.org/) (v18 or higher)
- [npm](https://www.npmjs.com/) (v9 or higher, bundled with Node.js)

#### Steps:

1. Install n8n globally:

   ```bash
   npm install n8n -g
   ```

3. Start n8n:

   ```bash
   n8n
   ```

4. Open your browser and go to `http://localhost:5678` to access the n8n editor and create or import my workflow

---

### Option 2: Run via Docker

#### Requirements:

- [Docker](https://docs.docker.com/get-docker/) installed on your system.

#### Steps:

1. Run the n8n container:

   ```bash
   docker volume create n8n_data

   docker run -it --rm --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n docker.n8n.io/n8nio/n8n
   ```

3. Open your browser and visit `http://localhost:5678`. To access the n8n editor and create or import my workflow.

---

## 📖 Documentation

- [n8n Documentation](https://docs.n8n.io/)
- [n8n CLI](https://docs.n8n.io/hosting/installation/local/cli/)
- [Docker Hub: n8n](https://hub.docker.com/r/n8nio/n8n)

---

## 💠 Troubleshooting

- Make sure your ports (especially 5678) are not in use.
- Use `--tunnel` when running via npm to access via a public URL:
  ```bash
  n8n start --tunnel
  ```

---

## 📟 License

This repository is released under the MIT License. n8n itself is [source-available](https://docs.n8n.io/reference/license/) under the Fair-code license.

---

## 🙌 Contributions

Feel free to fork, improve, or suggest new workflows via pull requests.
