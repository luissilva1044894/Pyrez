#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

"""
Setup script for the `Pyrez` package.
**python setup.py install**
  Install from the working directory into the current Python environment.
**python setup.py sdist**
  Build a source distribution archive.
**python setup.py bdist_wheel**
  Build a wheel distribution archive.
**python setup.py upload**
  Upload pyrez package.
"""
#https://realpython.com/pipenv-guide/

# Standard library modules.
import os
import sys

try:
    from setuptools import setup, find_packages, Command
except ImportError:
    from distutils.core import setup, find_packages, Command

def call_(cmd, show_stdout=True, shell=False):
    """Execute *cmd* and return True on success."""
    from subprocess import call
    if show_stdout:
        rc = call(cmd, shell=shell)
    else:
        with open(os.devnull, 'w') as n:
            rc = call(cmd, shell=shell, stdout=n)
    return rc == 0

if sys.argv[-1] == 'publis':#'setup.py publish' shortcut.
    call_('python setup.py sdist bdist_wheel')
    call_('twine upload dist/*'.format)
    #print("You probably want to also tag the version now:")
    #print("  git tag -a %(version)s -m 'version %(version)s'" % args)
    #print("  git push --tags")
    sys.exit()
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir))) # allow setup.py to be run from any path
HERE = os.path.abspath(os.path.dirname(__file__))

def __getGithub(_end=None, _user='luissilva1044894'):
    return 'https://github.com/{}/{}{}'.format(_user, NAME, '/{}'.format(_end) if _end else '')
def __readFile(filename):
    with open(os.path.join(HERE, filename), 'r', encoding='utf-8') as f:
        return f.read()

#def load_requirements(fname):
#    with open(fname) as f:
#        line_iter = (line.strip() for line in f.readlines())
#        return [line for line in line_iter if line and line[0] != '#']

def __getRequirements(filename='pip'):
    """ load requirements from a pip requirements file """
    requirements = []
    for requirement in __readFile('requirements/{}'.format(filename if filename.endswith(".txt") else '{}.txt'.format(filename))).splitlines():
        if requirement:
            if requirement[:3].lower() == '-r ':
                requirements += __getRequirements(requirement[3:].lower())
            elif requirement[:3].lower() == '-e ' or requirement[0] == '#':
                pass
            else:
                requirements.append(requirement)
    return requirements
    #return __readFile(filename).splitlines()
def __getReadMe(filename='README.rst'):
    try:
        import pypandoc
        return pypandoc.convert(filename, 'rst').replace('\r', '')
        #pypandoc.convert_text(readme_md.read(), 'rst', 'markdown', extra_args=["--eol=lf"])
    except(IOError, ImportError):
        try:
            return __readFile(filename)
        except FileNotFoundError:
            raise RuntimeError('File not found!')
def __regexFunc(pattern, package_name='pyrez'):
    import re
    pattern_match = re.search(r'^__{pattern}__\s*=\s*[\'"]([^\'"]*)[\'"]'.format(pattern=pattern), __readFile("{package_name}/__version__.py".format(package_name=package_name)), re.MULTILINE)#r"^__{pattern}__ = ['\"]([^'\"]*)['\"]".format(pattern=pattern)

    return pattern_match.group(1) if pattern_match else None
def __getMetadata(package_name='pyrez'):
    meta_ = {}
    exec(__readFile('{package_name}/__version__.py'.format(package_name=package_name)), meta_)
    return meta_
_exec = __getMetadata()
#__regexFunc("package_name"), __regexFunc("author"), __regexFunc("author_email"), __regexFunc("description"), __regexFunc("license"), __regexFunc("url"), __regexFunc("version")#https://www.python.org/dev/peps/pep-0440/
NAME, AUTHOR, AUTHOR_EMAIL, DESCRIPTION, LICENSE, URL, VERSION = _exec["__package_name__"], _exec["__author__"],_exec["__author_email__"], _exec["__description__"], _exec["__license__"], _exec["__url__"], _exec["__version__"]

if sys.version_info[:2] < (3, 5) and datetime.utcnow().year >= 2020:
    print("ERROR: {} requires at least Python 3.5 to run.".format(NAME.capitalize()))
    sys.exit(1)
