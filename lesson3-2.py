from pytube import YouTube
def showProgress(stream, chunk, bytes_remaining):
    size = stream.filesize
    currentProgress = (size - bytes_remaining) * 100 / size
    print("Progress remaining" + str(surrentProgress) + %)
yt = Youtube("https://www.youtube.com/watch?v=sGOchSK6VNo",on_progress_callback = showProgress)
stream = yt.streams.filter(only_audio = True).first()
stream.download()