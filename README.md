# Pyrez: Easily way to connect to Hi-Rez API
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/luissilva1044894/Pyrez/blob/master/LICENSE)
[![Runtime Version](https://img.shields.io/pypi/pyversions/pyrez.svg)](https://pypi.org/project/pyrez)
[![Contributors](https://img.shields.io/github/contributors/luissilva1044894/Pyrez.svg)](https://github.com/luissilva1044894/Pyrez/graphs/contributors)


**PyRez** is an open-source Python-based wrapper for [Hi-Rez](http://www.hirezstudios.com "Hi-Rez Studios") API that supports *[Paladins](https://www.paladins.com "Paladins Game")*, *[Realm Royale](https://github.com/apugh/realm-api-proposal/wiki "Realm Royale API Documentation")* and *[Smite](https://www.smitegame.com "Smite Game")*.

## Requirements
* [Python](http://python.org "Python.org") 3.5(or higher).
    * The following libraries are required: [`Requests`](https://pypi.org/project/requests "requests") and `requests-aeaweb`.
- [Access](https://fs12.formsite.com/HiRez/form48/secure_index.html "Form access to Hi-Rez API") to Hi-Rez Studios API.

## Installation
The easiest way to install **Pyrez** is using `pip`, Python's package manager:

```
pip install -e git+https://github.com/luissilva1044894/pyrez.git@master#egg=pyrez
```
The required dependencies will be installed automatically.
After that, you can use the library using:
```py
import pyrez
```

## Example

```py
from pyrez.api import PaladinsAPI

paladinsAPI = PaladinsAPI(devId=1004, authKey="23DF3C7E9BD14D84BF892AD206B6755C")
playerId = paladinsAPI.getPlayer("FeyRazzle").playerId
championsRank = paladinsAPI.getGodRanks(playerId)

for championRank in championsRank:
	print(championRank.getWinratio())
```

This example will print the winrate with every [Champion](https://www.paladins.com/champions "Paladins Champions") of player **[FeyRazzle](https://twitch.tv/FeyRazzle "Sexiest Voice on Twitch")**.

#### Methods
###### ``` __createSession__() ``` - The Sessions are self-managed by Pyrez so you really don't need to initalise / call this yourself
###### ``` makeRequest(apiMethod, params =()) ``` - Bla bla bla
###### ``` switchEndpoint(endpoint) ``` - Bla bla bla
###### ``` ping() ``` - Bla bla bla
###### ``` testSession(sessionId) ``` - Bla bla bla
###### ``` getDataUsed() ``` - Returns an :class:`DataUsed` object containing resources used.
###### ``` getHiRezServerFeeds() ``` - Bla bla bla
###### ``` getHiRezServerStatus() ``` - Bla bla bla
###### ``` getPatchInfo() ``` - Bla bla bla
###### ``` getFriends(playerId) ``` - Returns a list of :class:`Friend` objects containing all friend of a player. 
###### ``` getMatchDetails(matchId) ``` - Returns details of a specific match.
###### ``` getMatchDetailsBatch(matchIds =()) ``` - Bla bla bla
###### ``` getMatchHistory(playerId) ``` - Returns a list of  the players most recent matches (50).
###### ``` getMatchIdsByQueue(queueId, date, hour) ``` - Bla bla bla
###### ``` getPlayer(playerId) ``` - Returns an object with basic player statistics.
###### ``` getPlayerAchievements(playerId) ``` - Bla bla bla
###### ``` getPlayerStatus(playerId) ``` - Returns the current status of the player. (offline, in-lobby etc.)
###### ``` getQueueStats(playerId, queueId) ``` - Bla bla bla
##### PaladinsAPI
###### ``` getGods(language) ``` - Returns a list of all the champions and details about them.
###### ``` getGodRanks(playerId) ``` - Returns details of the players performance with all champions.
###### ``` getGodSkins(champId, language) ``` - Returns all skins available for chosen champion.
###### ``` getItems(language) ``` - Returns all the items in the game, including cards, items etc...
###### ``` getChampions(language) ``` - Returns a list of all the champions and details about them.
###### ``` getChampionRanks(playerId) ``` - Returns details of the players performance with all champions.
###### ``` getChampionRecommendedItems(champId, language) ```
###### ``` getChampionSkins(champId, language) ``` - Returns all skins available for chosen champion.
###### ``` getMatchPlayerDetails(matchId) ``` - Bla bla bla
###### ``` getPlayerIdInfoForXboxAndSwitch(playerName) ``` - Bla bla bla
###### ``` getPlayerLoadouts(playerId, language) ``` - Returns champion loadouts for player.
##### RealmRoyaleAPI
###### ``` getPlayerMatchHistory(playerId) ``` - Bla bla bla
###### ``` getPlayerMatchHistoryAfterDatetime(playerId, startDatetime) ``` - Bla bla bla
###### ``` getPlayerStats(playerId) ``` - Bla bla bla
###### ``` searchPlayers(playerId) ``` - Bla bla bla
##### SmiteAPI
###### ``` getGods(language) ``` - Returns a list of all the gods and details about them.
###### ``` getGodLeaderboard(godId, queueId) ``` - Bla bla bla
###### ``` getGodRanks(playerId) ``` - Returns details of the players performance with all gods.
###### ``` getGodRecommendedItems(godId, language) ``` - Bla bla bla
###### ``` getGodSkins(godId, language) ``` - Returns all skins available for chosen god.
###### ``` getItems(language) ``` - Returns all the items in the game, including cards, items etc...
###### ``` getDemoDetails(matchId) ``` - Bla bla bla
###### ``` getEsportsProLeagueDetails() ``` - Bla bla bla
###### ``` getLeagueLeaderboard(queueId, tier, season) ``` - Bla bla bla
###### ``` getLeagueSeasons(queueId) ``` - Bla bla bla
###### ``` getMotd() ``` - Bla bla bla
###### ``` getTeamDetails(clanId) ``` - Bla bla bla
###### ``` getTeamMatchHistory(clanId) ``` - Bla bla bla
###### ``` getTeamPlayers(clanId) ``` - Bla bla bla
###### ``` getTopMatches() ``` - Bla bla bla
###### ``` searchTeams(teamId) ``` - Bla bla bla
