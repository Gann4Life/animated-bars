from progress_bar import ProgressBar
from progressbar_builder import ProgressBarBuilder, Templates
import requests, re

def download_file():
    url = "https://cdn-files.gamejolt.net/8lKQpOCmtiq8fXoi-Qrkdw==,1653276368/data/games/4/225/261475/files/61206fa2765ef/thirdym-v0.1.0-alpha.rar"
    with requests.get(url, stream=True) as r:
        disposition = r.headers.get("content-disposition")
        file_name = re.findall("filename=(.+)", disposition)[0]

        total_size = int(r.headers.get("content-length"))
        current_progress = 0

        with open(f"tests/{file_name}", "wb") as f:
            for chunk in r.iter_content(chunk_size=1024):
                current_progress += len(chunk)
                progress = current_progress / total_size
                progressbar.display_progress(progress, f"Downloading {file_name}..." +horizontalbar.make_fill(progress, "{0}"))
                f.write(chunk)

def on_finish():
    print("\nseems like it finished lol")

horizontalbar = Templates.horizontal_bars()[4]
animatedbar = ProgressBarBuilder(Templates.animations()[1])
progressbar = ProgressBar(animatedbar, on_finish=on_finish)

progressbar.start(download_file)