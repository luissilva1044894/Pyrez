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
            #self.date = "{0} {1} {2}".format(textPlain [10].replace("Date:", ""), textPlain [11], textPlain [12])
            self.date = datetime.strptime("{0} {1} {2}".format(textPlain [10].replace("Date:", ""), textPlain [11], textPlain [12]), "%m/%d/%Y %H:%M:%S %p")
    def __str__(self):
        return "APIName: {0} APIVersion: {1} GameVersion: {2} Ping: {3} Date: {4}".format(self.apiName, self.apiVersion, self.gamePatch, self.ping, self.date)
