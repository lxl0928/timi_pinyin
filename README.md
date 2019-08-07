# timi_pinyin
根据传入的input_str="费家村设备01", 返回该字符串的所有字符的拼音首字目组成的字符串: "fjcsb01".

# install 
```
pip install timi-pinyin==1.0.0
```

# examples

```
In [1]: from timi_pinyin import pinyin

In [2]: pinyin.get_first_letter_string(input_str="我是费家村南门设备01")
Out[2]: 'wsfjcnmsb01'

In [3]: device_01 = pinyin.get_first_letter_string(input_str="我是费家村南门设备01")

In [4]: device_02 = pinyin.get_first_letter_string(input_str="我是费家村南门设备01")

In [5]: sorted([device_01, device_02])
Out[5]: ['wsfjcnmsb01', 'wsfjcnmsb01']

# 按首字母排序
In [6]: device_01 = pinyin.get_first_letter_string(input_str="我是费家村南门设备01")

In [7]: device_02 = pinyin.get_first_letter_string(input_str="北京费家村南门设备01")

In [8]: sorted([device_01, device_02])
Out[8]: ['bjfjcnmsb01', 'wsfjcnmsb01']



In [1]: from timi_pinyin import get_first_letters

In [2]: get_first_letters("我是中国人")
Out[2]: 'wszgr'

In [3]: from timi_pinyin import lazy_pinyin

In [4]: lazy_pinyin("我是中国人")
Out[4]: ['wo', 'shi', 'zhong', 'guo', 'ren']

In [5]: from timi_pinyin import pypinyin

In [6]: pypinyin("我是中国人")
Out[6]: [['wǒ'], ['shì'], ['zhōng'], ['guó'], ['rén']]


```
