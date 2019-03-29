## Pyrez: Easiest way to connect to Hi-Rez Studios' API
[![License](https://img.shields.io/github/license/luissilva1044894/Pyrez.svg?style=plastic&logoWidth=15)](./LICENSE "Pyrez License")
[![Contributors](https://img.shields.io/github/contributors/luissilva1044894/Pyrez.svg?style=plastic&logo=github&logoWidth=15)](https://github.com/luissilva1044894/Pyrez/graphs/contributors "Contributors")
[![PyPi Version](https://img.shields.io/pypi/v/pyrez.svg?style=plastic&logo=pypi&logoWidth=15)](https://pypi.org/project/pyrez "Pyrez · PyPI (Outdated)")
[![Runtime Version](https://img.shields.io/pypi/pyversions/pyrez.svg?style=plastic&logo=python&logoWidth=15)](https://pypi.org/project/pyrez "Python Runtime Versions")
[![Discord Server](https://img.shields.io/discord/549020573846470659.svg?style=plastic&logo=discord&logoWidth=15)](https://discord.gg/XkydRPS "Pyrez Discord Server")
[![Say Thanks!](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/luissilva1044894 "Say Thanks!")

[![CodeFactor](https://www.codefactor.io/repository/github/luissilva1044894/pyrez/badge)](https://www.codefactor.io/repository/github/luissilva1044894/pyrez "CodeFactor - Pyrez")
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/b3bb9e1efed0432ab923c11c2250089c)](https://www.codacy.com/app/luissilva1044894/Pyrez?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=luissilva1044894/Pyrez&amp;utm_campaign=Badge_Grade)

**Pyrez** is an open-source Python-based wrapper for [*Hi-Rez Studios*](http://www.hirezstudios.com "Hi-Rez Studios")' API that supports [*Paladins*](https://www.paladins.com "Paladins Game"), [*Realm Royale*](https://www.realmroyale.com "Realm Royale Game") and [*Smite*](https://www.smitegame.com "Smite Game").

### Documentation
Official Documentation, which shows all available methods and how to use them: [**Click here!**](./docs "Pyrez Documentation")

### Support
For support using Pyrez, please join the official [*support server*](
https://discord.gg/XkydRPS "Pyrez Discord Server") on [Discord](https://discordapp.com/ "Discord App")

### Requirements
* [Python](http://python.org "Python.org") 3.x (3.4 or higher).
	* The following libraries are required: [`Requests`](https://pypi.org/project/requests "requests") and `requests-aeaweb`.
* [Access](./docs#registration "Form access to Hi-Rez API") to Hi-Rez Studios' API.

### Installation
Pyrez currently isn't being updated on [PyPI](https://pypi.org/project/pyrez "Pyrez · PyPI (Outdated)") and thus needs to be installed using git. The easiest way to install **Pyrez** is using `pip`, Python's package manager:

```
pip install -e git+https://github.com/luissilva1044894/pyrez.git@master#egg=Pyrez
```
The required dependencies will be installed automatically.
After that, you can use the library using:
```py
import pyrez
```

### Contributors
 * [`@shaklev`](https://github.com/shaklev "Aleksandar")
 * [`@Rabrg`](https://github.com/Rabrg "Ryan Greene")
 * [`@EthanHicks1`](https://github.com/EthanHicks1 "Ethan Hicks")

### License
This project is provided under the MIT License, which you can view in [`LICENSE.md`](./LICENSE "Pyrez License"). You can do what you want with the code and, where possible, attribute back to the [GitHub page](https://github.com/luissilva1044894/Pyrez "Pyrez Github repository").

All information obtained is provided by Hi-Rez Studios' API and is thus their property. According to Section 11a of the [`API Terms of Use`](https://www.hirezstudios.com/wp-content/themes/hi-rez-studios/pdf/api-terms-of-use-agreement.pdf "Hi-Rez Studios' API - Terms of Use"), you must attribute any data provided as below.

> Data provided by Hi-Rez. © 2019 Hi-Rez Studios, Inc. All rights reserved.
