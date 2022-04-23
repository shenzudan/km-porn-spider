#define km constant
#main endpoint
import yaml
f = open('config.yml', 'r', encoding='utf-8')
cfg = yaml.load(f.read(), Loader=yaml.FullLoader)

ENDPOINT = cfg['endpoint'] + "{0}"
URL_ALL = "/api/videos/listAll"
URL_HOT = "/api/videos/listHot"
URL_DETAIL = "/api/videos/detail"

SIG_KEY = "maomi_pass_xyz"
AES_KEY = b"625202f9149maomi"
AES_IV  = b"5efd3f6060emaomi"



def getAllUrl():
    return ENDPOINT.format(URL_ALL)

def getHotUrl():
    return ENDPOINT.format(URL_HOT)

def getDetailUrl():
    return ENDPOINT.format(URL_DETAIL)

