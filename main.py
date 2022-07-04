import time
import pafy
import vlc
import asyncio

class ytplayer:
    def player(self, song):
        video = pafy.new(song)
        best = video.getbestaudio() 
        media = vlc.MediaPlayer(best.url)
        return media

    def play(self, media):
        media.play()

if "__main__" == __name__:

    # url of the video 
    url = []
    url.append("https://www.youtube.com/watch?v=dyRsYk0LyA8")
    url.append("https://www.youtube.com/watch?v=2S24-y0Ij3Y")


    song = 0
    p = ytplayer().player(url[song])
    p.play()

    while True:
        cmd = input('command :')
        print("song:", song)
        if cmd == 'n':

            del p
            song += 1
            p = ytplayer().player(url[song])
            p.play()
