import re as Regex
import os
from setuptools import find_packages, setup
import sys

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir))) # allow setup.py to be run from any path
__here = os.path.abspath(os.path.dirname(__file__))

if sys.version_info [:2] < (3, 4):
    raise RuntimeError("Unsupported Python version")

def readFile(filename):
    with open(os.path.join(__here, filename), 'r', encoding="utf-8") as file:
        return file.read()

#https://docs.python.org/3/distutils/setupscript.html
#https://packaging.python.org/tutorials/packaging-projects/#description
#https://stackoverflow.com/questions/26737222/pypi-description-markdown-doesnt-work
#https://stackoverflow.com/questions/1471994/what-is-setup-py
def getReadMe(filename="README.md"):
    try:
        import pypandoc
        return pypandoc.convert(filename, "rst").replace("\r","")
    except(IOError, ImportError):
        try:
            return readFile(filename)
        except FileNotFoundError:
            raise RuntimeError("File not found!")
def getRequeriments(filename="requirements.txt"):
    try:
        return readFile(filename).splitlines()
    except FileNotFoundError as exception:
        return [ "requests>=2.21.0", "requests-aeaweb>=0.0.1" ]
def regexFunc(pattern):
    stringFile = readFile("pyrez/__init__.py")
    return Regex.search(r'^__{}__\s*=\s*[\'"]([^\'"]*)[\'"]'.format(pattern), stringFile, Regex.MULTILINE).group(1)

NAME, AUTHOR, AUTHOR_EMAIL, DESCRIPTION, LICENSE, URL, VERSION = regexFunc("name"), regexFunc("author"), regexFunc("author_email"), regexFunc("description"), regexFunc("license"), regexFunc("url"), regexFunc("version")#https://www.python.org/dev/peps/pep-0440/

setup(
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    classifiers=[#https://pypi.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 5 - Production/Stable",
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
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Games/Entertainment",
        "Topic :: Internet",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities"
    ],
    description=DESCRIPTION,
    download_url="https://pypi.org/project/pyrez/#files",
    include_package_data=True,
    install_requires=getRequeriments(),
    keywords=["pyrez hirez hi-rez smite paladins realmapi open-source api wrapper library python api-wrapper paladins-api smitegame smiteapi realm-api realm-royale python3 python-3 python-3-6"],
    license=LICENSE,
    long_description=getReadMe(), # long_description=open ('README.rst').read () + '\n\n' + open ('HISTORY.rst').read (),
    long_description_content_type="text/markdown",#"text/x-rst", #https://guides.github.com/features/mastering-markdown/
    name=NAME,
    packages=find_packages(exclude=["docs", "tests", "examples", ".gitignore", ".gitattributes", "README.md"]),#find_packages(), # packages=[name] # find_packages (exclude=['docs', 'tests*']),
    #python_requires=">=3.0, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*, !=3.6.*, !=3.7.*, !=3.8.*",#>=2.6, 
    url=URL,
    version=VERSION,
    #zip_safe=True,
    project_urls={
        "Documentation": "https://github.com/luissilva1044894/pyrez/docs",
        "Source": "https://github.com/luissilva1044894/pyrez",
    },
)
if __name__ == "main":
    from subprocess import call as cmdShell
    if sys.argv[-1] == 'publish':# 'setup.py publish' shortcut.
        cmdShell("python setup.py sdist bdist_wheel", shell=False)
        cmdShell("twine upload dist/*", shell=False)
    else:
        cmdShell("python setup.py sdist", shell=False)
    sys.exit()
