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
    sql = 'insert into videos(id, img_url, play_url, like, title, height, width, create_time)' \
          'VALUES({},{},{},{},{},{},{},{})' \
        .format(data['mv_id'], data['mv_img_url'], data['mv_play_url'], data['mv_like'], data['mv_play_height'],
                data['mv_play_width'], 'now()')
    cur.execute(sql)
    db.commit()
