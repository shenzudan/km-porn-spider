#define km constant
#main endpoint
import json

import yaml
import requests

f = open('config.yml', 'r', encoding='utf-8')
cfg = yaml.load(f.read(), Loader=yaml.FullLoader)

def fetchDirectEndpoint():
    url = cfg['endpoint']
    # allow_redirects= False 这里设置不允许跳转
    response = requests.get(url=url, allow_redirects=False)
    if 300 <= response.status_code < 400:
        end = response.headers['Location']
        cfg['endpoint'] = end
        print('解析到新地址: %s' % end)

fetchDirectEndpoint()

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

