import time
from email_validator import validate_email, EmailNotValidError
import requests
import re

from selenium import webdriver

from config import HEADERS, URL, URL_INST
from db import Items, session


def find_email(text):
    a = re.search(r'[^\s]+@[^\s]+.[^\s]+', text)
    if a is not None:
        email = a.group(0)
        try:
            valid = validate_email(email)
            email = valid.email
        except EmailNotValidError as e:
            return 'Нет почты'

        return email

    return 'Нет почты'


def parse_inst(nms, br: webdriver):
    to_xlsx = []
    j = 1
    for name in nms:
        print(j)
        url_ = URL_INST.format(name=name)

        br.get(url_)
        bio = br.find_element_by_class_name('-vDIg').text
        count = int(br.find_element_by_class_name('k9GMp ').find_elements_by_class_name('g47SY ')[1].get_attribute('title').replace(' ', ''))
        print(count)

        email = find_email(bio)

        print(email)
        print(count)

        item = Items(email=email, url=url_, subs=count)
        session.add(item)
        session.commit()
        data = (url_, count, email)
        to_xlsx.append(data)

        j += 1

    return to_xlsx
