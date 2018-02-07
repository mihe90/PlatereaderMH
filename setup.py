#!/usr/bin/env python3
try:
    from setuptools import setup, find_packages
except ImportError:
    print("setuptools not found, falling back to distutils")
    from distutils.core import setup

setup(
    name='PlatereaderMH',
    version='0.49',
    author='Michael Heimes',
    packages=find_packages(),
    #extras_require = {},
    scripts=['platereader/platereader.py'],
    install_requires=['pandas', 'numpy', 'openpyxl'],
    #platforms=['Linux', 'Windows', 'MacOSX'],
    #zip_safe=False,
    #classifiers=["License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    #             "Environment :: Console",
    #             "Intended Audience :: Science/Research",
    #             "Programming Language :: Python",
    #             "Programming Language :: Python :: 2.7",
    #             "Programming Language :: Python :: 3.4",],
    #package_data={},
    #license='GNU General Public License v2 (GPLv2)',
    description='A script to convert SpectraMax M5 platereader data to .xlsx',
    #long_description=,
    #url='',
)
