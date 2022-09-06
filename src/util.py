import hashlib
import json
import os

import requests
import tqdm

import AES
# self
import constant as const

# import tqdm

aes = AES.AES_ENCRYPT()


def getCfg():
    return const.cfg


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

    return decrypt(response.text)


def decrypt(hex):
    return json.loads(aes.decrypt(hex))


def download(url: str, fname: str, title: str):
    resp = requests.get(url, stream=True)
    total = int(resp.headers.get('content-length', 1))
    total_unit = '%.2f' % (total / 1024 / 1024)
    desc = 'title: %s\tfile_name: %s' % (title, fname)
    chunk = 1024

    # print('title: %s\t开始下载 %sMb' % (title, total_unit))
    # c = 0
    # with open(fname, 'wb') as file:
    #     for data in resp.iter_content(chunk_size=chunk):
    #         # c = c+1
    #         size = file.write(data)
    #         # if c % 1024 == 0:
    #         #     size_unit = '%.2f' % (size / 1024 / 1024)
    #         #     per = '{:.2%}'.format(size / (total * 1.0)) if total == 0 else '0%'
    #         #     desc = '[%s]title: %s\tfile: %s\tcur: %sMb\ttotal: %sMb' % (per, title, fname, size_unit, total_unit)
    #         #     print(desc)
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
