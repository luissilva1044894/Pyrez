## Pyrez: Easiest way to connect to Hi-Rez Studios API
[![License](https://img.shields.io/github/license/luissilva1044894/Pyrez.svg?style=plastic&logoWidth=15)](https://opensource.org/licenses/MIT "Pyrez · MIT License")
[![Discord Server](https://img.shields.io/discord/549020573846470659.svg?style=plastic&logo=discord&logoWidth=15)](https://discord.gg/XkydRPS "Support Server · Discord")
[![Say Thanks!](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/luissilva1044894 "Say Thanks!")

**Pyrez** is an [open-source](https://www.opensource.org "See https://www.opensource.org for the Open Source Definition") wrapper for [*Hi-Rez Studios*](https://www.hirezstudios.com "Hi-Rez Studios") API that supports [*Paladins*](https://www.paladins.com "Paladins Game"), [*Realm Royale*](https://www.realmroyale.com "Realm Royale Game") and [*Smite*](https://www.smitegame.com "Smite Game").

### Built with
- [Python](https://www.python.org/) - 2.7, 3.5, 3.6, & 3.7 are supported.
- [Requests](https://pypi.org/project/requests/)

### Documentation
Official Documentation, which shows all available methods and how to use them: [**Click here!**](https://pyrez.readthedocs.io/en/stable/ "Pyrez · Documentation")

### Support
If you need further help, please join the official [*support server*](
https://discord.gg/XkydRPS "Support Server · Discord") on [Discord](https://discordapp.com/ "Discord App").

### Requirements
- [Access](https://pyrez.readthedocs.io/en/stable/getting_started.html#registration "Form access to Hi-Rez Studios API") to Hi-Rez Studios API.

### Usage

```py
import pyrez

devId=1004
authKey='23DF3C7E9BD14D84BF892AD206B6755C'

def main():
    with pyrez.PaladinsAPI(devId, authKey) as paladins:
        print(paladins.getDataUsed())

if __name__ == '__main__':
	main()
```

### Application Example

- [FlaskPyrezAPI](https://github.com/luissilva1044894/FlaskPyrezAPI) - Example of a web application using Flask and Pyrez.

### License
This project is provided under the [MIT License](https://opensource.org/licenses/MIT "Pyrez · MIT License").

All information obtained is provided by Hi-Rez Studios API and is thus their property. According to Section 11a of the [`API Terms of Use`](https://www.hirezstudios.com/wp-content/themes/hi-rez-studios/pdf/api-terms-of-use-agreement.pdf "Hi-Rez Studios API · Terms of Use"), you must attribute any data provided as below.

> Data provided by Hi-Rez. © 2019 Hi-Rez Studios, Inc. All rights reserved.
