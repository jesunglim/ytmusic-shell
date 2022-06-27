import os
import webbrowser as web

playlist = {}
playlist = {'BLACKPINK - ‘뚜두뚜두 (DDU-DU DDU-DU)’ M/V' : 
'https://www.youtube.com/watch?v=IHNzOHi8sJs'}
key_list = list(playlist.keys())


print(playlist)

while(1):
    i = input('입력: ')
    os.system("taskkill /im chrome.exe /f")
    if i == '1':
        web.open(playlist[key_list[0]])
        