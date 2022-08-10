#define km constant
import yaml
import requests

#config file path
cfg_name = 'config.yml'

f = open(cfg_name, 'r', encoding='utf-8')
cfg = yaml.load(f.read(), Loader=yaml.FullLoader)

def fetchDirectEndpoint():
    url = cfg['endpoint']
    # allow_redirects= False 这里设置不允许跳转
    response = requests.get(url=url, allow_redirects=False)
    if 300 <= response.status_code < 400:
        end = response.headers['Location']
        cfg['endpoint'] = end
        print('解析到新地址: %s' % end)
        # record new address
        # with open('output.yaml', 'w') as fp:
        #     yaml.dump(cfg, fp)

fetchDirectEndpoint()

ENDPOINT = cfg['endpoint'] + "{0}"
URL_ALL = ENDPOINT.format("/api/videos/listAll")
URL_HOT = ENDPOINT.format("/api/videos/listHot")
URL_DETAIL = ENDPOINT.format("/api/videos/detail")

SIG_KEY = "maomi_pass_xyz"
AES_KEY = b"625202f9149maomi"
AES_IV  = b"5efd3f6060emaomi"

