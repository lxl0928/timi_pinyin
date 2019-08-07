from setuptools import setup

setup(
    name="timi-pinyin",
    version="1.0.0",
    url='http://github.com/lxl0928/timi_pinyin',
    author='Timi long',
    author_email='lixiaolong@smuer.cn',
    description='根据传入的字符串，返回该字符串的所有首字母',
    long_description="""传入字符串: '北京演示设备1', 返回: 'bjyssb1' """,
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
