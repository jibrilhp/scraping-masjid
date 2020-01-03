from multiprocessing.dummy import Pool
import requests
import urllib

def sendLogMessage(message):
    pool = Pool(1)
    parsedMessage = urllib.parse.quote(message)
    pool.apply_async(requests.get, ['https://api.telegram.org/bot1049146609:AAF986C7CUE4fZTKy8FYKSylzKyEFakVBLg/sendMessage?chat_id=67793950&text=' + str(parsedMessage)])
