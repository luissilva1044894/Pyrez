from datetime import datetime
class Ping:
    def __init__(self, kwargs):
        self.textPlain = str(kwargs)
        textPlain = str(kwargs).split(' ')
        if len(textPlain) > 11:
            self.apiName = textPlain[0]
            self.apiVersion = textPlain[2].replace(')', '')
            self.gamePatch = textPlain[5].replace(']', '')
            self.ping = textPlain[8] == "successful."
            self.date = datetime.strptime("{} {} {}".format(textPlain[10].replace("Date:", ""), textPlain[11], textPlain[12]), "%m/%d/%Y %I:%M:%S %p")
    def __str__(self):
        return "APIName: {0.apiName} APIVersion: {0.apiVersion} GameVersion: {0.gamePatch} Ping: {0.ping} Date: {0.date}".format(self)
