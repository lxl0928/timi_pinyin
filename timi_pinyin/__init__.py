# coding: utf-8

from pypinyin import *
from pypinyin import pinyin as pypinyin

from .__version__ import __version__, __title__, __description__, __url__, __author_email__
from .main import TimiPinYin

pinyin = TimiPinYin()
get_first_letters = pinyin.get_first_letter_string
get_first_letters_with_list = pinyin.get_first_letter_list

