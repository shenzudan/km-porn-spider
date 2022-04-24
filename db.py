import pymysql

import util


def getConn():
    cfg = util.getCfg()
    db = pymysql.connect(host=cfg['db']['host'], user=cfg['db']['user'],
                         port=cfg['db']['port'], password=cfg['db']['pass'],
                         db=cfg['db']['database'])
    return db


def insert(db, data):
    cur = db.cursor()
    sql = 'insert into videos(id, img_url, play_url, `like`, title, height, width)' \
          'VALUES({},\"{}\",\"{}\",{},\"{}\",{},{}) ON DUPLICATE KEY UPDATE play_url="{}"' \
        .format(data['mv_id'], data['mv_img_url'], data['mv_play_url'],
                data['mv_like'], data['mv_title'],
                data['mv_play_height'], data['mv_play_width'],
                data['mv_play_url'])
    print('exec->', sql)
    try:
        cur.execute(sql)
    except Exception as e:
        print("\033[0;31;40m", 'SAVE exception', e, "\033[0m")
    finally:
        db.commit()
