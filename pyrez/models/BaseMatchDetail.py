from .MatchBase import MatchBase
class BaseMatchDetail(MatchBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.damageBot = kwargs.get("Damage_Bot", 0) or 0
        self.damageDoneInHand = kwargs.get("Damage_Done_In_Hand", 0) or 0
        self.damageDoneMagical = kwargs.get("Damage_Done_Magical", 0) or 0
        self.damageDonePhysical = kwargs.get("Damage_Done_Physical", 0) or 0
        self.damageMitigated = kwargs.get("Damage_Mitigated", 0) or 0
        self.damageStructure = kwargs.get("Damage_Structure", 0) or 0
        self.damageTaken = kwargs.get("Damage_Taken", 0) or 0
        self.damageTakenMagical = kwargs.get("Damage_Taken_Magical", 0) or 0
        self.damageTakenPhysical = kwargs.get("Damage_Taken_Physical", 0) or 0
        self.deaths = kwargs.get("Deaths", 0) or 0
        self.distanceTraveled = kwargs.get("Distance_Traveled", 0) or 0
        self.healing = kwargs.get("Healing", 0) or 0
        self.healingBot = kwargs.get("Healing_Bot", 0) or 0
        self.healingPlayerSelf = kwargs.get("Healing_Player_Self", 0) or 0
        self.killingSpree = kwargs.get("Killing_Spree", 0) or 0
        self.mapName = kwargs.get("Map_Game", '') or ''
        self.matchMinutes = kwargs.get("Minutes", 0) or 0
        self.matchRegion = kwargs.get("Region", '') or ''
        self.matchTimeSecond = kwargs.get("Time_In_Match_Seconds", 0) or 0
        self.multiKillMax = kwargs.get("Multi_kill_Max", 0) or 0
        self.objectiveAssists = kwargs.get("Objective_Assists", 0) or 0
        self.playerName = kwargs.get("playerName", '') or ''
        self.surrendered = kwargs.get("Surrendered", '') or ''
        self.team1Score = kwargs.get("Team1Score", 0) or 0
        self.team2Score = kwargs.get("Team2Score", 0) or 0
        self.wardsPlaced = kwargs.get("Wards_Placed", 0) or 0
        self.winStatus = kwargs.get("Win_Status", '') or ''
        self.winningTaskForce = kwargs.get("Winning_TaskForce", 0) or 0
