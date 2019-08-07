# coding: utf-8

from timi_pinyin import pinyin


class TestTimiPinYin(object):

    def test_first_letter_string(self):
        result = pinyin.get_first_letter_string(input_str="费家村南门设备01")
        assert isinstance(result, str)
        print(result)

    def test_first_letter_list(self):
        result = pinyin.get_first_letter_list(input_str="费家村停车场出口")
        assert isinstance(result, list)
        print(result)


obj = TestTimiPinYin()
obj.test_first_letter_string()
obj.test_first_letter_list()

"""
fjcnmsb01
['f', 'j', 'c', 't', 'c', 'c', 'c', 'k']
"""