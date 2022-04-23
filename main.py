import db
import km

# 测试接口方法是否有效
import util

def test():
    data = km.getAll(1, 1)
    print(data)
    data = km.getHot(1, 1)
    print(data)
    data = km.getDetail(2941995)
    print(data)


# save in db
def save(conn, video):
    print(video['mv_id'], video['mv_title'], video['mv_img_url'], video['mv_play_url'])
    if conn:
        db.insert(conn, video)


def run(mode=0):
    page = 1
    idSet = set()  # 视频id集合
    lastLen = 0  # 上次循环结束的视频个数
    conn = None
    if cfg['save']:
        conn = db.getConn()
        print('初始化sql连接完毕..')

    while True:
        if mode == 0:
            data = km.getHot(page, 20)
        else:
            data = km.getAll(page, 20)

        # 开始处理数据
        if 'list' in data:
            list = data['list']
            print('当前采集%s页，共有%s个视频' % (page, len(list)))
            for video in list:
                if 'mv_id' in video:
                    id = video['mv_id']
                    idSet.add(id)
                    save(conn, video)
                else:
                    print('疑似广告', video)
        # 结束当前页记录

        # 退出采集条件
        curLen = len(idSet)
        # print(curLen, lastLen)
        if curLen <= lastLen:
            return page, curLen
        # 继续采集
        lastLen = curLen
        page += 1


if __name__ == '__main__':
    cfg = util.getCfg()
    page, curLen = run()
    print('本次共采集%s个视频, 共%s页' % (page, curLen))
