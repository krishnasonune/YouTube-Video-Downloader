from pytube import YouTube    #pip install pytube

video_url = input(print(" Enter Youtube video link :  "))
# enter youtube link here


yt = YouTube(video_url)
#pass the value in variable

print(yt.title)
#print the title of the video

print(yt.thumbnail_url)
#print thumbnail of the video


hd_resolution = yt.streams.get_highest_resolution()
#set the resolution to high for better quality



hd_resolution.download()
#downloads the video, it'll download the video in the same project directory

print('video download complete')
#download status of video
