# km-porn-spider

#### Description
##### Crawler for 快猫短视频
##### If the endpoint cannot access, just change it in  `constant.py` 


#### Environment 
- python3+
- mysql5.6+

#### Install dependencies
* python dependencies
```shell
pip install requests
#for mac use: pip install pycryptodome
pip install pycrypto
#save videos to db
pip install pymysql
pip install pyyaml
```
* db scripts
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
* start crawl
```shell
#crawl hot videos
python main.py 
#crawl all videos
python main.py 1
```

#### Contribution

1.  just push
