<div  align="center">
<a href="https://github.com/luissilva1044894/Pyrez" title="Pyrez · Github repository" alt="Pyrez: Easiest way to connect to Hi-Rez Studios API!"><img src="https://raw.githubusercontent.com/luissilva1044894/Pyrez/gh-pages/assets/images/Pyrez.png" height="128" width="128"></a>

# Pyrez: Easiest way to connect to Hi-Rez Studios API :snake:

> :construction: **It's a work in progress, still undergoing some change, documentation is in-progress, and may be unstable.**

[![License][bagde-license]][license]
[![Documentation Status][bagde-documentation]][pyrez-documentation]
[![Runtime Version][bagde-runtime-version]][pyrez-pypi]

[![Discord Server][bagde-discord-server]][support-server-discord]
[![Contributors][bagde-contributors]](https://github.com/luissilva1044894/Pyrez/graphs/contributors "Contributors")
[![Requirements Status][bagde-requirements]](https://requires.io/github/luissilva1044894/Pyrez/requirements/?branch=master)
[![Say Thanks!][bagde-say-thanks]](https://saythanks.io/to/luissilva1044894 "Say Thanks!")

Built with: [![Python][badgde-python]][python-3-7]
[![requests][bagde-requests]](https://pypi.org/project/requests/2.22.0/ "requests 2.22")
[![aiohttp][bagde-aiohttp]](https://pypi.org/project/aiohttp/3.6.2/ "aiohttp 3.6.2")

</div>

> If you are currently using this project, please ⭐️ this [repository][github-repo]!

**Pyrez** is an easy to use (a)synchronous wrapper for [*Hi-Rez Studios*][hi-rez-studios] API that supports [*Paladins*][paladins-game], [*Realm Royale*][realm-royale] and [*Smite*][smite-game].

<a href="https://github.com/luissilva1044894/pyrez" title="Pyrez" target="_blank">
  <img alt="Pyrez" src="https://img.shields.io/badge/Using-Pyrez-00bb88.svg?logo=python&logoColor=white&logoWidth=20&style=plastic">
</a>
<details markdown="1">
<summary>If you are currently using this, you may include this badge in your project's Readme to let people know that you are using <code>Pyrez</code>!<br/>The markdown code is below...</summary>

```markdown hl_lines="7 12"
[![Pyrez](https://img.shields.io/badge/Using-Pyrez-00bb88.svg?logo=python&logoColor=white&logoWidth=20&style=plastic)](https://github.com/luissilva1044894/pyrez)
```

</details>

### Key Features :gem:
 * Entire coverage of [Hi-Rez Studios API endpoints][hi-rez-studios-developer-guide], supporting all games and their platforms.
 * Support both [Python 2.7][python-2] and [Python 3.5+][python-3].
 * Use the same client for sync and async ([PEP 492](https://www.python.org/dev/peps/pep-0492/)) usage.
 * Easy to use with an object oriented design.

### Description & Philosophy :coffee:
> **Disclaimer**: This project, including this repository, is neither created, affiliated, associated nor endorsed by Hi-Rez Studios, or any of its subsidiaries or its affiliates. It is created by the community for the community. Please refrain from contacting Hi-Rez Studios regarding any issues or support of this project, instead feel free to submit an issue.

The purpose of this project is to expose and simplify the interacting with Hi-Rez Studios API for third party and/or individual standalone projects, without the headache of learning the ins and outs of API authentication and structure.

I encourage developers to look into the codebase to better understand this wrapper and what it can truly offer.

 * Rapidly begin interacting with the API, no more always having to write tedious code.
 * Low number of dependencies: Installing and using is simple as possible, without having to deal with long dependency chains.
 * Avoid useless API calls, such as `/createsession` every 15 minutes, keeping your requests low.

#### Mantainance 🛠
> :warning: Sometimes the API updates whenever necessary and often the developers don't specify when or why these changes are taking place. Due to this, note that any feature could break at any time if the API gets updated in a way this project depends on. If a break does occur, please open up an issue detailing the error, we will try to patch these issues as quickly as we can when they arrise.

As long as Hi-Rez Studios doesn't change its APIs simpliest functions won't be changed. However, functions could be updated, added or removed until it's in a very clear and stable state.

#### Documentation & Support :book:
The Sphinx-compiled documentation, which shows all available methods and how to use them, is being hosted on [**Read the Docs**][pyrez-documentation]!

If you have any questions, concerns, need further help, want to be up-to-date on, or like interested to contribute in any way or mantaining this project, please join the official [*support server*][support-server-discord] on [Discord][discord].

### Requirements
 * Requires the Credentials necessary to interating with Hi-Rez Studios API. For more information, [click here](https://pyrez.readthedocs.io/en/latest/getting_started.html#registration "Form access to Hi-Rez Studios API").
 * [Python](https://www.python.org/) - 2.7, 3.5, 3.6, & 3.7 are supported.
 * Dependencies
 	* [requests](https://github.com/kennethreitz/requests/ "Python HTTP Requests for Humans") - 2.0 or greater.
 	* [aiohttp](https://github.com/aio-libs/aiohttp/) - 2.0 or higher.
 	* Optional Dependencies
 	 	* [simplejson](https://github.com/simplejson/simplejson) - for faster JSON "parsing".

### Installation 📦
> This project is intended to be run on 2.7.x or newer.

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
Then, to use these functions, you must import the package:

```py
import pyrez
```

#### How to use
More complete examples can be found in the [examples][examples-folder] folder.

Synchronous (blocks until data is fully returned)
```py
import pyrez

fake_dev_id=1004
fake_auth_key='23DF3C7E9BD14D84BF892AD206B6755C'

def main():
    with pyrez.PaladinsAPI(fake_dev_id, fake_auth_key) as paladins:
        print(paladins.getDataUsed())

if __name__ == '__main__':
	main()
```

<details markdown="1">
<summary>Asynchronous (non-blocking)</summary>
If your code uses <code>async</code> / <code>await</code>, use <code>async def</code>:

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

#### Application Example

 * [FlaskPyrezAPI](https://github.com/luissilva1044894/FlaskPyrezAPI) - Example of a web application using Flask and Pyrez.
 * [PyrezBot](https://github.com/luissilva1044894/PyrezBot) - Async example of a [Discord][discord] bot using Pyrez.

### How to contribute :octocat:

Feel free to contribute to this project, a helping hand is always appreciated.

 1. Become more familiar with the project by reading through our [Contributor's Guide](./.github/CONTRIBUTING.md) first.
 2. Check for open issues or open a fresh issue to start a discussion around a feature idea or a bug.
 3. Fork [the repository][github-repo] on GitHub to start making your changes to the **master** branch (or branch off of it).
 4. Send a [pull request](https://help.github.com/en/articles/creating-a-pull-request-from-a-fork) and bug the maintainer until it gets merged and published. :) Make sure to add yourself to [AUTHORS](./AUTHORS.md).

### Copyright & License 📝

> I reserve the right to place future versions of this library under a different license. <br/>If you make any changes or additions to Pyrez itself, then it must be released under this same license, make it open source, and provide documentation of changes made.

This is a free, open source [![Open Source][open-source-icon]][open-source-definition], and GPL friendly project. Full license can be found in the [`LICENSE`][license] file. You can use it for commercial, non-commercial or open source projects, or really almost whatever you want and by any means. All versions must have copyright credit pointing back to this [GitHub page][github-repo]. The programs in the “[examples][examples-folder]” subdirectory are in the public domain unless specified otherwise.

Please note, however, that this license does NOT cover third-party libraries used by Pyrez, they are under their own licenses. Please refer to those libraries for details on the license they use.

All information obtained is provided by Hi-Rez Studios API and is thus their property. According to Section 11a of the [`API Terms of Use`][api-terms-of-use], you must attribute any data provided as below.

> Data provided by Hi-Rez. © 2019 Hi-Rez Studios, Inc. All rights reserved.

### Quick Links :link:

 * [GitHub Page][github-repo]
 * [Documentation][pyrez-documentation]
 * [License][license]
 * [Issue Tracker](https://github.com/luissilva1044894/Pyrez/issues)
 * [API Reference][hi-rez-studios-developer-guide]

[api-terms-of-use]: https://www.hirezstudios.com/wp-content/themes/hi-rez-studios/pdf/api-terms-of-use-agreement.pdf "Hi-Rez Studios API · Terms of Use"
[bagde-aiohttp]: https://img.shields.io/badge/aiohttp-3.6.2-orange.svg?logo=pypi&logoColor=white&style=plastic
[bagde-contributors]: https://img.shields.io/github/contributors/luissilva1044894/Pyrez.svg?logo=github&logoWidth=15&style=plastic
[bagde-discord-server]: https://img.shields.io/discord/549020573846470659.svg?logo=discord&logoColor=white&logoWidth=15&style=plastic
[bagde-documentation]: https://img.shields.io/readthedocs/pyrez/latest.svg?logo=read-the-docs&logoColor=white&style=plastic
[bagde-license]: https://img.shields.io/pypi/l/pyrez.svg?logo=github&logoWidth=15&style=plastic
[badgde-python]: https://img.shields.io/badge/Python-3.7.5-orange.svg?logo=python&logoColor=white&style=plastic
[bagde-requests]: https://img.shields.io/badge/requests-2.22.0-orange.svg?logo=pypi&logoColor=white&style=plastic
[bagde-requirements]: https://requires.io/github/luissilva1044894/Pyrez/requirements.svg?branch=master
[bagde-runtime-version]: https://img.shields.io/pypi/pyversions/pyrez.svg?logo=python&logoColor=white&logoWidth=15&style=plastic
[bagde-say-thanks]: https://img.shields.io/badge/Say%20Thanks!-🦉-1EAEDB.svg
[discord]: https://discordapp.com/ "Discord App"
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
[python-3]: https://docs.python.org/3/whatsnew/index.html "What’s New In Python 3.x · Changes in Python Behavior"
[python-3-7]: https://docs.python.org/3.7/whatsnew/changelog.html#python-3-7-5-final "Built and Tested on Python 3.7.5"
[realm-royale]: https://www.realmroyale.com "Realm Royale Game"
[smite-game]: https://www.smitegame.com "Smite Game"
[support-server-discord]: https://discord.gg/XkydRPS "Support Server · Discord"
