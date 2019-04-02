<div  align="center">
<a href="https://github.com/luissilva1044894/Pyrez" title="Pyrez - Github repository" alt="Pyrez: Easiest way to connect to Hi-Rez Studios' API!"><img src="../assets/Pyrez.png" height="128" width="128"></a>

# Welcome to the official documentation of Pyrez
</div>

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
		<th> devId (4 digit number) </th>
		<th> authKey (32 hex digits string) </th>
	</tr>
	<tr>
		<td> 1004 </td>
		<td> 23DF3C7E9BD14D84BF892AD206B6755C </td>
	</tr>
</table>

***

## Importing
```py
import pyrez
import pyrez.api
from pyrez.api import PaladinsAPI, SmiteAPI, RealmRoyaleAPI
import pyrez.enumerations
import pyrez.models
```

## Creating API object
```py
paladinsAPI = PaladinsAPI(options)
```
or
```py
smiteAPI = SmiteAPI(options)
```
or
```py
reamlRoyaleAPI = RealmRoyaleAPI(options)
```

Options can have the following fields:
* `devId` - Your devId.
* `authKey` - Your autKey.
* `responseFormat` - `pyrez.enumerations.ResponseFormat.JSON` or `pyrez.enumerations.ResponseFormat.XML`. Defaults to JSON.
* `sessionId` - Manually sets a sessionId. Defaults to None.
* `useConfigIni` - Allows Pyrez to read and store sessionId in a `config.ini` file. Defaults to True.

## Sessions

Sessions are created automatically and self-managed by Pyrez so you really don't need to initialise / call this method directly. However, you can set it manually or even request a new Session.

#### Manually:
```py
paladinsAPI = PaladinsAPI(devId=1004, authKey="23DF3C7E9BD14D84BF892AD206B6755C", sessionId="1465AFCA32DBDB800CEF8C72F296C52C")
```
#### Requesting a new Session:
```py
paladinsAPI = PaladinsAPI(devId=1004, authKey="23DF3C7E9BD14D84BF892AD206B6755C")
session = paladinsAPI._createSession()
print(session.sessionId)
```

### Usage - All methods return a promise that resolves to JSON response, unless stated otherwise
#### Methods
>These methods are supported by [`PaladinsAPI`](https://github.com/luissilva1044894/Pyrez/tree/master/docs#paladins-specific "Paladins Specific Methods"), [`RealmRoyaleAPI`](https://github.com/luissilva1044894/Pyrez/tree/master/docs#realm-royale-specific "Realm Royale Specific Methods"), and [`SmiteAPI`](https://github.com/luissilva1044894/Pyrez/tree/master/docs#smite-specific "Smite Specific Methods") object.
###### ``` makeRequest(apiMethod, params) ``` - Returns a JSON object (Or XML string).
###### ``` switchEndpoint(endpoint) ``` - Bla bla bla
###### ``` ping() ``` - A quick way of validating access to the Hi-Rez API.
###### ``` testSession(sessionId) ``` - Returns a boolean that means if a sessionId is valid.
###### ``` getDataUsed() ``` - Returns a [`DataUsed`](https://github.com/luissilva1044894/Pyrez/blob/7d165ce963c633e740daca0fc2813cf83249afae/pyrez/models.py#L297 "DataUsed class") object containing resources used.
###### ``` getHiRezServerFeeds(format) ``` - Bla bla bla
###### ``` getHiRezServerStatus() ``` - Bla bla bla
###### ``` getPatchInfo() ``` - Returns information about current deployed patch. Currently, this information only includes patch version.
###### ``` getFriends(playerId) ``` - Returns a list of [`Friend`](https://github.com/luissilva1044894/Pyrez/blob/7d165ce963c633e740daca0fc2813cf83249afae/pyrez/models.py#L315 "Friend class") objects containing all friend of a player. 
###### ``` getMatchDetails(matchId) ``` - Returns details of a specific match.
###### ``` getMatchDetailsBatch(matchIds) ``` - Returns details of a specific matches.
###### ``` getMatchHistory(playerId) ``` - Returns a list of  the player most recent 50 matches.
###### ``` getMatchIdsByQueue(queueId, date, hour) ``` - Bla bla bla
###### ``` getPlayer(playerId) ``` - Returns an object with basic statistics for a particular player.
###### ``` getPlayerAchievements(playerId) ``` - Bla bla bla
###### ``` getPlayerIdByName(playerName) ``` - Bla bla bla
###### ``` getPlayerIdByPortalUserId(portalId, portalUserId) ``` - Bla bla bla
###### ``` getPlayerIdsByGamerTag(gamerTag, portalId) ``` - Bla bla bla
###### ``` getPlayerStatus(playerId) ``` - Returns the current status of the player. (offline, in-lobby etc.)
###### ``` getQueueStats(playerId, queueId) ``` - Bla bla bla
##### Paladins-specific
>These methods are only supported by [`PaladinsAPI`](https://github.com/luissilva1044894/Pyrez/blob/f855bd3a5d2e4175ae5cd86d2251c85316f2bf4c/pyrez/api.py#L799 "Paladins Class Definition") object.
###### ``` getChampions(language) ``` - Returns a list of [`Champion`](https://github.com/luissilva1044894/Pyrez/blob/7d165ce963c633e740daca0fc2813cf83249afae/pyrez/models.py#L152 "Champion class") objects containing all the champions and details about them.
###### ``` getChampionCards(champId, languageCode) ``` -  - Returns a list of all the cards available for chosen champion and details about them.
###### ``` getChampionLeaderboard(champId, queueId) ``` - Bla bla bla
###### ``` getChampionRanks(playerId) ``` - Returns details of the players performance with all champions.
###### ``` getChampionSkins(champId, language) ``` - Returns all available skins for a particular Champion.
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
##### Realm Royale-specific
>These methods are only supported by [RealmRoyaleAPI](https://github.com/luissilva1044894/Pyrez/blob/f855bd3a5d2e4175ae5cd86d2251c85316f2bf4c/pyrez/api.py#L996 "Realm Royale Class Definition") object.
###### ``` getLeaderboard(queueId, rankingCriteria) ``` - Bla bla bla
###### ``` getPlayerMatchHistory(playerId) ``` - Bla bla bla
###### ``` getPlayerMatchHistory(playerId, startDatetime) ``` - Bla bla bla
###### ``` getPlayerStats(playerId) ``` - Bla bla bla
###### ``` getTalents(languageCode) ``` - Bla bla bla
###### ``` searchPlayers(playerId) ``` - Bla bla bla
##### Smite-specific
>These methods are only supported by [SmiteAPI](https://github.com/luissilva1044894/Pyrez/blob/f855bd3a5d2e4175ae5cd86d2251c85316f2bf4c/pyrez/api.py#L1084 "Smite Class Definition") object.
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