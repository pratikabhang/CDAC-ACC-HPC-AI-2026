import os
import threading
from vinutils import line
import requests
        
apikey = "aa9e49f"


class PosterDownloader(threading.Thread):
    def __init__(self, **kwargs):
        super().__init__()
        self.url = kwargs.get("url")

    def run(self):
        resp = requests.get(self.url)
        filename = "downloaded_movie_posters/" + self.url.split("/")[-1]
        with open(filename, "wb") as file:
            file.write(resp.content)
            print(f"{filename} saved")


class MoviePosterDownloader(threading.Thread):
    def __init__(self, **kwargs):
        super().__init__()
        self.search_term = kwargs.get("search_term", "spider")
        self.page_count = kwargs.get("page_count", 1)

    # this method is the `target` method of the thread
    # when this thread begins its work, `run()` is called
    def run(self):
        for pc in range(1, self.page_count+1):
            url = f"https://omdbapi.com/?apikey={apikey}&s={self.search_term}&page={pc}"
            resp = requests.get(url)
            movies = resp.json()["Search"]
            for movie in movies:
                if movie["Poster"].startswith("http"):
                    PosterDownloader(url=movie["Poster"]).start()


def main():
    if not os.path.exists("downloaded_movie_posters"):
        os.mkdir("downloaded_movie_posters")
    titles = [
        "iron",
        "spider",
        "super",
        "pirate"
    ]
    all_threads = []

    for title in titles:
        downloader = MoviePosterDownloader(search_term=title, page_count=5)
        all_threads.append(downloader)

    [t.start() for t in all_threads]
    [t.join() for t in all_threads]


if __name__ == "__main__":
    line()
    main()
    line()
