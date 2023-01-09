#!/usr/bin/env python3
"""

    iceweather: Look up information about Icelandic weather (observations, forecasts,
    human readable descriptive texts, etc.) using vedur.is xmlweather API.

    Copyright (c) 2019-2023 Miðeind ehf.
    Original author: Sveinbjorn Thordarson

    BSD 3-clause License (see License.txt).

"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="iceweather",
    version="0.2.3",
    author="Miðeind ehf.",
    author_email="mideind@mideind.is",
    license="BSD",
    url="https://github.com/mideind/iceweather",
    description="Look up Icelandic weather information (observations, forecasts, etc.)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["requests"],
    packages=["iceweather"],
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
    zip_safe=True,
)
