# Pyrez: Easily way to connect to Hi-Rez API
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/luissilva1044894/Pyrez/blob/master/LICENSE)
[![Runtime Version](https://img.shields.io/pypi/pyversions/pyrez.svg)](https://pypi.org/project/pyrez)
[![Contributors](https://img.shields.io/github/contributors/luissilva1044894/Pyrez.svg)](https://github.com/luissilva1044894/Pyrez/graphs/contributors)


**PyRez** is an open-source Python-based wrapper for [Hi-Rez](http://www.hirezstudios.com "Hi-Rez Studios") API that supports *[Paladins](https://www.paladins.com "Paladins Game")*, *[Realm Royale](https://github.com/apugh/realm-api-proposal/wiki "Realm Royale API Documentation")* and *[Smite](https://www.smitegame.com "Smite Game")*.

## Requirements
* [Python](http://python.org "Python.org") 3.5(or higher).
    * The following libraries are required: [`Requests`](https://pypi.org/project/requests "requests") and `requests-aeaweb`.
- [Access](https://fs12.formsite.com/HiRez/form48/secure_index.html "Form access to Hi-Rez API") to Hi-Rez Studios API.

## Installation
The easiest way to install **Pyrez** is using `pip`, Python's package manager:

```
pip install -e git+https://github.com/luissilva1044894/pyrez.git@master#egg=pyrez
```
The required dependencies will be installed automatically.
After that, you can use the library using:
```py
import pyrez
```

