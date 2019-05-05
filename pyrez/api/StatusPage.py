from .API import API
from pyrez.enumerations import Endpoint, Format
from pyrez.models.StatusPage import Incidents, ScheduledMaintenances, StatusPage as SttPage
class StatusPage(API):
    def __init__(self):
        super().__init__()
    def getComponents(self):
        return self._httpRequest(self._getEndpoint("components"))
    @classmethod
    def _getEndpoint(cls, _endpoint=None, _api=True, _format="json"):
        return "{}{}{}{}".format(Endpoint.STATUS_PAGE, "/api/v2" if _api else "", "/{}".format(_endpoint) if _endpoint else "",  ".{}".format(_format) if _format else "")
    def getHistory(self, _format=Format.JSON):
        return self._httpRequest(self._getEndpoint("history", _api=False, _format=_format))
    def getIncidents(self, unresolvedOnly=False):
        _ = self._httpRequest(self._getEndpoint("incidents{}".format("/unresolved" if unresolvedOnly else "")))
        return Incidents(**_) if _ else None
    def getScheduledMaintenances(self, activeOnly=False, upcomingOnly=False):
        _ = self._httpRequest(self._getEndpoint("scheduled-maintenances{}".format("/active" if activeOnly else "/upcoming" if upcomingOnly else "")))
        return ScheduledMaintenances(**_) if _ else None
    def getStatus(self):
        _ = self._httpRequest(self._getEndpoint("status"))
        return SttPage(**_) if _ else None
    def getSummary(self):
        return self._httpRequest(self._getEndpoint("summary"))
