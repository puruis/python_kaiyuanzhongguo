#!/usr/bin/python
# -*- coding: utf-8 -*-
import datetime

import pymysql as pymysql


def insert(article_title,author_name, author_photo, release_time, article_content,news_links):
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "123456", "code_learning")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 插入语句
    dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sql = "INSERT INTO business_news(article_title,author_name, author_photo, release_time, article_content,news_links,create_time,from_source) \
           VALUES ('%s', '%s', '%s',  '%s',  '%s',  '%s' ,'%s','%s')" % \
          (article_title,author_name, author_photo, release_time, article_content,news_links,dt,'开源中国')
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 执行sql语句
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()

    # 关闭数据库连接
    db.close()

