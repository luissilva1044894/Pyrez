#https://realpython.com/pipenv-guide/
import re as Regex
import os
import sys
from datetime import datetime
try:
    from setuptools import find_packages, setup
except (ImportError, ModuleNotFoundError):
    from distutils.core import setup

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir))) # allow setup.py to be run from any path
__here = os.path.abspath(os.path.dirname(__file__))

if sys.version_info[:2] < (3, 4) and datetime.utcnow().year >= 2020:
    raise RuntimeError("Unsupported Python version - Pyrez requires Python 3.4+")

def __readFile(fileName):
    with open(os.path.join(__here, fileName), 'r', encoding="utf-8") as f:
        return f.read()

#https://docs.python.org/3/distutils/setupscript.html
#https://packaging.python.org/tutorials/packaging-projects/#description
#https://stackoverflow.com/questions/26737222/pypi-description-markdown-doesnt-work
#https://stackoverflow.com/questions/1471994/what-is-setup-py
def __getReadMe(fileName="README.rst"):
    try:
        import pypandoc
        return pypandoc.convert(fileName, "rst").replace("\r","")
    except(IOError, ImportError):
        try:
            return __readFile(fileName)
        except FileNotFoundError:
            raise RuntimeError("File not found!")
def __getRequeriments(fileName="requirements.txt"):
    try:
        return __readFile(fileName).splitlines()
    except FileNotFoundError:
        return [ "pip>=19.1.1", "requests>=2.21.0", "requests-aeaweb>=0.0.1", "setuptools>=41.0.1", "urllib3==1.24.3" ]
def __regexFunc(pattern):
    return Regex.search(r'^__{}__\s*=\s*[\'"]([^\'"]*)[\'"]'.format(pattern), __readFile("pyrez/__version__.py"), Regex.MULTILINE).group(1)

__NAME, __AUTHOR, __AUTHOR_EMAIL, __DESCRIPTION, __LICENSE, __URL, __VERSION = __regexFunc("package_name"), __regexFunc("author"), __regexFunc("author_email"), __regexFunc("description"), __regexFunc("license"), __regexFunc("url"), __regexFunc("version")#https://www.python.org/dev/peps/pep-0440/
def getGithub(_acc, _end=None):
    return "https://github.com/{}/{}{}".format(_acc, __NAME, '/{}'.format(_end) if _end else '')
setup(
    author=__AUTHOR,
    author_email=__AUTHOR_EMAIL,
    classifiers=[#https://pypi.org/pypi?%3Aaction=list_classifiers
    #https://pypi.org/classifiers/
        "Development Status :: 4 - Beta",#Development Status :: 5 - Production/Stable
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        #"Programming Language :: Python :: 3 :: Only",
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
    description=__DESCRIPTION,
    extras_require={
        "async": [
            "aiohttp>=3.5.4",
            "asyncio>=3.4.3",
        ],
        "docs": [
            "sphinx==1.7.4",
            "sphinxcontrib-asyncio",
            "sphinxcontrib-websupport",
        ]
    },
    #download_url="https://pypi.org/project/pyrez/#files", #getGithub("luissilva1044894", "tarball/{}".format(__VERSION))
    include_package_data=True,
    install_requires=__getRequeriments(),
    keywords=["pyrez", "hirez", "hi-rez", "smite", "paladins", "realmapi", "open-source", "api", "wrapper", "library", "python", "api-wrapper", "paladins-api", "smitegame", "smiteapi", "realm-api", "realm-royale", "python3", "python-3", "python-3-6"],
    license=__LICENSE,
    long_description=__getReadMe(), # long_description=open ('README.rst').read () + '\n\n' + open ('HISTORY.rst').read (), #u'\n\n'.join([readme, changes]),
    long_description_content_type="text/markdown; charset=UTF-8; variant=GFM",#"text/x-rst", #https://guides.github.com/features/mastering-markdown/
    maintainer=__AUTHOR, #u__AUTHOR,
    maintainer_email=__AUTHOR_EMAIL,
    name=__NAME,
    packages=find_packages(exclude=["docs", "tests", "examples", ".gitignore", ".github", ".gitattributes", "README.md"]),#find_packages(), # packages=[name] # find_packages (exclude=['docs', 'tests*']),
    python_requires=">=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,<4", #python_requires=">=3.0, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*, !=3.6.*, !=3.7.*, !=3.8.*",#>=2.6,
    setup_requires=[ "pip>=19.1.1", "setuptools>=41.0.1" ],
    url=__URL,
    version=__VERSION,
    #zip_safe=True,
    #include_package_data=True, # include everything in source control (Accept all data files and directories matched by MANIFEST.in)
    project_urls={
        "Documentation": "{}{}".format(__URL, "docs/#welcome-to-the-pyrez-wiki"),
        "Source Code": getGithub("luissilva1044894"),
        #"Changelog": "https://wheel.readthedocs.io/en/stable/news.html",
        "Issue Tracker": getGithub("luissilva1044894", "issues"),
        "Official Support": "https://discord.gg/XkydRPS",
    },
)
if __name__ == "main":
    from subprocess import call as cmdShell
    if sys.argv[-1] == "publish":# "setup.py publish" shortcut.
        cmdShell("python setup.py sdist bdist_wheel", shell=False)
        cmdShell("twine upload dist/*", shell=False)
    else:
        cmdShell("python setup.py sdist", shell=False)
    sys.exit()
#python setup.py sdist bdist_wheel > create dist folder
#twine upload --repository-url https://test.pypi.org/legacy/ dist/* > upload test-pypi
#twine upload dist/* > upload pypi
#python setup.py sdit upload -r pypi > upload pypi
