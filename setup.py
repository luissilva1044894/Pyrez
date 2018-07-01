import os
from setuptools import find_packages, setup

with open(os.path.join (os.path.dirname(__file__), "README.md"), "r") as readme:
    README = readme.read ()

#requirements = []
#with open ("requirements.txt") as f:
    #requirements = f.read ().splitlines ()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    author="Luís (Lugg) Gustavo",
    author_email="luis.silva.1044894@sga.pucminas.br",
    classifiers=[
        'Development Status :: 3 - Alpha', #'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet',
        'Topic :: Internet :: WWW/HTTP',
        #'Topic :: Games/Entertainment',
        #'Topic :: Games/Entertainment :: First Person Shooters',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    description="A Python-based wrapper for Hi-Rez API",
    include_package_data=True,
    install_requires=[
        'requests>=2.18.4',
        'requests-aeaweb>=0.0.1'
    ],
    keywords=['hirez hi-rez smite paladins realmapi open-source api wrapper library'],
    license="MIT",
    long_description=README,
    name="pyrez",
    packages=find_packages(), #packages=[name]
    url="https://github.com/luissilva1044894/PyRez",
    version="0.8.5",
)
