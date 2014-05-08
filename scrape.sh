#!/bin/bash
cp ./urls.txt ./getSchools
cd ./getSchools
scrapy crawl schools
cp ./schools.txt ../rankings
cd ../rankings
scrapy crawl rankings
mv rankings_items.csv ..
