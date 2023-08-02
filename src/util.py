import hashlib
import json
import os

import requests
import tqdm
from urllib.parse import urlparse
import AES
# self
import constant as const

# import tqdm

aes = AES.AES_ENCRYPT()


def getCfg():
    return const.cfg


def getParam(d):
    # 签名计算
    sorted_d = dict(sorted(d.items(), key=lambda item: item[0]))
    sorted_d_str = "&".join(f"{k}={v}" for k, v in sorted_d.items())
    sig = md5('%s%s' % (sorted_d_str, const.SIG_KEY)).upper()
    d['signature'] = sig
    # 参数加密
    data = aes.encrypt(json.dumps(d))
    # print(d)
    return 'data=%s&device_version=h5&device_type=iPhone&version_code=1.0&device=h5&api_token=&c_name=developer-default' % (data)


def md5(text):
    md = hashlib.md5()  # 获取一个md5加密算法对象
    md.update(text.encode('utf-8'))  # 制定需要加密的字符串

    return md.hexdigest().upper()


def post(url, data):
    # 获取域名
    fd = getParam(data)
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        # 'authority': urlparse(url).netloc
    }
    print(url)
    print(headers)
    print(fd)
    response = requests.request("POST", url, headers=headers, data=fd)

    return decrypt(response.text)


def decrypt(hex):
    return json.loads(aes.decrypt(hex))


def download(url: str, fname: str, title: str):
    resp = requests.get(url, stream=True)
    total = int(resp.headers.get('content-length', 1))
    total_unit = '%.2f' % (total / 1024 / 1024)
    desc = 'title: %s\tfile_name: %s' % (title, fname)
    chunk = 1024
    with open(fname, 'wb') as file, tqdm.tqdm(desc=desc,
                                              total=total,
                                              unit='iB',
                                              unit_scale=True,
                                              unit_divisor=1024) as bar:
        for data in resp.iter_content(chunk_size=chunk):
            size = file.write(data)
            bar.update(size)

    print('title: %s\t下载完成 %sMb' % (title, total_unit))



def createDirIfNotExist(path: str):
    if not os.path.exists(path):
        os.mkdir(path)


print(decrypt("7041539E779DC1545FD4A04E22A25DB410A96BC46FDCF0E9AE00D93CD0D72CD8562D5F5489180341DA21481E4E51E45C0BCB1F0D611248BD65641D8F71D973B492548EA541E598D11791F60569FC1A52"))
