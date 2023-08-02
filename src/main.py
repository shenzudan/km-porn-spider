import db
import km
import sys
from TaskQueue import ThreadPool
import threading

# 测试接口方法是否有效
import util


def test():
    # data = util.decrypt('A8F1D656E68A75031DF8A255B0096B48DDD3AD12D43CBDD851C8D3677602E8953738C02B6A1D2D4B0978A9D84CE1ED2C1F036BC3CCB7138C070A61950010F4327DABB23CB296FD229661849935FEA6D64B598B4C98B44D1018B8A5EEEF3F958A16B99A66EE25BDDC6F452488F93D44E6458FB14EA48353E10F1B4AF73F8C8393EEDCF2C4D7EDFC69D414F60A01F7665AF7A702931B460EC63B1318DDE18EFDB3EBA710B84CD98CDDF041F7050C78299ACBA87129735AC0FA229933974C271DFB085CB0B9CF4920FD1DE031F30FBCC9E0E6F4D72D0EFF142F752C3F13AC898B8DBCEA74D4A7EEAD8EF3D7481E0675E72CE79A50E5681B3A4EB6B9ED63113978B7F789DE937397DBBD59988C9870F9E99DFCC776E26FFE21CC194165465C63B9E55246D9ECBDF6E24591C59592962083FAE67CE87AEE83FD99D6D3CAECA590ADB1B276058FD91A71E4BE6DE9729BE079EF03A285699BB94EB29E882DE1AD6860EBAD0F79BE6CD719DA9197C81E12B476243DD1C69CA954D97F5FC616625D041B85C4137F9D9453EF7B0AD490E75B6F21A993121210C9D910B991F2F3CCE6F8E6B8B86607A601B5AAFF96691FA6612DD61FE1D1A565C89FB8296EF2FF2D88DF9E5BB2ED9723D6C98453AC030F14F4B6BDCA6F64E49E6AF5CDB7A59389276CC9DDD79C980F4FF2327AB3801415C066150E79108BEBBFB75CCE511AE740C17A1C9D2FE98145BA0B1154D96D38F5719160A076AE223ED2414BB6D5A603D6455D8FF2DD1E0FF3434FF23AD458271F830602A669960FCBE6212AB9F1A6843F289F910D60DB0D3BEDFC36B161F2DA9D5ED7F30FE3542201A1882FF0112A5BFEA16DA3C0CAFFB6878DE6F3F7E510462425261994134E82637CC3E5D5673FAE33CBA8FEA1C3E09C42C680ABF0CA874AA62AF477172C23E2DD664A18220C983BA9459E18B730D6B8AC788BB19C22825B87715D5C28D94DD6ACE7FBAF8AFE6FC3465C12731CC4788503E6734F5B78D85339E980874BECE341FD0E06FF3D5AEDB9BD95688B802C9E3F06C2D75B25C48EE36260B24B9E654288D2CA58DED3DA05D8401A243AC51BDCE067622F7771051E12261030D1E39D2A30DE06AA9C53D74F08DE6D7FD0F70604ABAFD4A503EB72A2A7662A1C861433E9DDCCC231B291C22AE9F2A3957F0BDA6C6D58C38B9EFCE7EF550ABA1BC3D249CA536153E30F3A145243BB81488DB420C0EA5C55F9176FA35B16922055E937CB7461A5606B1B05DE2767857CED5A0EA99233C3EB6BC9BE7AAF4E560CAB9E489AEF4F529EF3472A3D54326ACB8F8D8C8BD0EF45BAA9B08D39B4BAEEA5B0F320631F5D1B919A221A2E8AC716A50CCD1D2D86875D031719FFE30EE57068AECF1E68636E6EAC69AC640B488843E872B26C722DAFF1929E6AC9E8713989BFA021DA296B2346C1A450B0AB3DE65EEBF2D6645466510CD4746401582326FFEA94B8FF67DC56A6261974B8D12AD2D261FA1F547C')
    # print(data)
    # data = km.getAll(1, 1)
    # print(data)
    # data = km.getHot(1, 10)
    # print(data)
    data = km.getDetail(1463657)
    print(data)
    # print(video)
    if 'video_info' not in data:
        return

    video = data['video_info']
    print("test:", video['title'], video['nickname'], video['normal_url'], video['cover'])
    fname = 'downloads/test.ts'
    util.download_m3u8_video(video['m3u8_url'], fname)


# fetch detail and save in db
def work(t_name, mid, thread_local):
    print('[%s]:获取mv[%s]' % (t_name, mid))
    video = km.getDetail(mid)
    # print(video)
    if 'video_info' not in video:
        return

    video = video['video_info']
    print("[%s]:" % t_name, video['id'], video['title'], video['nickname'], video['normal_url'], video['cover'])
    if cfg['download']:
        fname = 'downloads/%s.mp4' % mid
        util.download_m3u8_video(video['m3u8_url'], fname)
        # util.download(video['normal_url'], fname, video['title'])

    # don't save
    if thread_local is None:
        return

    if hasattr(thread_local, 'conn'):
        _conn = thread_local.conn
    else:
        print('[%s]:创建新sql链接' % t_name)
        _conn = db.getConn()
        thread_local.conn = _conn

    db.insert(_conn, video)

def run(mode=0):
    page = 1
    idSet = set()  # 视频id集合
    lastLen = 0  # 上次循环结束的视频个数
    thread_local = threading.local()
    if cfg['save']:
        conn = db.getConn()
        thread_local.conn = conn
        print('初始化sql连接完毕..')
    else:
        thread_local = None

    pool = ThreadPool(cfg['pool_size'])
    print('线程池最大线程数: %s' % pool.max_num)
    while True:
        if mode == 0:
            data = km.getHot(page, 10)
        else:
            data = km.getAll(page, 10)

        # 开始处理数据
        if 'video_list' in data:
            list = data['video_list']
            print('当前采集%s页，共有%s个视频，已采集%s个视频' % (page, len(list), len(idSet)))
            for video in list:
                if 'base64_txt' in video and 'id' in video:
                    mid = video['id']
                    idSet.add(mid)
                    pool.put(func=work, args=(mid, thread_local))

                else:
                    print('疑似广告', video)

        # 结束当前页记录

        # 退出采集条件
        curLen = len(idSet)
        # print(curLen, lastLen)
        if curLen <= lastLen:
            print('准备退出，等待线程池工作完成...')
            pool.close()
            return page, curLen
        # 继续采集
        lastLen = curLen
        page += 1


if __name__ == '__main__':
    model = 3
    if len(sys.argv) > 1:
        model = sys.argv[1]

    if model == 3:
        test()
        exit(0)

    cfg = util.getCfg()
    if cfg['download']:
        cfg['pool_size'] = 1
        print('开启下载，线程池数量改为1')
        util.createDirIfNotExist('downloads')

    page, curLen = run(model)
    print('本次共采集%s个视频, 共%s页' % (curLen, page))
