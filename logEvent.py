from multiprocessing.dummy import Pool
import requests
import urllib

def sendLogMessage(message):
    pool = Pool(1)
    parsedMessage = urllib.parse.quote(message)
    pool.apply_async(requests.get, ['https://api.telegram.org/<ss>/sendMessage?chat_id=67793950&text=' + str(parsedMessage)])
