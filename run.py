import urllib
import urllib.request
from bs4 import BeautifulSoup
import time
import requests

def make_soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage,"html.parser")
    return soupdata

def save_to_server(list_data):
    print(list_data)
    params_data = {'id_masjid':list_data[4],
        'kabupaten_kota':list_data[1],
        'kecamatan':list_data[2],
        'nama_masjid':list_data[3],
        'tipologi':list_data[5],
        'alamat':list_data[6],
        'latitude':0,
        'longitude':0,
        'luas_tanah':list_data[7],
        'status_tanah':list_data[8],
        'luas_bangunan':list_data[9],
        'tahun_berdiri':list_data[10],
        'jumlah_jamaah':list_data[11],
        'jumlah_imam':list_data[12],
        'jumlah_khatib':list_data[13],
        'jumlah_muazin':list_data[14],
        'jumlah_remaja':list_data[15],
        'nomor_kontak':list_data[16],
        'source_data':"SIMAS" }
    r = requests.post("https://jibs.my.id/api/masjid/saveMasjid",data=params_data)
    return r.text

for x in range(0,41860,10):
    
    if (x == 0):
        soup = make_soup('http://simas.kemenag.go.id/index.php/profil/masjid/?tipologi_id=7')
    else:
        soup = make_soup('http://simas.kemenag.go.id/index.php/profil/masjid/page/' + str(x) + '?tipologi_id=7')

    for record in soup.findAll('tbody'):
        for data in record.findAll('tr'):
            masjid_data = []
            for data2 in data.findAll('td'):
                masjid_data.append(data2.text)
            print(save_to_server(masjid_data))
    
    