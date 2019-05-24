<div  align="center">
<a href="https://github.com/luissilva1044894/Pyrez" title="Pyrez · Github repository" alt="Pyrez: Easiest way to connect to Hi-Rez Studios API!"><img src="https://raw.githubusercontent.com/luissilva1044894/Pyrez/gh-pages/assets/images/Pyrez.png" height="128" width="128"></a>

## Pyrez: Easiest way to connect to Hi-Rez Studios API
[![License](https://img.shields.io/github/license/luissilva1044894/Pyrez.svg?style=plastic&logoWidth=15)][license]
[![Contributors](https://img.shields.io/github/contributors/luissilva1044894/Pyrez.svg?style=plastic&logo=github&logoWidth=15)](https://github.com/luissilva1044894/Pyrez/graphs/contributors "Contributors")
[![PyPi Version](https://img.shields.io/pypi/v/pyrez.svg?style=plastic&logo=pypi&logoWidth=15)][pyrez-pypi]
[![Runtime Version](https://img.shields.io/pypi/pyversions/pyrez.svg?style=plastic&logo=python&logoWidth=15)][pyrez-pypi]
[![Discord Server](https://img.shields.io/discord/549020573846470659.svg?style=plastic&logo=discord&logoWidth=15)][support-server-discord]
[![Say Thanks!](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/luissilva1044894 "Say Thanks!")

[![CodeFactor](https://www.codefactor.io/repository/github/luissilva1044894/pyrez/badge)](https://www.codefactor.io/repository/github/luissilva1044894/pyrez "Pyrez · CodeFactor")
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/b3bb9e1efed0432ab923c11c2250089c)](https://www.codacy.com/app/luissilva1044894/Pyrez?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=luissilva1044894/Pyrez&amp;utm_campaign=Badge_Grade)
</div>

**Pyrez** is an [open-source](https://www.opensource.org "See http://www.opensource.org for the Open Source Definition") wrapper for [*Hi-Rez Studios*](https://www.hirezstudios.com "Hi-Rez Studios") API that supports [*Paladins*](https://www.paladins.com "Paladins Game"), [*Realm Royale*](https://www.realmroyale.com "Realm Royale Game") and [*Smite*](https://www.smitegame.com "Smite Game").

### Documentation
Official Documentation, which shows all available methods and how to use them: [**Click here!**](https://luissilva1044894.github.io/Pyrez/docs/ "Pyrez · Documentation")

### Support
If you need further help, join the official [*support server*][support-server-discord] on [Discord](https://discordapp.com/ "Discord App").

### Requirements
* [Python](https://python.org "Python.org") 2.7 or 3.x (3.4 or higher).
	* The following libraries are required: [`requests`](https://pypi.org/project/requests "requests").
* [Access](https://luissilva1044894.github.io/Pyrez/docs#registration "Form access to Hi-Rez Studios API") to Hi-Rez Studios API.

### Installation
> Pyrez currently isn't being updated on [PyPI][pyrez-pypi] and thus needs to be installed using git: <br/>`pip install -e git+https://github.com/luissilva1044894/pyrez.git@master#egg=pyrez`

The easiest way to install **Pyrez** is using `pip`, Python's package manager (or [pipenv](https://docs.pipenv.org), of course):

```bash
pip install pyrez
```
The required dependencies will be installed automatically.
After that, you can use the library using:
```py
import pyrez
```

### How to contribute
1. Become more familiar with the project by reading our [Contributor's Guide](./.github/CONTRIBUTING.md).
2.  Check for open issues or open a fresh issue to start a discussion around a feature idea or a bug.
3.  Fork [the repository][github-repo] on GitHub to start making your changes to the **master** branch (or branch off of it).
4.  Send a [pull request](https://help.github.com/en/articles/creating-a-pull-request-from-a-fork) and bug the maintainer until it gets merged and published. :) Make sure to add yourself to [AUTHORS](./AUTHORS.md).

### License
This project is provided under the MIT License, which you can view in [`LICENSE.md`][license]. You can do what you want with the code and, where possible, attribute back to the [GitHub page][github-repo].

All information obtained is provided by Hi-Rez Studios API and is thus their property. According to Section 11a of the [`API Terms of Use`][api-terms-of-use], you must attribute any data provided as below.

> Data provided by Hi-Rez. © 2019 Hi-Rez Studios, Inc. All rights reserved.

[api-terms-of-use]: https://www.hirezstudios.com/wp-content/themes/hi-rez-studios/pdf/api-terms-of-use-agreement.pdf "Hi-Rez Studios API · Terms of Use"
[github-repo]: https://github.com/luissilva1044894/Pyrez "Pyrez · Github repository"
[license]: ./LICENSE "Pyrez · License"
[pyrez-pypi]: https://pypi.org/project/pyrez "Pyrez · PyPI"
[support-server-discord]: https://discord.gg/XkydRPS "Support Server · Discord"
