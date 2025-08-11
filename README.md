# Offline Multi-Language Code Documentation Generator

## 📌 Overview
This project is an **offline** multi-language code documentation generator that:
- Monitors a codebase for changes (additions, updates, deletions)
- Processes **multi-language** files (Python, Java, PHP, etc.)
- Uses **Ollama** (local LLM) to generate and update documentation **in real-time**
- Runs entirely **offline** — no API keys, no cloud dependencies

---

## ⚙️ Architecture
1. **File Watcher**: Monitors the codebase for file changes.
2. **Parser & Chunker**: Reads and splits code into manageable chunks.
3. **Ollama LLM**: Generates summaries and documentation for each code chunk.
4. **Markdown Writer**: Saves generated documentation into organized `.md` files.
5. **Real-time Updates**: Only processes files that have been changed since last run.

---

## 📂 Project Structure
project_root/
│── main.py # Entry point, orchestrates the workflow
│── file_watcher.py # Monitors file changes
│── parser.py # Parses code into chunks
│── generate_docs.py # Calls Ollama for doc generation
│── requirements.txt # Python dependencies
│── README.md # Project documentation (this file)
│── docs/ # Generated documentation output




---

## 🚀 How It Works
1. **Start the watcher**:
    ```bash
    python main.py
    ```
2. The script detects any file changes.
3. Changed files are parsed and chunked.
4. Ollama generates/update the documentation.
5. Documentation is saved in `/docs`.

---

## 🛠️ Dependencies
- **Python 3.8+**
- **Ollama** (installed locally)
- `watchdog` (file monitoring)
- `tqdm` (progress bar)

Install Python dependencies:
```bash
pip install -r requirements.txt
```

##  Future Enhancements
Vector DB Integration (Chroma/Milvus) for large-scale projects

Dependency Graph support

Automated Architecture Diagrams

Multi-agent MCP orchestration
