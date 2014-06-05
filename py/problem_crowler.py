#!/usr/bin/env python3

from urllib import urlopen
from bs4 import BeautifulSoup
from string import Template


def get_problem_info(num):
    url = 'http://projecteuler.net/problem='

    soup = BeautifulSoup(urlopen(url + str(num)).read())
    p = soup.find(id='content')
    title = p.h2.text
    description = p.find(class_='problem_content').text.strip('\r\n')
    return {
        'title': title,
        'description': description,
        'problem_num': num
    }


def gen_problem(num):
    info = get_problem_info(num)
    print info
    t = Template(open('file_template.py').read())
    f = t.safe_substitute(info)
    filename = "euler_{0:03d}.py".format(num)
    w = open(filename, 'w')
    w.write(f.encode('UTF8'))

for i in range(77,81):
    gen_problem(i)
