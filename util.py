import hashlib
import requests
import json
#self
import constant as const
import AES


aes = AES.AES_ENCRYPT()


def getParam(json):
    data = aes.encrypt(json)
    sig = md5('data=%s%s' % (data, const.SIG_KEY))
    return 'data=%s&sig=%s' % (data, sig)


def md5(text):
    md = hashlib.md5()  # 获取一个md5加密算法对象
    md.update(text.encode('utf-8'))  # 制定需要加密的字符串
    return md.hexdigest()


def post(url, data):
    fd = getParam(json.dumps(data))
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        # 'Cookie': 'ci_session=laed9v2sk8992mctica6sdn8cq69r9o6'
    }
    response = requests.request("POST", url, headers=headers, data=fd)

    return json.loads(aes.decrypt(response.text))
