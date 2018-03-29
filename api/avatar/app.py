#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import time
from io import BytesIO
from .utils.visicon import Visicon

def ff(size=30):
    ip = "127.0.0.1"
    img = Visicon(ip, str(time()), size).draw_image()
    temp_img = BytesIO()
    img.save(temp_img, 'png')
    img_data = temp_img.getvalue()
    temp_img.close()
    return img_data

if __name__ == '__main__':
    ff()
