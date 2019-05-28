#https://realpython.com/pipenv-guide/
import os
import sys
from subprocess import call
from setuptools import find_packages, setup, Command

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir))) # allow setup.py to be run from any path
HERE = os.path.abspath(os.path.dirname(__file__))

def __getGithub(_acc, _end=None):
    return "https://github.com/{}/{}{}".format(_acc, NAME, "/{}".format(_end) if _end else '')
def __readFile(fileName):
    with open(os.path.join(HERE, fileName), 'r', encoding="utf-8") as f:
        return f.read()
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
NAME, AUTHOR, AUTHOR_EMAIL, DESCRIPTION, LICENSE, URL, VERSION = __regexFunc("package_name"), __regexFunc("author"), __regexFunc("author_email"), __regexFunc("description"), __regexFunc("license"), __regexFunc("url"), __regexFunc("version")#https://www.python.org/dev/peps/pep-0440/

if sys.version_info[:2] < (3, 5) and datetime.utcnow().year >= 2020:
    print("ERROR: {} requires at least Python 3.5 to run.".format(NAME.capitalize()))
    sys.exit(1)
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
        from shutil import rmtree
        try:
            self.status("Removing previous builds…")
            rmtree(os.path.join(HERE, "dist"))
        except OSError:
            pass
        self.status("Updating Pip, Wheel and Twine…")
        call("pip install --upgrade pip wheel twine", shell=False)
        self.status("Building Source and Wheel (universal) distribution…")
        call("{} setup.py sdist bdist_wheel --universal".format(sys.executable), shell=False)
        self.status("Uploading the {} package to PyPI via Twine…".format(NAME))
        call("twine upload dist/*", shell=False)
        self.status("Pushing git tags…")
        call("git tag {}".format(VERSION), shell=False)#git tag v{0}
        call("git push --tags", shell=False)
        sys.exit()
#https://docs.python.org/3/distutils/setupscript.html
#https://packaging.python.org/tutorials/packaging-projects/#description
#https://stackoverflow.com/questions/26737222/pypi-description-markdown-doesnt-work
#https://stackoverflow.com/questions/1471994/what-is-setup-py
#https://stackoverflow.com/questions/17803829/how-to-customize-a-requirements-txt-for-multiple-environments
DOCS_EXTRAS_REQUIRE = [
    "sphinx_rtd_theme>=0.4.3,<1",
    "sphinxcontrib-asyncio",
    "sphinxcontrib-websupport",
]
DEV_EXTRAS_REQUIRE = [
    "pip>=19.1.1",
    "pipenv>=2018.11.26",
    "setuptools>=41.0.1",
    "twine>=1.13.0",
    "wheel==0.33.4",
]
INSTALL_EXTRAS_REQUIRE = [
    "requests>=2.22.0,<3",
]
setup(
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    classifiers=[#https://pypi.org/pypi?%3Aaction=list_classifiers #https://pypi.org/classifiers/
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        #"Programming Language :: Python :: 3 :: Only",
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
    description=DESCRIPTION,
    entry_points = {
        'console_scripts': [
            "{0}={0}.command_line:main".format(NAME)
        ],
    },
    extras_require={
        "dev": DEV_EXTRAS_REQUIRE,
        "docs": DOCS_EXTRAS_REQUIRE,
    },
    #download_url="https://pypi.org/project/pyrez/#files", #__getGithub("luissilva1044894", "tarball/{}".format(VERSION)) #{}/archive/{}.tar.gz".format(__getGithub("luissilva1044894"), VERSION)
    download_url=__getGithub("luissilva1044894", "archive/{}.tar.gz".format(VERSION)),
    include_package_data=True,
    install_requires=INSTALL_EXTRAS_REQUIRE,
    keywords=["pyrez", "hirez", "hi-rez", "smite", "paladins", "realmapi", "open-source", "api", "wrapper", "library", "python", "api-wrapper", "paladins-api", "smitegame", "smiteapi", "realm-api", "realm-royale", "python3", "python-3", "python-3-6"],
    license=LICENSE,
    long_description=__getReadMe(), # long_description=open ('README.rst').read () + '\n\n' + open ('HISTORY.rst').read (), #u'\n\n'.join([readme, changes]),
    long_description_content_type="text/markdown; charset=UTF-8; variant=GFM", #https://guides.github.com/features/mastering-markdown/
    maintainer=AUTHOR,
    maintainer_email=AUTHOR_EMAIL,
    name=NAME,
    packages=find_packages(exclude=["docs", "tests*", "examples", ".gitignore", ".github", ".gitattributes", "README.md"]),# packages=[name]
    platforms = "Any",
    python_requires=">=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*,<4", #python_requires=">=3.0, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*, !=3.6.*, !=3.7.*, !=3.8.*",
    setup_requires=DEV_EXTRAS_REQUIRE,
    url=URL,
    version=VERSION,
    #zip_safe=True,
    #include_package_data=True, # include everything in source control (Accept all data files and directories matched by MANIFEST.in)
    project_urls={
        "Documentation": "https://{}.readthedocs.io/en/stable/".format(NAME),
        "Discord: Support Server": "https://discord.gg/XkydRPS",
        #"Changelog": "https://pyrez.readthedocs.io/en/stable/news.html",
        "Github: Issues": __getGithub("luissilva1044894", "issues"),
        "Github: Repo": __getGithub("luissilva1044894"),
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
