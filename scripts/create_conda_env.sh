#!/bin/sh
conda create -n km python=3.9

conda activate km
cd ../
pip install -r requirements.txt

