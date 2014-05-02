#/usr/bin/env python
import os
from setuptools import setup, find_packages

ROOT_DIR = os.path.dirname(__file__)
SOURCE_DIR = os.path.join(ROOT_DIR)
VERSION = "0.1"

reqs = []
with open("requirements.txt", "r+") as f:
    for line in f.readlines():
        reqs.append(line.strip())

try:
   import pypandoc
   long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    long_description = ''   

setup(
    name="correlationbot",
    description="A friendly python statistics bot",
    long_description=long_description,
    author="Steven Skoczen",
    author_email="steven@greenkahuna.com",
    url="https://github.com/greenkahuna/correlationbot",
    version=VERSION,
    download_url = ['https://github.com/greenkahuna/correlationbot/tarball/%s' % VERSION, ],
    install_requires=reqs,
    packages=find_packages(),
    include_package_data=True,
    keywords = ["statistics", "bot", "service"],
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Communications :: Chat",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],

)
