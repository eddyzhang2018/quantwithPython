# Credit: https://twitter.com/akshay_pachaar/status/1640332084026966016

# if required to install pytube package

# pip install pytube

import pytube

download_loc = './'

video_url = input('Enter url:')

video_instance = pytube.YouTube(video_url)

stream = video_instance.streams.get_highest_resolution()

stream.download()
