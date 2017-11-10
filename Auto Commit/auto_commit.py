import argparse
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

parser = argparse.ArgumentParser(description='Automatically commit file changes.')
parser.add_argument("-p", "--path", help="Enter folder path.")
#parser.add_argument("-u")
args = parser.parse_args()

path = args.path


class CommitHandler(FileSystemEventHandler):
    def process(self, event):
        print(event.event_type, event.src_path)

    def on_any_event(self, event):
        self.process(event)


if __name__ == '__main__':
    observer = Observer()
    observer.schedule(CommitHandler(), path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
