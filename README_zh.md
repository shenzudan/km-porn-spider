# km-porn-spider
[English](README.md)

#### 描述
##### 快猫短视频爬虫
##### 如果快猫地址有更新，请在配置文件`config.yml`中重新设置

#### 环境 
- python3+
- mysql5.6+ (可选)

#### 安装依赖
* python dependencies
```shell
pip install requests
#for mac use: pip install pycryptodome
pip install pycrypto
#save videos to db
pip install pymysql
pip install pyyaml
#downloads
pip install tqdm
```
* 数据库脚本(如果你不需要保存视频信息到数据库可以不用执行, 在`config.yml`可设置保存属性)
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

#### 运行 
* 导入sql脚本
* 配置数据库 `config.yml`
* 安装依赖 pip install -r requirements.txt
* 开始爬虫
```shell
#爬取热门视频
python main.py 
#爬取所有视频
python main.py 1
```

#### 配置
- `endpoint`  定义快猫地址
- `save`      是否保存视频数据到数据库
- `pool_size` 爬取线程池数量
- `db`        数据库配置
- `download`  是否下载视频 (如果下载视频，线程池数会设置为1)

#### 生成 `requirements.txt` (可选)
- 安装 
```
    pip install pipreqs 
```

- 生成 
```
    pipreqs . --encoding=utf8 --force
```

#### 贡献

1.  push就完事了
