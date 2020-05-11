<div  align="center">
<a href="https://github.com/luissilva1044894/Pyrez" title="Pyrez · Github repository" alt="Pyrez: Easiest way to connect to Hi-Rez Studios API!"><img src="https://raw.githubusercontent.com/luissilva1044894/Pyrez/gh-pages/assets/images/Pyrez.png" height="128" width="128"></a>

## Pyrez: Easiest way to connect to Hi-Rez Studios API
[![License](https://img.shields.io/github/license/luissilva1044894/Pyrez.svg?style=plastic&logoWidth=15)][license]
[![Documentation Status](https://readthedocs.org/projects/pyrez/badge/?version=stable)](https://pyrez.readthedocs.io/en/stable/?badge=stable)
[![PyPi Version](https://img.shields.io/pypi/v/pyrez.svg?style=plastic&logo=pypi&logoWidth=15)][pyrez-pypi]
[![Runtime Version](https://img.shields.io/pypi/pyversions/pyrez.svg?style=plastic&logo=python&logoWidth=15&logoColor=white)][pyrez-pypi]

[![Discord Server](https://img.shields.io/discord/549020573846470659.svg?style=plastic&logo=discord&logoWidth=15)][support-server-discord]
[![Contributors](https://img.shields.io/github/contributors/luissilva1044894/Pyrez.svg?style=plastic&logo=github&logoWidth=15)](https://github.com/luissilva1044894/Pyrez/graphs/contributors "Contributors")
[![CodeFactor](https://www.codefactor.io/repository/github/luissilva1044894/pyrez/badge/1.1.x)](https://www.codefactor.io/repository/github/luissilva1044894/pyrez/overview/1.1.x "Pyrez · CodeFactor")
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/b3bb9e1efed0432ab923c11c2250089c)](https://www.codacy.com/app/luissilva1044894/Pyrez?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=luissilva1044894/Pyrez&amp;utm_campaign=Badge_Grade)
[![Say Thanks!](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/luissilva1044894 "Say Thanks!")

Built with [![Python](https://img.shields.io/badge/Python-3.7.7-blue.svg?style=plastic&logo=python&logoWidth=15&logoColor=white)](https://docs.python.org/3.7/whatsnew/changelog.html#python-3-7-7-final "Python 3.7.7")
[![requests](https://img.shields.io/badge/requests-2.23.0-orange.svg?style=plastic)](https://pypi.org/project/requests/2.23.0/ "requests 2.23")

> [**`(A)SYNC` BRANCH** (unstable)](https://github.com/luissilva1044894/Pyrez/tree/master)

</div>

**Pyrez** is an easy to use synchronous wrapper for [*Hi-Rez Studios*](https://www.hirezstudios.com "Hi-Rez Studios") API that supports [*Paladins*](https://www.paladins.com "Paladins Game"), [*Realm Royale*](https://www.realmroyale.com "Realm Royale Game") and [*Smite*](https://www.smitegame.com "Smite Game").

### Key Features
 * Entire coverage of Hi-Rez Studios API endpoints.
 * Easy to use with an object oriented design.

<a href="https://github.com/luissilva1044894/pyrez" title="Pyrez" target="_blank">
  <img alt="Pyrez" src="https://img.shields.io/badge/Using-Pyrez-00bb88.svg?logo=python&logoWidth=20&logoColor=white&style=plastic">
</a>
<details markdown="1">
<summary>Use this badge in your project's Readme to show you're using <code>Pyrez</code>! The markdown code is below...</summary>

```markdown hl_lines="7 12"
[![Pyrez](https://img.shields.io/badge/Using-Pyrez-00bb88.svg?logo=python&logoWidth=20&logoColor=white&style=plastic)](https://github.com/luissilva1044894/pyrez)
```

</details>

### Requirements
 * [Access](https://pyrez.readthedocs.io/en/stable/getting_started.html#registration "Form access to Hi-Rez Studios API") to Hi-Rez Studios API.
 * [Python](https://www.python.org/) - 2.7, 3.5, 3.6, & 3.7, & 3.8 are supported.
 * [requests](https://2.python-requests.org/en/stable/) - 2.0 or greater.

### Documentation
Documentation is being hosted on Read the Docs, which shows all available methods and how to use them: [**Click here!**](https://pyrez.readthedocs.io/en/stable/ "Pyrez · Documentation")

### Support
If you need further help, please join the official [*support server*][support-server-discord] on [Discord](https://discordapp.com/ "Discord App").

### Installation
The easiest way to install the latest stable version is by using pip/easy_install (or [`pipenv`](https://docs.pipenv.org), of course) to pull it from [`PyPI`](https://pypi.org "Python's package manager ") by running the following command:

```py
pip install pyrez
```

You may also use git to clone the development version from [GitHub][github-repo] and install it manually:

```py
git clone https://github.com/luissilva1044894/pyrez.git
cd pyrez
python setup.py install
```

The required dependencies will be installed automatically.
Then, to use these functions, you must import the `pyrez` package:
```py
import pyrez
```

### How to use

```py
import pyrez

fake_dev_id=1004
fake_auth_key='23DF3C7E9BD14D84BF892AD206B6755C'

def main():
    with pyrez.PaladinsAPI(fake_dev_id, fake_auth_key) as paladins:
        print(paladins.getDataUsed())

if __name__ == "__main__":
	main()
```

### Application Example

 * [FlaskPyrezAPI](https://github.com/luissilva1044894/FlaskPyrezAPI) - Example of a web application using Flask and Pyrez.

### How to contribute
1. Become more familiar with the project by reading our [Contributor's Guide](./.github/CONTRIBUTING.md).
2. Check for open issues or open a fresh issue to start a discussion around a feature idea or a bug.
3. Fork [the repository][github-repo] on GitHub to start making your changes to the **master** branch (or branch off of it).
4. Send a [pull request](https://help.github.com/en/articles/creating-a-pull-request-from-a-fork) and bug the maintainer until it gets merged and published. :) Make sure to add yourself to [AUTHORS](./AUTHORS.md).

### License
> I reserve the right to place future versions of this library under a different license. But if you make any changes or additions to Pyrez itself, those must be released with a compatible license.
> Basically it means that you can do whatever you want with the code and, where possible, attribute back to the [GitHub page][github-repo].

This is an open source [![Open Source](https://raw.githubusercontent.com/abhishekbanthia/Public-APIs/master/opensource.png)](https://www.opensource.org "See http://www.opensource.org for the Open Source Definition") project provided under the MIT License, which can be found in the [`LICENSE file`][license]. The programs in the “[examples](./examples)” subdirectory are in the public domain.

Third-party libraries used by Pyrez are under their own licenses. Please refer to those libraries for details on the license they use.

All information obtained is provided by Hi-Rez Studios API and is thus their property. According to Section 11a of the [`API Terms of Use`][api-terms-of-use], you must attribute any data provided as below.

> Data provided by Hi-Rez. © 2020 Hi-Rez Studios, Inc. All rights reserved.

[api-terms-of-use]: https://www.hirezstudios.com/wp-content/themes/hi-rez-studios/pdf/api-terms-of-use-agreement.pdf "Hi-Rez Studios API · Terms of Use"
[github-repo]: https://github.com/luissilva1044894/Pyrez "Pyrez · Github repository"
[license]: ./LICENSE "Pyrez · License"
[pyrez-pypi]: https://pypi.org/project/pyrez "Pyrez · PyPI"
[support-server-discord]: https://discord.gg/XkydRPS "Support Server · Discord"
