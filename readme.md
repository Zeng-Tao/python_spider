
# 爬虫

## 简介

#### 目的
学习爬虫的原理及应用

项目中是用了 request 和 pyquery 库, request 库用来抓取页面原始数据, pyquery 用来处理 HTML 文件, 可以方便的像操作 DOM 一样, 除此之外, 没有使用其他爬虫框架

#### 支持

- 支持抓取数据本地持久化, 二次抓取加速, 降低被网站封 IP 的风险
- 支持登录网站
- 支持图片抓取


## 豆瓣电影 250 抓取

#### 处理后的数据

- name 电影名
- other 电影别名
- score 豆瓣评分
- quote 电影一句话点评
- cover_url 海报封面 URL 地址
- ranking 豆瓣电影 250 排名


![avatar](https://github.com/Zeng-Tao/python_spider/raw/master/GIF/douban_movie_250.gif)

## 知乎个人关注动态

动态按时间分割抓取, 如 zhihu_7_24_16 表示为 7 月 24 号 16 时的动态

- title 问题标题
- answer_url 回答连接
- content 回答摘要

![avatar](https://github.com/Zeng-Tao/python_spider/raw/master/GIF/zhihu_follow.gif)


### 说明

    知乎个人动态需要登录, 涉及到个人 Cookie, 放在 secret.py 中
    需要写入自己的 Cookie, Cookie 可以从浏览器的开发者工具中找到