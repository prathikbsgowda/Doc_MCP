import os
from transformers import pipeline

# Load summarizer model (small, offline-friendly)
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def read_code(file_path):
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()

def generate_summary(code_dirs, output_file):
    all_summaries = ["# 📄 Codebase Summary\n"]

    for code_dir in code_dirs:
        if not os.path.exists(code_dir):
            continue

        all_summaries.append(f"\n## {os.path.basename(code_dir).capitalize()} Files\n")

        for root, _, files in os.walk(code_dir):
            for file in files:
                if file.endswith((".py", ".java", ".php")):
                    file_path = os.path.join(root, file)
                    code_content = read_code(file_path)

                    # Summarize in chunks to avoid token limit
                    chunk_size = 500
                    chunks = [code_content[i:i+chunk_size] for i in range(0, len(code_content), chunk_size)]
                    summary_parts = []

                    for chunk in chunks[:3]:  # limit for speed
                        try:
                            summary = summarizer(chunk, max_length=60, min_length=20, do_sample=False)
                            summary_parts.append(summary[0]["summary_text"])
                        except Exception as e:
                            summary_parts.append(f"[Error summarizing chunk: {e}]")

                    file_summary = " ".join(summary_parts)
                    all_summaries.append(f"**{file}**:\n{file_summary}\n")

    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(all_summaries))
