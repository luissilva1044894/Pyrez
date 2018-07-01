# PyRez

**PyRez** is Python-based wrapper for [Hi-Rez](http://www.hirezstudios.com) API that supports *[Paladins](https://www.paladins.com)*, *[Realm Royale](https://store.steampowered.com/app/813820/Realm_Royale)* and *[Smite](https://www.smitegame.com)*.

## Requirements
* [Python](http://python.org) 3.5 (or higher)
    * The following libraries are required: `requests` and `requests-aeaweb`
- [Access](https://fs12.formsite.com/HiRez/form48/secure_index.html) to Hi-Rez Studios' API

## Installation
The easiest way to install **Py-rez** is using `pip`, Python's package manager:

```
pip install -U pyrez
```

The required dependencies will be installed automatically. After that, you can use the library using `import pyrez`.

## Example

```py
from pyrez.api import PaladinsAPI

DEV_ID = 1004
AUTH_KEY = "23DF3C7E9BD14D84BF892AD206B6755C"

client = PaladinsAPI (DEV_ID, AUTH_KEY)
godsRanks = client.getGodRanks ("FeyRazzle")

if godsRanks is not None:
    for godRank in godsRanks:
        print(godRank.getWinratio ())
```

This example will print the winrate with every gods of player **FeyRazzle**.
