# PyRez
[![Documentation Status](https://readthedocs.org/projects/pyrez/badge/?version=latest)](http://pyrez.readthedocs.io/en/latest/?badge=latest)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/luissilva1044894/Pyrez/blob/master/LICENSE)


**PyRez** is an open-source Python-based wrapper for [Hi-Rez](http://www.hirezstudios.com/) API that supports *[Paladins](https://www.paladins.com)*, *[Realm Royale](https://github.com/apugh/realm-api-proposal "Realm Royale API Documentation)* and *[Smite](https://www.smitegame.com)*.

## Requirements
* [Python](http://python.org) 3.5 (or higher)
    * The following libraries are required: [`Requests`](https://pypi.org/project/requests "requests") and `requests-aeaweb`
- [Access](https://fs12.formsite.com/HiRez/form48/secure_index.html) to Hi-Rez Studios' API

Detailed documentation is in the "docs" directory.

## Installation
The easiest way to install **Pyrez** is using `pip`, Python's package manager:

```
pip install -U pyrez
```
Or:
```
pip install -U https://github.com/luissilva1044894/Pyrez/blob/master/releases/pyrez-x.y.z.tar.gz?raw=true
```
The required dependencies will be installed automatically. After that, you can use the library using `import pyrez`.

## Example

```py
from pyrez.api import PaladinsAPI

paladinsAPI = PaladinsAPI (devId=1004, authKey="23DF3C7E9BD14D84BF892AD206B6755C")
championsRank = paladinsAPI.getGodRanks ("FeyRazzle")

if championsRank is not None:
    for championRank in championsRank:
        print(championRank.getWinratio ())
```

This example will print the winrate with every [Champions](https://www.paladins.com/champions) of player **[FeyRazzle](https://twitch.tv/FeyRazzle "FeyRazzle")**.
