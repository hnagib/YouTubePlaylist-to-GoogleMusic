import youtube_dl
from youScraper import crawl, ydl_opts
import pandas as pd
import os
import datetime

# Playlist `url` & download location
download_dir = '/Users/hasannagib/Music/Workout_2020' 
url_list = crawl('https://www.youtube.com/playlist?list=PLC-5C1DmrxMBaDFBpNVwQmZ53CHSkF8Q2')

# Downloaded new `url`s
try:
    df_old = pd.read_csv(os.path.join(download_dir, 'urls.csv'))
    df_old
except FileNotFoundError:
    df_old = pd.DataFrame({'url':[], 'download_date':[]})
    
df_new = pd.DataFrame(url_list, columns=['url'])
df_new['download_date'] = datetime.datetime.today().strftime('%Y-%m-%d')

download_urls = []
for url in df_new['url']:
    if url not in list(df_old['url']):
        download_urls.append(url)

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(download_urls)

# Save log of urls downloaded
os.popen(f'mv *.mp3 {download_dir}')
df_new.to_csv(os.path.join(download_dir, 'urls.csv'), index=None)