#slef
import constant as const
import util as u


def getAll(page, perPage=15):
    all = u.post(const.getAllUrl(), {"page": page, "perPage": perPage})
    return handleRtn(all)


def getHot(page, perPage=15):
    all = u.post(const.getHotUrl(), {"page": page, "perPage": perPage})
    return handleRtn(all)


def getDetail(mid):
    all = u.post(const.getDetailUrl(), {"uId": 1, "mvId": mid, 'type': 1})
    return handleRtn(all)


def handleRtn(data):
    if data['code'] == 0:
        return data['data']
    else:
        print('访问异常[%s]:[%s]' % (data['code'], data['message']))
        return []
