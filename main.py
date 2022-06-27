import os
import webbrowser as web

link = 'https://www.youtube.com/watch?v=ioNng23DkIM'

web.open(link)

i = input('입력: ')
if i == 'y':
    os.system("taskkill /im chrome.exe /f")