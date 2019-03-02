## Registration
><i>A</i> [<b>``Credentials``</b>](https://github.com/luissilva1044894/Pyrez/tree/master/pyrez/docs/README.md#credentials) <i>that will provide access to Hi-Rez Studios API.</i>

If you don't already have a devId and authKey, [<b>click here</b>](https://fs12.formsite.com/HiRez/form48/secure_index.html "Register to become developer") to become developer.

If your application is accepted, you will receive an e-mail from Hi-Rez Studios containing your personal [<b>``Credentials``</b>](https://github.com/luissilva1044894/Pyrez/tree/master/pyrez/docs/README.md#credentials) within a few days.

***
## Credentials
><i>To access the API you'll need your own set of Credentials which consist of a Developer ID (devId) and an Authentication Key (authKey).</i>


Here are the Credentials for a sample account:
<table>
	<tr>
		<th> DevId </th>
		<th> AuthKey </th>
	</tr>
	<tr>
		<td> 1004 </td>
		<td> 23DF3C7E9BD14D84BF892AD206B6755C </td>
	</tr>
</table>

***

## Import
```py
import pyrez
import pyrez.api
from pyrez.api import PaladinsAPI
import pyrez.enumerations
import pyrez.models
```

## Sessions

The Sessions are self-managed by the wrapper. But you can set it manually or even request a new Session.

### Manually:
```py
from pyrez.api import PaladinsAPI
paladinsAPI = PaladinsAPI (devId=1004, authKey="23DF3C7E9BD14D84BF892AD206B6755C", sessionId="1465AFCA32DBDB800CEF8C72F296C52C")
```

### Request a new Session:
```py
from pyrez.api import PaladinsAPI
paladinsAPI = PaladinsAPI (devId=1004, authKey="23DF3C7E9BD14D84BF892AD206B6755C")
session = paladinsAPI.__createSession__()
print(session.sessionId)
```
### Usage
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