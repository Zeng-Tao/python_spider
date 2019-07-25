import os
import time

import requests
from pyquery import PyQuery as pq
import secret


class Model:
    """
    基类, 用来显示类的信息
    """

    def __repr__(self):
        name = self.__class__.__name__
        properties = ('{}=({})'.format(k, v) for k, v in self.__dict__.items())
        s = '\n<{} \n  {}>'.format(name, '\n  '.join(properties))
        return s


class Answer(Model):
    def __init__(self):
        self.title = ''
        self.answer_url = ''
        self.content = ''


def get(url, filename):
    """
    缓存, 避免重复下载网页浪费时间
    """
    folder = 'zhihu_cached'
    # 建立 cached 文件夹
    if not os.path.exists(folder):
        os.makedirs(folder)

    path = os.path.join(folder, filename)
    if os.path.exists(path):
        with open(path, 'rb') as f:
            s = f.read()
            return s
    else:
        # 发送网络请求, 把结果写入到文件夹中
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/70.0.3538.110 '
                          'Safari/537.36',
            'Cookie': secret.zhihu_cookie,

        }
        r = requests.get(url, headers=headers)
        # r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            return r.content


def today():
    now = time.time()
    now = time.localtime(now)
    t = '{}_{}_{}'.format(now.tm_mon, now.tm_mday, now.tm_hour)
    return t


def cached_page(url):
    filename = 'zhihu_{}.html'.format(today())
    page = get(url, filename)
    return page


def answer_from_div(div):
    e = pq(div)

    m = Answer()
    m.title = e('.ContentItem-title a').text()
    if m.title == '':
        return None
    m.answer_url = 'www.zhihu.com{}'.format(e('.ContentItem-title a').attr('href'))
    m.content = e('.CopyrightRichText-richText').text()
    return m


def answers_from_url(url):
    page = cached_page(url)
    e = pq(page)
    cards = e('.TopstoryItem-isFollow')
    # 调用 answer_from_div
    answers = [answer_from_div(card) for card in cards]

    return answers


def main():
    url = 'https://www.zhihu.com/follow'
    answers = answers_from_url(url)
    print(answers)


if __name__ == '__main__':
    main()

    '''
    <h2 class="ContentItem-title">
        <div itemProp="zhihu:question" itemType="http://schema.org/Question" itemscope="">
            <meta itemProp="url" content="https://www.zhihu.com/question/333842651"/>
            <meta itemProp="name" content="如果没有生殖隔离地球会变成什么样？"/>
            <a target="_blank" data-za-detail-view-element_name="Title" data-za-detail-view-id="2812" href="/question/333842651/answer/759896098">
            如果没有生殖隔离地球会变成什么样？
            </a>
        </div>
    </h2>
    '''
