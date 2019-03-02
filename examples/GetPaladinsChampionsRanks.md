```py
from pyrez.api import PaladinsAPI

paladinsAPI = PaladinsAPI(devId=1004, authKey="23DF3C7E9BD14D84BF892AD206B6755C")
championsRank = paladinsAPI.getGodRanks(paladinsAPI.getPlayer("FeyRazzle").playerId)

for championRank in championsRank:
	print("{0} (Last Player: {1}) {2}".format(championRank.godName, championRank.lastPlayed, championRank.getWinratio()))
```


This example will print the winrate with every [Champion](https://www.paladins.com/champions "Paladins Champions") of player **[FeyRazzle](https://twitch.tv/FeyRazzle "Sexiest Voice on Twitch")**.
