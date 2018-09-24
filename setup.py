import re as Regex
import os
from setuptools import find_packages, setup
import sys

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir))) # allow setup.py to be run from any path

if sys.version_info [:2] < (3, 4):
    raise RuntimeError("Unsupported Python version")

def readFile(filename):
    with open(os.path.join(os.path.dirname(__file__), filename), 'r') as file:
        return file.read()
def readMe(filename = "README.rst"):
    try:
        return readFile(filename)
    except Exception:
        raise RuntimeError("File not found!")
def requeriments(filename = "requirements.txt"):
    try:
        return readFile(filename).splitlines()
    except Exception:
        return [ 'requests>=2.18.4', 'requests-aeaweb>=0.0.1' ]
def regexFunc(pattern):
    stringFile = readFile("pyrez/__init__.py")
    return Regex.search(r'^__{}__\s*=\s*[\'"]([^\'"]*)[\'"]'.format(pattern), stringFile, Regex.MULTILINE).group(1)

VERSION = regexFunc("version")
AUTHOR = regexFunc ("author")
LICENSE = regexFunc("license")
NAME = regexFunc("name")

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
    download_url="https://pypi.org/project/pyrez/#files",
    include_package_data=True,
    install_requires=requeriments(),
    keywords=["hirez hi-rez smite paladins realmapi open-source api wrapper library python api-wrapper paladins-api smitegame smiteapi realm-api python3 python-3 python-3-6"],
    license=LICENSE,
    long_description=readMe(), # long_description=open ('README.rst').read () + '\n\n' + open ('HISTORY.rst').read (),
    long_description_content_type="text/x-rst",
    name=NAME,
    packages=find_packages(), # packages=[name] # find_packages (exclude=['docs', 'tests*']),
    url="https://github.com/luissilva1044894/PyRez",
    version=VERSION,
    zip_safe=True,
    project_urls={
        "Documentation": "http://pyrez.readthedocs.io/en/latest/?badge=latest",
        "Source": "https://github.com/luissilva1044894/PyRez",
    },
)
if __name__ == "main":
    os.system ("python setup.py sdist")
    sys.exit()
