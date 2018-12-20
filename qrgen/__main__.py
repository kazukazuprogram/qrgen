#!/usr/bin/env python3
#coding: utf-8

from qrcode import make #qrcodeを起動
from sys import argv

img = make(argv[1]) #''内の文字をQRコードに変換

if not "-o" in argv:
    img.show() #生成したQRコードを表示
else:
    try:
        fn = argv[argv.index("-o")+1]
    except:
        fn = "qr_"++".png"
    img.save(fn) #QRコードに名前をつけて保存