class BaseCommand(Command):
    """Support setup.py upload."""
    description = __doc__
    user_options = []
    @staticmethod
    def input(message):
        # Python 2.x/3.x compatibility
        try:
            return raw_input(message)
        except NameError:
            return input(message)
    @staticmethod
    def recursive_delete(path):
        from shutil import rmtree
        try:
            rmtree(os.path.join(HERE, path))
        except OSError:
            pass
    @staticmethod
    def confirm(message):
        """ask a yes/no question, return result"""
        if not sys.stdout.isatty():
            return False
        reply = BaseCommand.input("\n{message} [Y/N]:".format(message=message))
        return reply and reply[0].lower() == 'y'
    @staticmethod
    def status_msgs(*msgs):
        print('*' * 75)
        for msg in msgs:
            print(msg)
        print('*' * 75)
    @staticmethod
    def status(s):
        """Prints things in bold."""
        print("\033 {}".format(s))#print("\033[1m{0}\033[0m".format(s))
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        pass
class DocsCommand(BaseCommand):
    """ For building the Pyrez documentation with `python setup.py docs`. This generates html, and documentation files. """
    def run(self):
        print(self.confirm("TESTING?!"))
class UploadCommand(BaseCommand):
    """Support setup.py upload."""

    description = "Build and publish the package."

    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        self.status("Removing previous builds…")
        self.recursive_delete("dist")
        self.status("Updating Pip, SetupTools, Twine and Wheel…")
        call_("pip install --upgrade pip setuptools twine wheel")
        self.status("Building Source and Wheel (universal) distribution…")
        # Warning (Wheels): If your project has optional C extensions, it is recommended not to publish a universal wheel, because pip will prefer the wheel over a source installation.
        call_("{PATH} setup.py sdist bdist_wheel --universal".format(PATH=sys.executable)) #call([sys.executable, "setup.py sdist bdist_wheel --universal"], shell=False)
        self.status("Uploading the {NAME} package to PyPI via Twine…".format(NAME=NAME.capitalize()))
        call_("twine upload dist/*")
        if self.confirm("Push tags"):
            self.status("Pushing git tags…")
            call_("git tag {VERSION}".format(VERSION=VERSION))#git tag v{0}
            call_("git push --tags")
        if self.confirm("Clear?"): #rm -r dist build *.egg-info
            self.recursive_delete("dist")
            self.recursive_delete("build")
            self.recursive_delete("{NAME}.egg-info".format(NAME=NAME))
        sys.exit()
