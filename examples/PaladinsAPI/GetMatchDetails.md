# Usage 1
```py
from pyrez.api import PaladinsAPI

paladinsAPI = PaladinsAPI(devId=1004, authKey="23DF3C7E9BD14D84BF892AD206B6755C")
matchDetails = paladinsAPI.getMatchDetails("811206235")

for matchDetail in matchDetails:
	print(matchDetail)
```

# Usage 2
```py
from pyrez.api import PaladinsAPI

paladinsAPI = PaladinsAPI(devId=1004, authKey="23DF3C7E9BD14D84BF892AD206B6755C")
matchDetails = paladinsAPI.getMatchDetails(811206235)

for matchDetail in matchDetails:
	print(matchDetail)
```

# Usage 3
```py
from pyrez.api import PaladinsAPI

matchIds = [ 811206235, 802047057, 802042501, 802033500, 802025706, 802019357 ]
paladinsAPI = PaladinsAPI(devId=1004, authKey="23DF3C7E9BD14D84BF892AD206B6755C")
matchDetails = paladinsAPI.getMatchDetails(matchIds)

for matchDetail in matchDetails:
	print(matchDetail)
```