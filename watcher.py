import os
from protocss import ProtoCSS
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time


if __name__ == '__main__':
    path = "./static"
    converter = ProtoCSS()
    event_handler = converter.FileChangeHandler(converter)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        while True:
            # os.system('cls') if os.name == 'nt' else os.system('clear')
            time.sleep(1)

    except KeyboardInterrupt:
        observer.stop()
    observer.join()