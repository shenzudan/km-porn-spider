# slef
import constant as const
import util as u


def getAll(page, perPage=10):
    all = u.post(const.URL_VIDEO, {"type": 3, "page": page, "Perpage": perPage})
    return handleRtn(all)


def getHot(page, perPage=10):
    all = u.post(const.URL_VIDEO, {"type": 3, "page": page, "Perpage": perPage})
    return handleRtn(all)


def getDetail(mid):
    all = u.post(const.URL_DETAIL, {"video_id": mid})
    return handleRtn(all)


def handleRtn(data):
    if data['code'] == 200:
        return data['data']
    else:
        print('访问异常[%s]:[%s]' % (data['code'], data['message']))
        return []
