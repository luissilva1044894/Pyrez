```py
from pyrez.api import PaladinsAPI

paladinsAPI = PaladinsAPI(devId=1004, authKey="23DF3C7E9BD14D84BF892AD206B6755C")
championRanks = paladinsAPI.getGodRanks(paladinsAPI.getPlayer("FeyRazzle").playerId)

for championRank in championRanks:
	print("{0} (Last Played: {1}) {2}".format(championRank.godName, championRank.lastPlayed, championRank.getWinratio()))
```

Version 2: except now we store the player's id to save API calls.

```py
from pyrez.api import PaladinsAPI

# Get the player id for a player based on their name. First it checks a dictionary and if they are not in there then
# it does an API call to get the player's id. Then it writes that id to the dictionary. Helps save API calls.
def get_player_id(playerName):
    playerName = playerName.lower()
    with open("player_ids") as f:
        player_ids = json.load(f)

    # This player is already in the dictionary and therefor we don't need to waste an api call to get the player id.
    if playerName in player_ids:
        return player_ids[playerName]
    else:
        player = paladinsAPI.getPlayer(playerName)
        if not player:  # invalid name
            return -1
        new_id = player.playerId
        player_ids[playerName] = new_id # store the new id in the dictionary

        # need to update the file now
        print("Added a new player the dictionary: " + playerName)
        with open("player_ids", 'w') as f:
            json.dump(player_ids, f)
        return new_id

paladinsAPI = PaladinsAPI(devId=1004, authKey="23DF3C7E9BD14D84BF892AD206B6755C")
championRanks = paladinsAPI.getGodRanks(get_player_id("FeyRazzle")) # This is the only line that changes from the program above

for championRank in championRanks:
    print("{0} (Last Played: {1}) {2}".format(championRank.godName, championRank.lastPlayed, championRank.getWinratio()))
```

This example will print the winrate with every [Champion](https://www.paladins.com/champions "Paladins Champions") of player **[FeyRazzle](https://twitch.tv/FeyRazzle "Sexiest Voice on Twitch")**.
