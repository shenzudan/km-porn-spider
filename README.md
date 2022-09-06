# km-porn-spider
[中文文档](README_zh.md)

#### Description
##### Crawler for 快猫短视频
##### If the endpoint cannot access, just change it in  `config.yml` 


#### Environment 
- python3+
- mysql5.6+ (optional)

#### Install dependencies
* python dependencies
```shell
pip install requests
#mac使用(win如果出现问题也用这个试试): pip install pycryptodome
pip install pycrypto
#保存到数据库
pip install pymysql
#下载依赖
pip install tqdm
pip install pyyaml

```
* db scripts(if you don't want to store these videos to mysql, configure save property in `config.yml`)
```sql
CREATE TABLE `videos` (
 `id` bigint(20) NOT NULL,
 `img_url` varchar(100) CHARACTER SET utf8 NOT NULL,
 `play_url` varchar(100) CHARACTER SET utf8 NOT NULL,
 `like` int(11) DEFAULT NULL,
 `title` varchar(100) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
 `height` int(11) DEFAULT NULL,
 `width` int(11) DEFAULT NULL,
 `create_time` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
 PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
```

#### Run 
* import sql scripts
* configure database in `config.yml`
* pip install -r requirements.txt
* start crawl
```shell
#crawl hot videos
python main.py 
#crawl all videos
python main.py 1
```

#### Configuration
- `endpoint`  define the kuaimao endpoint
- `save`      define whether to store videos
- `pool_size` define thread num to fetch videos
- `db`        define configuration to connect with database
- `download`  define whether download video (thread pool size will be set to 1 when is True)

#### Generate `requirements.txt`
- install 
```
    pip install pipreqs 
```

- gen 
```
    pipreqs . --encoding=utf8 --force
```

#### Contribution

1.  just push
