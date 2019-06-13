from pyrez.models import APIResponse
from pyrez.enumerations import Champions
class ChampionCard(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.activeFlagActivationSchedule = str(kwargs.get("active_flag_activation_schedule", '')).lower() == 'y' or False
        self.activeFlagLti = str(kwargs.get("active_flag_lti", '')).lower() == 'y' or False
        self.cardDescription = kwargs.get("card_description", '') or ''
        self.cardId1 = kwargs.get("card_id1", 0) or ''
        self.cardId2 = kwargs.get("card_id2", 0) or ''
        self.cardName = kwargs.get("card_name", '') or ''
        self.cardNameEnglish = kwargs.get("card_name_english", '') or ''
        self.godCardURL =  kwargs.get("championCard_URL", '') or ''
        self.godIconURL = kwargs.get("championIcon_URL", '') or ''
        try:
            self.godId = Champions(kwargs.get("champion_id"))
            self.godName = self.godId.getName()
        except ValueError:
            self.godId = kwargs.get("champion_id", 0) or 0
            self.godName = kwargs.get("champion_name", '') or ''
        self.exclusive = str(kwargs.get("exclusive", '')).lower() == 'y' or False
        self.rank = kwargs.get("rank", 0) or 0
        self.rarity = kwargs.get("rarity", '') or ''
        self.rechargeSeconds = kwargs.get("recharge_seconds", 0) or 0
    def getIconURL(self):
        return "https://web2.hirez.com/paladins/champion-icons/{}.jpg".format(self.godName.lower().replace(' ', '-'))
    def getCardURL(self):
        return "https://web2.hirez.com/paladins/champion-cards/{}.jpg".format(self.cardNameEnglish.lower().replace(' ', '-'))
