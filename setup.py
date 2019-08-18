# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 20:51:08 2019

@author: piotr_000
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="LDS-ctrl",
    version="0.0.1",
    author="Piotr Kaminski",
    author_email="author@example.com",
    description="LDS station",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)