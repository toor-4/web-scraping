#!/bin/python3

from bs4 import BeautifulSoup
import re
import subprocess

with open('index.html') as f:
    file = f.read()
    soup = BeautifulSoup(file,'lxml')
    contributor = soup.find('div', class_="textwidget")
    number = contributor.find('h4').text
    print(number)
    names = contributor.find_all('li')
    for i,j in enumerate(names):
        if i > 0:
            print(j.text)

