"""
需要安装
pip install watchdog
"""
import time

from watchdog.events import *
from watchdog.observers import Observer
from rapidocr_onnxruntime import RapidOCR


class FileEventHandler(FileSystemEventHandler):
    def __init__(self):
        """
        __init__ 的功能说明（请补充）。

        """
        FileSystemEventHandler.__init__(self)

    def on_moved(self, event):
        """
        on_moved 的功能说明（请补充）。

        Args:
            event: 参数说明。

        """
        if event.is_directory:
            print("directory moved from {0} to {1}".format(event.src_path, event.dest_path))
        else:
            print("file moved from {0} to {1}".format(event.src_path, event.dest_path))

    def on_created(self, event):
        """
        on_created 的功能说明（请补充）。

        Args:
            event: 参数说明。

        """
        if event.is_directory:
            print("directory created:{0}".format(event.src_path))
        else:
            print("file created:{0}".format(event.src_path))

    def on_deleted(self, event):
        """
        on_deleted 的功能说明（请补充）。

        Args:
            event: 参数说明。

        """
        if event.is_directory:
            print("directory deleted:{0}".format(event.src_path))
        else:
            print("file deleted:{0}".format(event.src_path))

    def on_modified(self, event):
        """
        on_modified 的功能说明（请补充）。

        Args:
            event: 参数说明。

        """
        if event.is_directory:
            print("directory modified:{0}".format(event.src_path))
        else:
            print("file modified:{0}".format(event.src_path))


if __name__ == "__main__":
    observer = Observer()
    event_handler = FileEventHandler()
    observer.schedule(event_handler, "C:/test", True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

