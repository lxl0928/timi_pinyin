# coding: utf-8

from pypinyin import pinyin, Style


class TimiPinYin(object):
    """ 根据输入的字符串，返回此字符串的中所有字符的拼音首字母

    """
    @classmethod
    def get_first_letter_string(cls, input_str: str):
        assert isinstance(input_str, str), "Param Type Error: input_str type error, support type: str."
        try:
            first_letters = pinyin(input_str, style=Style.FIRST_LETTER)
        except Exception as e:
            raise e
        return "".join(item[0] for item in first_letters)

    @classmethod
    def get_first_letter_list(cls, input_str: str):
        return list(cls.get_first_letter_string(input_str=input_str))
