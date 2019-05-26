#https://realpython.com/pipenv-guide/
import os
import sys
from datetime import datetime
from subprocess import call
from shutil import rmtree
from setuptools import find_packages, setup, Command

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir))) # allow setup.py to be run from any path
here = os.path.abspath(os.path.dirname(__file__))

if sys.version_info[:2] < (3, 4) and datetime.utcnow().year >= 2020:
    raise RuntimeError("Unsupported Python version - Pyrez requires Python 3.4+")

def __readFile(fileName):
    with open(os.path.join(here, fileName), 'r', encoding="utf-8") as f:
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
def __regexFunc(pattern):
    import re
    return re.search(r'^__{}__\s*=\s*[\'"]([^\'"]*)[\'"]'.format(pattern), __readFile("pyrez/__version__.py"), re.MULTILINE).group(1)

__NAME, __AUTHOR, __AUTHOR_EMAIL, __DESCRIPTION, __LICENSE, __URL, __VERSION = __regexFunc("package_name"), __regexFunc("author"), __regexFunc("author_email"), __regexFunc("description"), __regexFunc("license"), __regexFunc("url"), __regexFunc("version")#https://www.python.org/dev/peps/pep-0440/
def getGithub(_acc, _end=None):
    return "https://github.com/{}/{}{}".format(_acc, __NAME, "/{}".format(_end) if _end else '')

class UploadCommand(Command):
    """Support setup.py upload."""

    description = "Build and publish the package."
    user_options = []

    @staticmethod
    def status(s):
        print("\033{}".format(s))
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        try:
            self.status("Removing previous builds…")
            rmtree(os.path.join(here, "dist"))
        except OSError:
            pass
        self.status("Updating Pip, Wheel and Twine…")
        call("pip install --upgrade pip wheel twine", shell=False)
        self.status("Building Source and Wheel (universal) distribution…")
        call("{} setup.py sdist bdist_wheel --universal".format(sys.executable), shell=False)
        self.status("Uploading the package to PyPI via Twine…")
        call("twine upload dist/*", shell=False)
        #self.status("Pushing git tags…")
        #call("git tag v{0}".format(about["__version__"]), shell=False)
        #call("git push --tags", shell=False)
        sys.exit()
#https://stackoverflow.com/questions/17803829/how-to-customize-a-requirements-txt-for-multiple-environments
DOCS_EXTRAS_REQUIRE = [
    "sphinx>=2.0.1",
    "sphinxcontrib-asyncio",
    "sphinxcontrib-websupport",
]
ASYNC_EXTRAS_REQUIRE = [
    "aiohttp>=3.5.4;python_version>='3.5'",
    "asyncio>=3.4.3;python_version>='3.4'",
]
DEV_EXTRAS_REQUIRE = [
    "pip>=19.1.1",
    "pipenv>=2018.11.26",
    "setuptools>=41.0.1",
    "twine>=1.13.0"
]
INSTALL_EXTRAS_REQUIRE = [
    "requests>=2.22.0,<3",
]
setup(
    author=__AUTHOR,
    author_email=__AUTHOR_EMAIL,
    classifiers=[#https://pypi.org/pypi?%3Aaction=list_classifiers #https://pypi.org/classifiers/
        "Development Status :: 4 - Beta",#Development Status :: 5 - Production/Stable
        "Intended Audience :: Developers",
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
    cmdclass={
        "upload": UploadCommand, #$ setup.py upload support.
    },
    description=__DESCRIPTION,
    extras_require={
        "async": ASYNC_EXTRAS_REQUIRE,
        "dev": DEV_EXTRAS_REQUIRE,
        "docs": DOCS_EXTRAS_REQUIRE,
    },
    #download_url="https://pypi.org/project/pyrez/#files", #getGithub("luissilva1044894", "tarball/{}".format(__VERSION)) #{}/archive/{}.tar.gz".format(getGithub("luissilva1044894"), __VERSION)
    include_package_data=True,
    install_requires=INSTALL_EXTRAS_REQUIRE,
    keywords=["pyrez", "hirez", "hi-rez", "smite", "paladins", "realmapi", "open-source", "api", "wrapper", "library", "python", "api-wrapper", "paladins-api", "smitegame", "smiteapi", "realm-api", "realm-royale", "python3", "python-3", "python-3-6"],
    license=__LICENSE,
    long_description=__getReadMe(), # long_description=open ('README.rst').read () + '\n\n' + open ('HISTORY.rst').read (), #u'\n\n'.join([readme, changes]),
    long_description_content_type="text/markdown; charset=UTF-8; variant=GFM", #https://guides.github.com/features/mastering-markdown/
    maintainer=__AUTHOR,
    maintainer_email=__AUTHOR_EMAIL,
    name=__NAME,
    packages=find_packages(exclude=["docs", "tests*", "examples", ".gitignore", ".github", ".gitattributes", "README.md"]),# packages=[name]
    platforms = "Any",
    python_requires=">=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*,<4", #python_requires=">=3.0, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*, !=3.6.*, !=3.7.*, !=3.8.*",
    setup_requires=DEV_EXTRAS_REQUIRE,
    url=__URL,
    version=__VERSION,
    #zip_safe=True,
    #include_package_data=True, # include everything in source control (Accept all data files and directories matched by MANIFEST.in)
    project_urls={
        "Documentation": "http://pyrez.rtfd.io/",
        "Discord: Support Server": "https://discord.gg/XkydRPS",
        #"Changelog": "https://pyrez.readthedocs.io/en/stable/news.html",
        "Github: Issues": getGithub("luissilva1044894", "issues"),
        "Github: Repo": getGithub("luissilva1044894"),
        "Say Thanks!": "https://saythanks.io/to/luissilva1044894",
    },
)
if __name__ == "main":
    if sys.argv[-1] == "publish":#"setup.py publish" shortcut.
        call("python setup.py sdist bdist_wheel", shell=False)
        call("twine upload dist/*", shell=False)
    else:
        call("python setup.py sdist upload", shell=False)#os.system(payload, shell=False) #os.popen(payload)
    sys.exit()
#python setup.py sdist bdist_wheel > create dist folder
#twine upload --repository-url https://test.pypi.org/legacy/ dist/* > upload test-pypi
#twine upload dist/* > upload pypi
#python setup.py sdit upload -r pypi > upload pypi
