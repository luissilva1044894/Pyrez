## Registration
><i>A</i> [<b>``Credentials``</b>](https://github.com/luissilva1044894/Pyrez/tree/master/docs#credentials) <i>that will provide access to Hi-Rez Studios' API.</i>

If you don't already have a devId and authKey, [<b>click here</b>](https://fs12.formsite.com/HiRez/form48/secure_index.html "Register to become developer") to become developer.

If your application is accepted, you will receive an e-mail from Hi-Rez Studios containing your personal [<b>``Credentials``</b>](https://github.com/luissilva1044894/Pyrez/tree/master/docs#credentials) within a few days.

***
## Credentials
><i>To access the API you'll need your own set of Credentials which consist of a Developer ID (devId) and an Authentication Key (authKey).</i>


Here are the Credentials for a sample account:
<table>
	<tr>
		<th> devId </th>
		<th> authKey </th>
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

## Creating API object
```py
    paladinsAPI = pyrez.api.PaladinsAPI(options)
```
or
```py
    smiteAPI = pyrez.api.SmiteAPI(options)
```
or
```py
    reamlRoyaleAPI = pyrez.api.RealmRoyaleAPI(options)
```

Options can have the following fields:
* `devId` - your developer ID (4 digit number).
* `authKey` - your authorization key (32 hex digits).
* `responseFormat` - `pyrez.enumerations.ResponseFormat.JSON` or `pyrez.enumerations.ResponseFormat.XML`. Defaults to JSON.
* `sessionId` - Manually set a sessionId. Defaults to None.
* `useConfigIni` - Allow Pyrez to read and store sessionId in a `config.ini` file. Defaults to True.

## Sessions

Sessions are created automatically and self-managed by Pyrez so you really don't need to initialise / call this method directly. However, you can set it manually or even request a new Session.

#### Manually:
```py
from pyrez.api import PaladinsAPI
paladinsAPI = PaladinsAPI(devId=1004, authKey="23DF3C7E9BD14D84BF892AD206B6755C", sessionId="1465AFCA32DBDB800CEF8C72F296C52C")
```
#### Requesting a new Session:
```py
from pyrez.api import PaladinsAPI
paladinsAPI = PaladinsAPI(devId=1004, authKey="23DF3C7E9BD14D84BF892AD206B6755C")
session = paladinsAPI._createSession()
print(session.sessionId)
```

### Usage - All methods return a promise that resolves to JSON response, unless stated otherwise
#### Methods -  - These methods are supported by pyrez.api.PaladinsAPI, pyrez.api.RealmRoyaleAPI object, and pyrez.api.SmiteAPI.
###### ``` makeRequest(apiMethod, params) ``` - Returns a JSON (Or XML) response
###### ``` switchEndpoint(endpoint) ``` - Bla bla bla
###### ``` ping() ``` - A quick way of validating access to the Hi-Rez API.
###### ``` testSession(sessionId) ``` - Returns a boolean that means if a sessionId is valid.
###### ``` getDataUsed() ``` - Returns a [`DataUsed`](https://github.com/luissilva1044894/Pyrez/blob/7d165ce963c633e740daca0fc2813cf83249afae/pyrez/models.py#L297 "DataUsed class") object containing resources used.
###### ``` getHiRezServerFeeds(format) ``` - Bla bla bla
###### ``` getHiRezServerStatus() ``` - Bla bla bla
###### ``` getPatchInfo() ``` - Function returns information about current deployed patch. Currently, this information only includes patch version.
###### ``` getFriends(playerId) ``` - Returns a list of [`Friend`](https://github.com/luissilva1044894/Pyrez/blob/7d165ce963c633e740daca0fc2813cf83249afae/pyrez/models.py#L315 "Friend class") objects containing all friend of a player. 
###### ``` getMatchDetails(matchId) ``` - Returns details of a specific match.
###### ``` getMatchDetailsBatch(matchIds) ``` - Bla bla bla
###### ``` getMatchHistory(playerId) ``` - Returns a list of  the players most recent matches (50).
###### ``` getMatchIdsByQueue(queueId, date, hour) ``` - Bla bla bla
###### ``` getPlayer(playerId) ``` - Returns an object with basic player statistics.
###### ``` getPlayerAchievements(playerId) ``` - Bla bla bla
###### ``` getPlayerIdByName(playerName) ``` - Bla bla bla
###### ``` getPlayerIdByPortalUserId(portalId, portalUserId) ``` - Bla bla bla
###### ``` getPlayerIdsByGamerTag(gamerTag, portalId) ``` - Bla bla bla
###### ``` getPlayerStatus(playerId) ``` - Returns the current status of the player. (offline, in-lobby etc.)
###### ``` getQueueStats(playerId, queueId) ``` - Bla bla bla
##### PaladinsAPI - These methods are only supported by pyrez.api.PaladinsAPI object.
###### ``` getChampions(language) ``` - Returns a list of [`Champion`](https://github.com/luissilva1044894/Pyrez/blob/7d165ce963c633e740daca0fc2813cf83249afae/pyrez/models.py#L152 "Champion class") objects containing all the champions and details about them.
###### ``` getChampionCards(champId, languageCode) ``` -  - Returns a list of all the cards available for chosen champion and details about them.
###### ``` getChampionLeaderboard(champId, queueId) ``` - Bla bla bla
###### ``` getChampionRanks(playerId) ``` - Returns details of the players performance with all champions.
###### ``` getChampionSkins(champId, language) ``` - Returns all skins available for chosen champion.
###### ``` getDemoDetails(matchId) ``` - Bla bla bla
###### ``` getEsportsProLeagueDetails() ``` - Bla bla bla
###### ``` getGods(language) ``` - Returns a list of [`Champion`](https://github.com/luissilva1044894/Pyrez/blob/7d165ce963c633e740daca0fc2813cf83249afae/pyrez/models.py#L152 "Champion class") objects containing all the champions and details about them.
###### ``` getGodLeaderboard(champId, queueId) ``` - Bla bla bla
###### ``` getGodRanks(playerId) ``` - Returns details of the players performance with all champions.
###### ``` getGodSkins(champId, language) ``` - Returns all skins available for chosen champion.
###### ``` getItems(language) ``` - Returns all the items in the game, including cards, items etc...
###### ``` getLatestPatchNotes(languageCode) ``` - Bla bla bla
###### ``` getLeagueLeaderboard(queueId, tier, season) ``` - Bla bla bla
###### ``` getLeagueLeaderboard(queueId, tier, season) ``` - Bla bla bla
###### ``` getLeagueSeasons(queueId) ``` - Bla bla bla
###### ``` getLiveMatchDetails(matchId) ``` - Bla bla bla
###### ``` getPlayerIdInfoForXboxAndSwitch(playerName) ``` - Bla bla bla
###### ``` getPlayerLoadouts(playerId, language) ``` - Returns champion loadouts for player.
###### ``` getWebsitePostBySlug(slug, languageCode) ``` - Bla bla bla
###### ``` getWebsitePosts(languageCode) ``` - Bla bla bla
###### ``` getWebsitePostsByQuery(query, languageCode) ``` - Bla bla bla
##### RealmRoyaleAPI - These methods are only supported by pyrez.api.RealmRoyaleAPI object.
###### ``` getLeaderboard(queueId, rankingCriteria) ``` - Bla bla bla
###### ``` getPlayerMatchHistory(playerId) ``` - Bla bla bla
###### ``` getPlayerMatchHistory(playerId, startDatetime) ``` - Bla bla bla
###### ``` getPlayerStats(playerId) ``` - Bla bla bla
###### ``` getTalents(languageCode) ``` - Bla bla bla
###### ``` searchPlayers(playerId) ``` - Bla bla bla
##### SmiteAPI - These methods are only supported by pyrez.api.SmiteAPI object.
###### ``` getDemoDetails(matchId) ``` - Bla bla bla
###### ``` getEsportsProLeagueDetails() ``` - Bla bla bla
###### ``` getGods(language) ``` - Returns a list of [`God`](https://github.com/luissilva1044894/Pyrez/blob/7d165ce963c633e740daca0fc2813cf83249afae/pyrez/models.py#L173 "God class") objects containing all the gods and details about them.
###### ``` getGodLeaderboard(godId, queueId) ``` - Bla bla bla
###### ``` getGodRanks(playerId) ``` - Returns details of the players performance with all gods.
###### ``` getGodRecommendedItems(godId, language) ``` - Bla bla bla
###### ``` getGodSkins(godId, language) ``` - Returns all skins available for chosen god.
###### ``` getItems(language) ``` - Returns all the items in the game, including cards, items etc...
###### ``` getLeagueLeaderboard(queueId, tier, season) ``` - Bla bla bla
###### ``` getLeagueSeasons(queueId) ``` - Bla bla bla
###### ``` getLiveMatchDetails(matchId) ``` - Bla bla bla
###### ``` getMotd() ``` - Bla bla bla
###### ``` getTeamDetails(clanId) ``` - Bla bla bla
###### ``` getTeamPlayers(clanId) ``` - Bla bla bla
###### ``` getTopMatches() ``` - Bla bla bla
###### ``` searchTeams(teamId) ``` - Bla bla bla