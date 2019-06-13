from .APIResponse import APIResponse
from pyrez.models.Mixin import Player as PlayerMixin
class PlayerAcheviements(APIResponse, PlayerMixin):
    def __init__(self, **kwargs):
        APIResponse.__init__(self, **kwargs)
        PlayerMixin.__init__(self, **kwargs)
        self.assistedKills = kwargs.get("AssistedKills", 0) or 0
        self.campsCleared = kwargs.get("CampsCleared", 0) or 0
        self.deaths = kwargs.get("Deaths", 0) or 0
        self.divineSpree = kwargs.get("DivineSpree", 0) or 0
        self.doubleKills = kwargs.get("DoubleKills", 0) or 0
        self.fireGiantKills = kwargs.get("FireGiantKills", 0) or 0
        self.firstBloods = kwargs.get("FirstBloods", 0) or 0
        self.godLikeSpree = kwargs.get("GodLikeSpree", 0) or 0
        self.goldFuryKills = kwargs.get("GoldFuryKills", 0) or 0
        self.immortalSpree = kwargs.get("ImmortalSpree", 0) or 0
        self.killingSpree = kwargs.get("KillingSpree", 0) or 0
        self.minionKills = kwargs.get("MinionKills", 0) or 0
        self.pentaKills = kwargs.get("PentaKills", 0) or 0
        self.phoenixKills = kwargs.get("PhoenixKills", 0) or 0
        self.playerKills = kwargs.get("PlayerKills", 0) or 0
        self.quadraKills = kwargs.get("QuadraKills", 0) or 0
        self.rampageSpree = kwargs.get("RampageSpree", 0) or 0
        self.shutdownSpree = kwargs.get("ShutdownSpree", 0) or 0
        self.siegeJuggernautKills = kwargs.get("SiegeJuggernautKills", 0) or 0
        self.towerKills = kwargs.get("TowerKills", 0) or 0
        self.tripleKills = kwargs.get("TripleKills", 0) or 0
        self.unstoppableSpree = kwargs.get("UnstoppableSpree", 0) or 0
        self.wildJuggernautKills = kwargs.get("WildJuggernautKills", 0) or 0
