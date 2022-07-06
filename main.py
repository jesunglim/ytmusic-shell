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
    url.append("https://www.youtube.com/watch?v=L5CV53wCWO0")
    url.append("https://www.youtube.com/watch?v=2S24-y0Ij3Y")


    song = 0
    

    while True:
        p = ytplayer().player(url[song])
        p.play()

        print('재생중 [ {} ] 볼륨 : {}' .format(url[song], p.audio_get_volume()))
        cmd = input('command :')

        if cmd == 'p':
            print()

        elif cmd == 'n':
            p.stop()
            del p
            song += 1
            p = ytplayer().player(url[song])
            p.play()

        elif cmd == 'list':
            for i in url:
                print(i)

        elif cmd == 's':
            print(p.get_position())

        # 다음곡 넘어가기
        if p.get_position() >= 0.99:
            p.stop()
            del p
            song += 1
            p = ytplayer().player(url[song])
            p.play()
