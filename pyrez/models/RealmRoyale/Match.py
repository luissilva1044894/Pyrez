from pyrez.enumerations import Classes, QueueRealmRoyale
from pyrez.models import APIResponseBase
from pyrez.models.Mixin import MatchId
class Match(APIResponseBase, MatchId):
    def __init__(self, **kwargs):
        APIResponseBase.__init__(self, **kwargs)
        MatchId.__init__(self, **kwargs)
        self.assists = kwargs.get("assists", 0) if kwargs else 0
        try:
            self.godId = Classes(kwargs.get("class_id"))
            self.godName = self.godId.getName()
        except ValueError:
            self.godId = kwargs.get("class_id", 0)  if kwargs else 0
            self.godName = kwargs.get("class_name", None) if kwargs else None
        self.creeps = kwargs.get("creeps", 0) if kwargs else 0
        self.damage = kwargs.get("damage", 0) if kwargs else 0
        self.damageDoneInHand = kwargs.get("damage_done_in_hand", 0) if kwargs else 0
        self.damageMitigated = kwargs.get("damage_mitigated", 0) if kwargs else 0
        self.damageTaken = kwargs.get("damage_taken", 0) if kwargs else 0
        self.deaths = kwargs.get("deaths", 0) if kwargs else 0
        self.gold = kwargs.get("gold", 0) if kwargs else 0
        self.healingBot = kwargs.get("healing_bot", 0) if kwargs else 0
        self.healingPlayer = kwargs.get("healing_player", 0) if kwargs else 0
        self.healingPlayerSelf = kwargs.get("healing_player_self", 0) if kwargs else 0
        self.killingSpreeMax = kwargs.get("killing_spree_max", 0) if kwargs else 0
        self.kills = kwargs.get("kills", 0) if kwargs else 0
        self.mapName = kwargs.get("map_game", None) if kwargs else None
        self.matchDatetime = kwargs.get("match_datetime", None) if kwargs else None
        self.matchDurationSecs = kwargs.get("match_duration_secs", 0) if kwargs else 0
        try:
            self.matchQueueId = QueueRealmRoyale(kwargs.get("match_queue_id"))
        except ValueError:
            self.matchQueueId = kwargs.get("match_queue_id", 0) if kwargs else 0
        self.matchQueueName = kwargs.get("match_queue_name", None) if kwargs else None
        self.placement = kwargs.get("placement", 0) if kwargs else 0
        self.playerId = kwargs.get("player_id", 0) if kwargs else 0
        self.region = kwargs.get("region", None) if kwargs else None
        self.teamId = kwargs.get("team_id", 0) if kwargs else 0
        self.timeInMatchMinutes = kwargs.get("time_in_match_minutes", 0) if kwargs else 0
        self.timeInMatchSecs = kwargs.get("time_in_match_secs", 0) if kwargs else 0
        self.wardsMinesPlaced = kwargs.get("wards_mines_placed", 0) if kwargs else 0
