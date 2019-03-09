# Pyrez: Easily way to connect to Hi-Rez API
[![License](https://img.shields.io/badge/license-MIT-green.svg)](./LICENSE)
[![Runtime Version](https://img.shields.io/pypi/pyversions/pyrez.svg)](https://pypi.org/project/pyrez)
[![Contributors](https://img.shields.io/github/contributors/luissilva1044894/Pyrez.svg)](https://github.com/luissilva1044894/Pyrez/graphs/contributors)


**PyRez** is an open-source Python-based wrapper for [Hi-Rez](http://www.hirezstudios.com "Hi-Rez Studios") API that supports *[Paladins](https://www.paladins.com "Paladins Game")*, *[Realm Royale](https://www.realmroyale.com "Realm Royale Game")* and *[Smite](https://www.smitegame.com "Smite Game")*.

### Documentation
Official Documentation: [**Click here!**](./docs)

### Support
For support using Pyrez, please join the official [*support server*](
https://discord.gg/XkydRPS) on [Discord](https://discordapp.com/ "Discord App")

### Requirements
* [Python](http://python.org "Python.org") 3.5(or higher).
    * The following libraries are required: [`Requests`](https://pypi.org/project/requests "requests") and `requests-aeaweb`.
- [Access](./docs#registration "Form access to Hi-Rez API") to Hi-Rez Studios API.

### Installation
Pyrez currently isn't being updated on [PyPI](https://pypi.org/project/pyrez) and thus needs to be installed using git. The easiest way to install **Pyrez** is using `pip`, Python's package manager:

```
pip install -e git+https://github.com/luissilva1044894/pyrez.git@master#egg=pyrez
```
The required dependencies will be installed automatically.
After that, you can use the library using:
```py
import pyrez
```

### Contributors
- [@shaklev](https://github.com/shaklev)

### License
This project is licensed under [MIT](./LICENSE)