#https://docs.python.org/3/distutils/setupscript.html
#https://packaging.python.org/tutorials/packaging-projects/#description
#https://stackoverflow.com/questions/26737222/pypi-description-markdown-doesnt-work
#https://stackoverflow.com/questions/1471994/what-is-setup-py
#https://stackoverflow.com/questions/17803829/how-to-customize-a-requirements-txt-for-multiple-environments
LICENSES = {
    "Apache": "License :: OSI Approved :: Apache Software License",
    "BSD": "License :: OSI Approved :: BSD License",
    "GPLv3": "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "ISCL": "License :: OSI Approved :: ISC License (ISCL)",
    "LGPL": "License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)",
    "MIT": "License :: OSI Approved :: MIT License",
}
DEVELOPMENT_STATUS = {
    "PLANNING": "Development Status :: 1 - Planning",
    "PRE_ALPHA": "Development Status :: 2 - Pre-Alpha",
    "ALPHA": "Development Status :: 3 - Alpha",
    "BETA": "Development Status :: 4 - Beta",
    "STABLE": "Development Status :: 5 - Production/Stable",
    "MATURE": "Development Status :: 6 - Mature",
    "INACTIVE": "Development Status :: 7 - Inactive",
}
setup(
    # A string corresponding the package author’s name
    author=AUTHOR,

    # A string corresponding the email address of the package author
    author_email=AUTHOR_EMAIL,
    classifiers=[
        # Trove classifiers - Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers | https://pypi.org/classifiers/
        DEVELOPMENT_STATUS['STABLE'],
        "Intended Audience :: Developers",
        LICENSES[LICENSE],
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
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities"
    ],
    cmdclass={
        "upload": UploadCommand, #$ setup.py upload support.
        "docs": DocsCommand,
    },
    description=DESCRIPTION,

    # A dictionary mapping entry point group names to strings or lists of strings defining the entry points. Entry points are used to support dynamic discovery of services or plugins provided by a project.
    entry_points = {
        "console_scripts": [
            "{project_slug}={project_slug}.command_line:main".format(project_slug=NAME),#"{0}-cli={0}.command_line:main".format(NAME),
        ],
    },

    # A dictionary mapping names of “extras” (optional features of your project) to strings or lists of strings specifying what other distributions must be installed to support those features.
    extras_require={
        # Environment Marker works for wheel 0.24 or later
        #':os_name=="nt"': ['colorama<1'],#;platform_system=="Windows" #:sys_platform=="win32"
        'dev': __getRequirements('dev'),
        'docs': __getRequirements('docs'),
    },
    #download_url="https://pypi.org/project/{}/#files".format(NAME),
    #__getGithub("tarball/{}".format(VERSION))
    download_url="{}/archive/{}.tar.gz".format(URL, VERSION),#__getGithub("archive/{}.tar.gz".format(VERSION))

    # If set to True, this tells setuptools to automatically include any data files it finds inside your package directories (Accept all data files and directories it finds inside your package directories that are specified by your MANIFEST.in file)
    include_package_data=True,

    # A string or list of strings specifying what other distributions need to be installed when this one is
    install_requires=__getRequirements(),
    keywords=['pyrez', 'hirez', 'hi-rez', 'smite', 'paladins', 'realmapi', 'open-source', 'api', 'wrapper', 'library', 'python', 'api-wrapper', 'paladins-api', 'smitegame', 'smiteapi', 'realm-api', 'realm-royale', 'python3', 'python-3', 'python-3-6', 'async', 'asyncio'],
    license=LICENSE,
    long_description=__getReadMe(), # long_description=open ('README.rst').read () + '\n\n' + open ('HISTORY.rst').read (), #u'\n\n'.join([readme, changes]),
    long_description_content_type="text/markdown; charset=UTF-8; variant=GFM", #https://guides.github.com/features/mastering-markdown/
    maintainer=AUTHOR,
    maintainer_email=AUTHOR_EMAIL,

    # A string corresponding to distribution name of your package. This can be any name as long as only contains letters, numbers, _ , and -. It also must not already taken on pypi.org
    name=NAME,
    packages=find_packages(exclude=["docs", "tests*", "examples", ".gitignore", ".github", ".gitattributes", "README.md"]),# packages=[name]
    platforms = 'any',

    # A string corresponding to a version specifier (as defined in PEP 440) for the Python version, used to specify the Requires-Python defined in PEP 345.
    python_requires=">=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*", #python_requires=">=3.0, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*, !=3.6.*, !=3.7.*, !=3.8.*, <4",
    setup_requires=__getRequirements('dev'),

    # is the URL for the homepage of the project. For many projects, this will just be a link to GitHub, GitLab, Bitbucket, or similar code hosting service.
    url=URL,

    # A string corresponding the version of this release
    version=VERSION,

    # A boolean flag specifying whether the project can be safely installed and run from a zip file.
    zip_safe=False,

    # An arbitrary map of URL names to hyperlinks, allowing more extensible documentation of where various resources can be found than the simple url and download_url options provide.
    project_urls={
        "Documentation": "https://{}.readthedocs.io/en/stable/".format(NAME),
        "Discord: Support Server": "https://discord.gg/XkydRPS",
        #"Changelog": "https://{}.readthedocs.io/en/stable/news.html".format(NAME),
        "Github: Issues": URL + "/issues",#__getGithub("issues")
        "Say Thanks!": "https://saythanks.io/to/luissilva1044894",
    },
    tests_require=__getRequirements('dev'),
)
#python setup.py sdist bdist_wheel > create dist folder
#twine upload --repository-url https://test.pypi.org/legacy/ dist/* > upload test-pypi
#twine upload dist/* > upload pypi
#python setup.py sdit upload -r pypi > upload pypi
