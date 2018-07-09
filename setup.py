import re as Regex
import os
from setuptools import find_packages, setup
import sys

os.chdir (os.path.normpath (os.path.join (os.path.abspath (__file__), os.pardir))) # allow setup.py to be run from any path

if sys.version_info [:2] < (3, 4):
    raise RuntimeError ("Unsupported Python version")

def readFile (filename):
    with open (os.path.join (os.path.dirname (__file__), filename), 'r') as file: #open(os.path.join (os.path.dirname(__file__), encoding="utf-8")
        return file.read ()
def readMe (filename = "README.md"):
    try:
        return readFile (filename)
    except Exception:
        raise RuntimeError ("File not found!")

def requeriments (filename = "requirements.txt"):
    try:
        return readFile (filename).splitlines ()
    except Exception:
        raise RuntimeError ("File not found!")

INIT_FILE = readFile ("pyrez/__init__.py")
VERSION = Regex.search (r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', INIT_FILE, Regex.MULTILINE).group (1)
AUTHOR = Regex.search (r'^__author__\s*=\s*[\'"]([^\'"]*)[\'"]', INIT_FILE, Regex.MULTILINE).group (1)
LICENSE = Regex.search (r'^__license__\s*=\s*[\'"]([^\'"]*)[\'"]', INIT_FILE, Regex.MULTILINE).group (1)
NAME = Regex.search (r'^__name__\s*=\s*[\'"]([^\'"]*)[\'"]', INIT_FILE, Regex.MULTILINE).group (1)

setup(
    author=AUTHOR,
    author_email="luis.silva.1044894@sga.pucminas.br",
    classifiers=[#https://pypi.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Games/Entertainment",
        "Topic :: Internet",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    description="An open-source wrapper for Hi-Rez API (Paladins, Realm Royale, and Smite), written in Python",
    download_url='https://pypi.org/projects/pyrez',
    include_package_data=True,
    install_requires=requeriments (),
    keywords=["hirez hi-rez smite paladins realmapi open-source api wrapper library python api-wrapper paladins-api smitegame smiteapi realm-api python3 python-3 python-3-6"],
    license=LICENSE,
    long_description=readMe (), # long_description=open ('README.rst').read () + '\n\n' + open ('HISTORY.rst').read (),
    name=NAME,
    packages=find_packages (), # packages=[name] # find_packages (exclude=['docs', 'tests*']),
    url="https://github.com/luissilva1044894/PyRez",
    version=VERSION,
    zip_safe=True
)
if __name__ == "main":
    os.system ("python setup.py sdist")
    sys.exit ()
