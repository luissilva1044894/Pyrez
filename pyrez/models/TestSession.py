class TestSession:
    def __init__(self, kwargs):
        self.textPlain = str(kwargs)
        textPlain = str(kwargs).split(' ')
        if len(textPlain) > 19:
            self.successfull = self.textPlain.lower().find('this was a successful test with the following parameters added:') != -1
            self.devId = textPlain[11]
            from ..utils.datetime import string_datetime_utc_to_datetime
            #self.date = '{0} {1} {2}'.format(textPlain[13].replace('time:', ''), textPlain[14], textPlain[15])
            self.date = string_datetime_utc_to_datetime('{} {} {}'.format(textPlain[13].replace('time:', ''), textPlain[14], textPlain[15]))
            self.signature = textPlain[17]
            self.session = textPlain[19]
    def __str__(self):
        return 'Successful: {0.successfull} devId: {0.devId} Date: {0.date} Signature: {0.signature} Session: {0.session}'.format(self)
