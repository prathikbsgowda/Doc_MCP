from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import time
import os

WATCH_PATH = "./codebase"

class ChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            print(f"[MODIFIED] {event.src_path}")
            subprocess.run(["python", "mcp_orchestrator.py", event.src_path])

    def on_created(self, event):
        if not event.is_directory:
            print(f"[CREATED] {event.src_path}")
            subprocess.run(["python", "mcp_orchestrator.py", event.src_path])

    def on_deleted(self, event):
        if not event.is_directory:
            print(f"[DELETED] {event.src_path}")
            subprocess.run(["python", "mcp_orchestrator.py", event.src_path])

if __name__ == "__main__":
    os.makedirs("docs", exist_ok=True)

    event_handler = ChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, WATCH_PATH, recursive=True)
    observer.start()
    print(f"📡 Watching '{WATCH_PATH}' for changes...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
