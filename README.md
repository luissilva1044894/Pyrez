<div  align="center">
<a href="https://github.com/luissilva1044894/Pyrez" title="Pyrez · Github repository" alt="Pyrez: Easiest way to connect to Hi-Rez Studios API!"><img src="https://raw.githubusercontent.com/luissilva1044894/Pyrez/gh-pages/assets/images/Pyrez.png" height="128" width="128"></a>

## Pyrez: Easiest way to connect to Hi-Rez Studios API :snake:

> :warning: **It's a work in progress, still undergoing some change, documentation is in-progress, and may be un[stable][github-repo].**

[![License][bagde-license]][license]
[![Documentation Status][bagde-documentation]][pyrez-documentation]
[![Runtime Version][bagde-runtime-version]][pyrez-pypi]

[![Discord Server][bagde-discord-server]][support-server-discord]
[![Contributors][bagde-contributors]](https://github.com/luissilva1044894/Pyrez/graphs/contributors "Contributors")
[![Requirements Status][bagde-requirements]](https://requires.io/github/luissilva1044894/Pyrez/requirements/?branch=master)
[![Say Thanks!][bagde-say-thanks]](https://saythanks.io/to/luissilva1044894 "Say Thanks!")

Built with: [![Python][badgde-python]][python-3-7]
[![requests][bagde-requests]](https://pypi.org/project/requests/2.22.0/ "requests 2.22")
[![aiohttp][bagde-aiohttp]](https://pypi.org/project/aiohttp/3.5.4/ "aiohttp 3.5.4")

</div>

**Pyrez** is an easy to use (a)synchronous wrapper for [*Hi-Rez Studios*][hi-rez-studios] API that supports [*Paladins*][paladins-game], [*Realm Royale*][realm-royale] and [*Smite*][smite-game].

<a href="https://github.com/luissilva1044894/pyrez" title="Pyrez" target="_blank">
  <img alt="Pyrez" src="https://img.shields.io/badge/Using-Pyrez-00bb88.svg?logo=python&logoColor=white&logoWidth=20&style=plastic">
</a>
<details markdown="1">
<summary>If you use Pyrez, you can include this badge in your project's Readme to let people know that you are using <code>Pyrez</code>!<br/>The markdown code is below...</summary>

```markdown hl_lines="7 12"
[![Pyrez](https://img.shields.io/badge/Using-Pyrez-00bb88.svg?logo=python&logoColor=white&logoWidth=20&style=plastic)](https://github.com/luissilva1044894/pyrez)
```

</details>

### Key Features
 * Support both [Python 2.7.x][python-2] and [Python 3.x][python-3].
 * Entire coverage of [Hi-Rez Studios API endpoints][hi-rez-studios-developer-guide].
 * Use the same client for sync and async ([PEP 492](https://www.python.org/dev/peps/pep-0492/)) usage.
 * Easy to use with an object oriented design.

### Requirements
 * [Access](https://pyrez.readthedocs.io/en/latest/getting_started.html#registration "Form access to Hi-Rez Studios API") to Hi-Rez Studios API.

#### Dependencies
 * [Python](https://www.python.org/) - 2.7, 3.5, 3.6, & 3.7 are supported.
 * [requests](https://github.com/kennethreitz/requests/) - 2.0 or greater.
 * [aiohttp](https://github.com/aio-libs/aiohttp/) - 2.0 or higher.

### Installation 📦
The easiest way to install the latest stable version is by using [pip](http://www.pip-installer.org/en/latest/)/[easy_install](https://setuptools.readthedocs.io/en/latest/easy_install.html) (or [`pipenv`](https://docs.pipenv.org), of course) to pull it from [`PyPI`](https://pypi.org "Python's package manager") by running the following command:

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

### Documentation :book:
Documentation is being hosted on [**Read the Docs**][pyrez-documentation], which shows all available methods and how to use them!

### Support
If you need further help, please join the official [*support server*][support-server-discord] on [Discord](https://discordapp.com/ "Discord App").

### How to use
More complete examples can be found in the [examples][examples-folder] folder.

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

<details markdown="1">
<summary>Or use <code>async def</code>...</summary>

If your code uses `async` / `await`, use `async def`:

```python hl_lines="7 12"
async def main(dev_id, auth_key):
   import pyrez
   async with pyrez.PaladinsAPI.Async(dev_id, auth_key) as paladins:
      print(await paladins.getDataUsed())

import asyncio

fake_dev_id=1004
fake_auth_key='23DF3C7E9BD14D84BF892AD206B6755C'

loop = asyncio.get_event_loop()
loop.run_until_complete(main(fake_dev_id, fake_auth_key))
```

</details>

### Application Example

 * [FlaskPyrezAPI](https://github.com/luissilva1044894/FlaskPyrezAPI) - Example of a web application using Flask and Pyrez.
 * [PyrezBot](https://github.com/luissilva1044894/PyrezBot) - Async example of a Discord bot using Pyrez.

### How to contribute :octocat:

Feel free to contribute to this project, a helping hand is always appreciated.

 1. Become more familiar with the project by reading through our [Contributor's Guide](./.github/CONTRIBUTING.md) first.
 2. Check for open issues or open a fresh issue to start a discussion around a feature idea or a bug.
 3. Fork [the repository][github-repo] on GitHub to start making your changes to the **master** branch (or branch off of it).
 4. Send a [pull request](https://help.github.com/en/articles/creating-a-pull-request-from-a-fork) and bug the maintainer until it gets merged and published. :) Make sure to add yourself to [AUTHORS](./AUTHORS.md).

### Misc

If you are currently using this project, please ⭐️ this [repository][github-repo]!

If you would like to help, just let us know in our [*support server*][support-server-discord]! :heart:

### Copyright & License 📝

> I reserve the right to place future versions of this library under a different license. <br/>If you make any changes or additions to Pyrez itself, those must be released with a compatible license.

This is a free, open source [![Open Source][open-source-icon]][open-source-definition], and GPL friendly project. Full license can be found in the [`LICENSE file`][license]. You can use it for commercial or non-commercial projects, open source projects, or really almost whatever you want and by any means. And, where possible, attribute back to the [GitHub page][github-repo]. The programs in the “[examples][examples-folder]” subdirectory are in the public domain unless specified otherwise.

Please note, however, that this license does NOT cover third-party libraries used by Pyrez, they are under their own licenses. Please refer to those libraries for details on the license they use.

All information obtained is provided by Hi-Rez Studios API and is thus their property. According to Section 11a of the [`API Terms of Use`][api-terms-of-use], you must attribute any data provided as below.

> Data provided by Hi-Rez. © 2019 Hi-Rez Studios, Inc. All rights reserved.

[api-terms-of-use]: https://www.hirezstudios.com/wp-content/themes/hi-rez-studios/pdf/api-terms-of-use-agreement.pdf "Hi-Rez Studios API · Terms of Use"
[bagde-aiohttp]: https://img.shields.io/badge/aiohttp-3.5.4-orange.svg?logo=pypi&logoColor=white&style=plastic
[bagde-contributors]: https://img.shields.io/github/contributors/luissilva1044894/Pyrez.svg?logo=github&logoWidth=15&style=plastic
[bagde-discord-server]: https://img.shields.io/discord/549020573846470659.svg?logo=discord&logoColor=white&logoWidth=15&style=plastic
[bagde-documentation]: https://img.shields.io/readthedocs/pyrez/latest.svg?logo=read-the-docs&logoColor=white&style=plastic
[bagde-license]: https://img.shields.io/github/license/luissilva1044894/Pyrez.svg?logo=github&logoWidth=15&style=plastic
[badgde-python]: https://img.shields.io/badge/Python-3.7.3-orange.svg?logo=python&logoColor=white&style=plastic
[bagde-requests]: https://img.shields.io/badge/requests-2.22.0-orange.svg?logo=pypi&logoColor=white&style=plastic
[bagde-requirements]: https://requires.io/github/luissilva1044894/Pyrez/requirements.svg?branch=master
[bagde-runtime-version]: https://img.shields.io/pypi/pyversions/pyrez.svg?logo=python&logoColor=white&logoWidth=15&style=plastic
[bagde-say-thanks]: https://img.shields.io/badge/Say%20Thanks!-🦉-1EAEDB.svg
[examples-folder]: ./examples
[github-repo]: https://github.com/luissilva1044894/Pyrez "Pyrez · Github repository"
[hi-rez-studios]: https://www.hirezstudios.com "Hi-Rez Studios"
[hi-rez-studios-developer-guide]: https://docs.google.com/document/d/1OFS-3ocSx-1Rvg4afAnEHlT3917MAK_6eJTR6rzr-BM/edit "Hi-Rez Studios API · Developer Guide"
[license]: ./LICENSE "Pyrez · License"
[open-source-definition]: https://www.opensource.org "See http://www.opensource.org for the Open Source Definition"
[open-source-icon]: https://raw.githubusercontent.com/abhishekbanthia/Public-APIs/master/opensource.png
[paladins-game]: https://www.paladins.com "Paladins Game"
[pyrez-pypi]: https://pypi.org/project/pyrez "Pyrez · PyPI"
[pyrez-documentation]: https://pyrez.readthedocs.io/en/latest/ "Pyrez · Documentation"
[python-2]: https://docs.python.org/2.7/ "Python 2.7.x"
[python-3]: https://docs.python.org/3/whatsnew/index.html "Python 3.x"
[python-3-7]: https://docs.python.org/3.7/whatsnew/changelog.html#python-3-7-3-final "Python 3.7.3"
[realm-royale]: https://www.realmroyale.com "Realm Royale Game"
[smite-game]: https://www.smitegame.com "Smite Game"
[support-server-discord]: https://discord.gg/XkydRPS "Support Server · Discord"
