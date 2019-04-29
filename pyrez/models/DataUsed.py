from .APIResponse import APIResponse
class DataUsed(APIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.activeSessions = kwargs.get("Active_Sessions", kwargs.get("active_sessions", 0)) if kwargs is not None else 0
        self.concurrentSessions = kwargs.get("Concurrent_Sessions", kwargs.get("concurrent_sessions", 0)) if kwargs is not None else 0
        self.requestLimitDaily = kwargs.get("Request_Limit_Daily", kwargs.get("request_limit_daily", 0)) if kwargs is not None else 0
        self.sessionCap = kwargs.get("Session_Cap", kwargs.get("session_cap", 0)) if kwargs is not None else 0
        self.sessionTimeLimit = kwargs.get("Session_Time_Limit", kwargs.get("session_time_limit", 0)) if kwargs is not None else 0
        self.totalRequestsToday = kwargs.get("Total_Requests_Today", kwargs.get("total_requests_today", 0)) if kwargs is not None else 0
        self.totalSessionsToday = kwargs.get("Total_Sessions_Today", kwargs.get("total_sessions_today", 0)) if kwargs is not None else 0
    def __str__(self):
        return "Active sessions: {0} Concurrent sessions: {1} Request limit daily: {2} Session cap: {3} Session time limit: {4} Total requests today: {5} Total sessions today: {6} ".format(self.activeSessions, self.concurrentSessions, self.requestLimitDaily, self.sessionCap, self.sessionTimeLimit, self.totalRequestsToday, self.totalSessionsToday)
    def sessionsLeft(self):
        return self.sessionCap - self.totalSessionsToday if self.sessionCap - self.totalSessionsToday > 0 else 0
    def requestsLeft(self):
        return self.requestLimitDaily - self.totalRequestsToday if self.requestLimitDaily - self.totalRequestsToday > 0 else 0
    def concurrentSessionsLeft(self):
        return self.concurrentSessions - self.activeSessions if self.concurrentSessions - self.activeSessions > 0 else 0
