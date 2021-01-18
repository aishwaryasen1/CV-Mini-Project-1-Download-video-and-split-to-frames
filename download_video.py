import pytube
yt = pytube.YouTube("https://www.youtube.com/watch?v=AyHX7GsrMlo")
print(yt.title)
stream=yt.streams.first()
stream.download()