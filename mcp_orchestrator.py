import os
from generate_docs import generate_summary

def orchestrate():
    print("[MCP] Starting documentation generation process...")
    project_root = os.path.dirname(os.path.abspath(__file__))
    code_dirs = [
        os.path.join(project_root, "src", "python"),
        os.path.join(project_root, "src", "java"),
        os.path.join(project_root, "src", "php"),
    ]
    docs_path = os.path.join(project_root, "docs", "SUMMARY.md")

    generate_summary(code_dirs, docs_path)
    print(f"[MCP] Documentation updated at {docs_path}")

if __name__ == "__main__":
    orchestrate()
