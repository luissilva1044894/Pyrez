
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

def check_error_msg(error_msg):
  if error_msg.find('Error while comparing Server and Client timestamp') != -1 or error_msg.find('Exception - Timestamp') != -1:
  	from ..exceptions.invalid_time import InvalidTime
  	raise InvalidTime(error_msg)
  if error_msg.find('dailylimit') != -1:
  	from ..exceptions.RateLimitExceeded import RateLimitExceeded
  	raise RateLimitExceeded(error_msg)
	if error_msg.find("No match_queue returned.  It is likely that the match wasn't live when GetMatchPlayerDetails() was called") != -1:
		from ..exceptions.MatchException import MatchException
		raise MatchException(error_msg)
	if error_msg.find('No Match History') != -1:
		from ..exceptions.MatchException import MatchException
		raise MatchException(error_msg)
	if error_msg.find('Only training queues') != -1 and error_msg.find('are supported for GetMatchPlayerDetails()') != -1:
		from ..exceptions.MatchException import MatchException
		raise MatchException(error_msg)
	if error_msg.find('404') != -1:
		from ..exceptions.NotFound import NotFound
		raise NotFound(error_msg)
	if error_msg.find('The server encountered an error processing the request') != -1:
		from ..exceptions.RequestError import RequestError
		raise RequestError(error_msg)
	if error_msg.find('Maximum number of active sessions reached') != -1:
		from ..exceptions.SessionLimitExceeded import SessionLimitExceeded
		raise SessionLimitExceeded(error_msg)
	if error_msg.find('Exception while validating developer access') != -1:
		from ..exceptions.UnauthorizedError import UnauthorizedError
		raise UnauthorizedError(error_msg)
