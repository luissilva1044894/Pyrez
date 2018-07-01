# PyRez

**PyRez** is Python-based wrapper for [Hi-Rez](http://www.hirezstudios.com/) API that supports *[Paladins](https://www.paladins.com)*, *[Realm Royale](https://store.steampowered.com/app/813820/Realm_Royale)* and *[Smite](https://www.smitegame.com)*.

## Requirements
* [Python](http://python.org) 3.5 (or higher)
    * The following libraries are required: `requests` and `requests-aeaweb`
- [Access](https://fs12.formsite.com/HiRez/form48/secure_index.html) to Hi-Rez Studios' API

Detailed documentation is in the "docs" directory.

## Installation
The easiest way to install **Py-rez** is using `pip`, Python's package manager:

```
pip install -U pyrez
```

The required dependencies will be installed automatically. After that, you can use the library using `import pyrez`.

## Example

```py
from pyrez.api import PaladinsAPI

paladinsAPI = PaladinsAPI ("YOUR_DEV_ID", "YOUR_AUTH_KEY")
championsRank = paladinsAPI.getGodRanks ("FeyRazzle")

if championsRank is not None:
    for championRank in championsRank:
        print(championRank.getWinratio ())
```

This example will print the winrate with every [Champions](https://www.paladins.com/champions) of player **[FeyRazzle](https://twitch.tv/FeyRazzle "FeyRazzle")**.
