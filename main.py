from os import listdir
from os.path import isfile, join
import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from pathlib import Path

listOfDirectories = {
    "Pictures": [".jpeg", "jpg", ".gif", ".png", ".svg", ".ico"],
    "Videos": [".wmv", ".mov", ".mp4", ".mpg", ".mpeg", ".mkv"],
    "Zip": [".iso", ".tar", ".gz", ".rz", ".7z", ".dmg", ".rar", ".zip"],
    "Audio": [".mp3", ".msv", ".wav", ".wma"],
    "Documents": [".doc", ".docx", ".odt", ".pdf", ".rtf", ".tex", ".txt", ".wpd", ".ppt", ".pptx", ".pps"],
    "Programming": [".c", ".class", ".cpp", ".cs", ".h", ".java", ".php", ".py", ".sh", "swift", ".vb", ".js", ".htm", ".html", ".rss", ".xhtml", ".css"],
}

# File_Format_Dictionary = {
#     final_file_format: directory
#     for directory, file_format_stored in listOfDirectories.items()
#     for final_file_format in file_format_stored
# }


def on_created(event):
    print(f"hey, {event.src_path} has been created!")

if __name__ == "__main__":
    patterns = "*"
    ignore_patterns = ""
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

    my_event_handler.on_created = on_created
    path = "C:\\Users\\Youri\\Documents\\test"
    go_recursively = True
    my_observer = Observer()
    my_observer.schedule(my_event_handler, path, recursive=go_recursively)

    my_observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        my_observer.stop()
        my_observer.join()
    