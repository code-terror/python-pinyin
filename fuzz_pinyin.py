import atheris
import sys
import os
from pypinyin import pinyin, lazy_pinyin, Style
from pypinyin.converter import DefaultConverter

def TestOneInput(data):
    barray=bytearray(data)
    fdp=atheris.FuzzedDataProvider(data)
    if len(barray)>0:
        if barray[0]%5==0:
            pinyin(fdp.ConsumeString(len(data)))
        if barray[0]%5==1:
            pinyin(fdp.ConsumeString(len(data)),style=Style.TONE2,heteronym=True)
        if barray[0]%5==2:
            lazy_pinyin(fdp.ConsumeString(len(data)))
        if barray[0]%5==3:
            lazy_pinyin(fdp.ConsumeString(len(data)),Style.TONE3,tone_sandhi=True)
        else:
            DefaultConverter().convert(fdp.ConsumeString(len(data)),Style.TONE3,False,'ignore',True)


atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()
