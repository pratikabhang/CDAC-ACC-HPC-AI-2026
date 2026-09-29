import threading

class FolderScanner:
    def __init__(self):
        self.files_scanned = 0
        self.lock = threading.RLock()

        self.folder = {
            "files": ["a.txt", "b.txt"],
            "subfolders": {
                "sub1": {
                    "files": ["c.txt", "d.txt"],
                    "subfolders": {
                        "sub2": {
                            "files": ["e.txt"],
                            "subfolders": {}
                        }
                    }
                }
            }
        }

    def scan_directory(self, folder):
        with self.lock:
            for file_name in folder["files"]:
                self.files_scanned += 1
                print("Scanned:", file_name)

            for subfolder in folder["subfolders"].values():
                self.scan_directory(subfolder)


if __name__ == "__main__":
    scanner = FolderScanner()

    thread = threading.Thread(
        target=scanner.scan_directory,
        args=(scanner.folder,)
    )

    thread.start()
    thread.join()

    print("Total files scanned:", scanner.files_scanned)
    assert scanner.files_scanned == 5
    print("Test passed!")
