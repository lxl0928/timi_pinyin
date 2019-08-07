from setuptools import setup

setup(
    name="timi-pinyin",
    version="1.0.1",
    url='http://github.com/lxl0928/timi_pinyin',
    author='Timi long',
    author_email='lixiaolong@smuer.cn',
    description='根据传入的input_str="费家村设备01", 返回该字符串的所有字符的拼音首字目组成的字符串: "fjcsb01".',
    long_description="""根据传入的input_str="费家村设备01", 返回该字符串的所有字符的拼音首字目组成的字符串: "fjcsb01"., 
    文档:  http://github.com/lxl0928/timi_pinyin/README.md """,
    packages=['timi_pinyin'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    extras_require={
        "pypinyin": ["pypinyin"],
    },
    install_requires=["pypinyin==0.35.4"]
)
