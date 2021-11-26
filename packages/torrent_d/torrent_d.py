import requests
import bs4 as bs


movie_name="deadpool 2"
print(movie_name)

dp_mag="""magnet:?xt=urn:btih:00102086b401f8ce049be55410ff9c69d87bb740&dn=Deadpool%202%20(2018)%20%5bWEBRip%5d%20%5b720p%5d%20%5bYTS.AM%5d&tr=udp%3a%2f%2ftracker.coppersurfer.tk%3a6969%2fannounce&tr=udp%3a%2f%2f9.rarbg.com%3a2710%2fannounce&tr=udp%3a%2f%2fp4p.arenabg.com%3a1337&tr=udp%3a%2f%2ftracker.leechers-paradise.org%3a6969&tr=udp%3a%2f%2ftracker.internetwarriors.net%3a1337&tr=udp%3a%2f%2ftracker.opentrackr.org%3a1337%2fannounce"""


#sudo apt-get install python3-libtorrent

import libtorrent as lt
import time
import datetime

# link = input("Paste your Torrent / Magnet link here")
link = dp_mag

ses = lt.session()
ses.listen_on(6881, 6891)
params = {
    'save_path': '/home/adil/Torrent Download/',
    'storage_mode': lt.storage_mode_t(2)
    # 'paused': False,
    # 'auto_managed': True,
    # 'duplicate_is_error': True
    }

print(link)

handle = lt.add_magnet_uri(ses, link, params)
ses.start_dht()

begin = time.time()
print(datetime.datetime.now())

print ('Downloading Metadata...')
while (not handle.has_metadata()):
    time.sleep(1)
print ('Got Metadata, Starting Torrent Download...')

print("Starting", handle.name())

while (handle.status().state != lt.torrent_status.seeding):
    s = handle.status()
    state_str = ['queued', 'checking', 'downloading metadata', \
            'downloading', 'finished', 'seeding', 'allocating']
    print ('%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s ' % \
            (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, \
            s.num_peers, state_str[s.state]))
    time.sleep(5)

end = time.time()
print(handle.name(), "COMPLETE")

print("Elapsed Time: ",int((end-begin)//60),"min :", int((end-begin)%60), "sec")
print(datetime.datetime.now())  