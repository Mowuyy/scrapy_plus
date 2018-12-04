#coding:utf-8

# pip <= 9.0
try:
    from pip.req import parse_requirements
# pip > 9.0-
except:
    from pip._internal.req import parse_requirements

from setuptools import find_packages, setup


with open('./version.txt', 'r') as f:
    version = f.read()
    """
        作为一个合格的模块，应该要有版本号哦。
    """
setup(
    name='scrapy_plus',    # 模块名称
    version=version,  # 版本号
    description='A mini spider framework, like Scrapy',    # 描述
    packages=find_packages(exclude=[]),  # 获取代码里所有的package
    author='itheima',
    author_email='xxx@qq.com',
    license='Apache License v2', # 软件授权协议， GPL、BSD、APL
    package_data={'': ['*.*']},
    url='#',
    install_requires=[str(ir.req) for ir in parse_requirements("requirements.txt", session=False)],#所需的运行环境
    zip_safe=False, # 安装后在windows上卸载不会报错
    classifiers=[
        'Programming Language :: Python',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Unix',
        'Operating System :: GNU/Linux',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
