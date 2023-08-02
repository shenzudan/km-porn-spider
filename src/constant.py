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

# fetchDirectEndpoint()

ENDPOINT = cfg['endpoint'] + "{0}"
URL_VIDEO = ENDPOINT.format("/api/video/index")
URL_DETAIL = ENDPOINT.format("/api/video/info")

SIG_KEY = 'ohI}-bFpD*z8)W7~REusVa]U`YKQ=[C1&XZ."n5:dl<{?@J6NkO+f%c^"$tevxB>j2M_9;G#y3Tw|gL/HS,Pqr0!Ami(49Y_.~Tan#z{5ZLO,_E(7!vJ^HC5_{Xq5$z*'
AES_KEY = b"x;j/6olSp})&{ZJD"
AES_IV  = b"znbV%$JN5olCpt<c"

