#!/bin/sh
conda create -n km python=3.9

conda activate km

pip install requests
pip install pycrypto
pip install pymysql
pip install pyyaml
