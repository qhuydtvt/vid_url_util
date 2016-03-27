__author__ = 'qhuydtvt'

import youtube_dl

ydl_opts = {}

ydl = youtube_dl.YoutubeDL(ydl_opts)

info = ydl.extract_info(url="http://mp3.zing.vn/bai-hat/Sau-Tat-Ca-ERIK-ST-319/ZW7O777O.html",
                        download=False)

for key, value in info.items():
    print(key, value)


