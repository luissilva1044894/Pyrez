
.. |coro| replace:: This function is a |corourl|_.
.. |corourl| replace:: *coroutine*
.. _corourl: https://docs.python.org/3/library/asyncio-task.html#coroutine

.. _Hi-Rez Studios: http://www.hirezstudios.com/
.. _Paladins: https://www.paladins.com/
.. _Realm Royale: https://www.realmroyale.com/
.. _Smite: https://www.smitegame.com/
.. _Python: https://www.python.org/
.. _Status Page: https://status.hirezstudios.com/
.. _Homepage: https://pyrez.readthedocs.io/en/stable/
.. _searching: https://pyrez.readthedocs.io/en/stable/search.html
.. _Search: https://pyrez.readthedocs.io/en/stable/search.html

.. |SEARCHPAGE| replace:: `Search`_
.. |HOMEPAGE| replace:: `Homepage`_
.. |STATUSPAGE| replace:: `Status Page`_
.. |HIREZSTUDIOS| replace:: `Hi-Rez Studios`_
.. |PALADINSGAME| replace:: `Paladins`_
.. |SMITEGAME| replace:: `Smite`_
.. |REALMROYALEGAME| replace:: `Realm Royale`_
.. |PYTHON| replace:: `Python`_
.. |DailyException| replace:: pyrez.exceptions.RateLimitExceeded: |DailyExceptionDescrip|
.. _DailyException: pyrez.exceptions.RateLimitExceeded: |DailyExceptionDescrip|
.. |DailyExceptionDescrip| replace:: Raised when the daily request limit is reached.

.. |NONE| replace:: ``None``
.. |STR| replace:: :class:`str`
.. |INT| replace:: :class:`int`
.. |BOOL| replace:: :class:`bool`
.. |LIST| replace:: :class:`list`
.. |DICT| replace:: :class:`dict`
.. |TUPLE| replace:: :class:`tuple`
.. |FLOAT| replace:: :class:`float`

.. |PassingNone| replace:: Passing in |NONE| or an invalid value will use the default instead of the passed in value.

.. |MatchIdDescrip| replace:: The id of the match. Can be obtained from :meth:`getMatchHistory`, :meth:`getTopMatches` & :meth:`getMatchIds`.

.. |PrivacyMode| replace:: Any player with ``Privacy Mode`` enabled in-game will return a null dataset from methods that require a **playerId** or **playerName**.

.. |UsedForAuthentication| replace:: Used for authentication.

.. |AuthKey| replace:: This is the Authentication Key that you receive from Hi-Rez Studios.
.. |AuthKeyAtrib| replace:: |STR| – |AuthKey|
.. |AuthKeyConstruct| replace:: |UsedForAuthentication| |AuthKey|

.. |DevId| replace:: This is the Developer ID that you receive from Hi-Rez Studios.
.. |DevIdAtrib| replace:: |INT| – |DevId|
.. |DevIdConstruct| replace:: |UsedForAuthentication| |DevId|

.. |Format| replace:: The response format that will be used by default when making requests.
.. |FormatAtrib| replace:: :class:`.Format` – |Format|
.. |FormatConstruct| replace:: |Format| |PassingNone|

.. |Language| replace:: :class:`.Language`
.. |LanguageDescrip| replace:: The language that you want results returned in.
.. |LanguageEnglish| replace:: :class:`Language.English`
.. |LanguageParamDescrip| replace:: |LanguageDescrip| Passing in |NONE| will use |LanguageEnglish| instead of the passed in value.
.. |LanguageParam| replace:: Optional |INT| or |Language|

.. |TypeError| replace:: Raised when passing any parameters.
.. |TypeErrorA| replace:: Raised when more (or less) than 1 parameter is passed.
.. |TypeErrorB| replace:: Raised when more than 2 parameters or less than 1 parameter is passed.
.. |TypeErrorC| replace:: Raised when more than 3 parameters or less than 1 parameter is passed.

.. |CREDENTIALS| replace:: ``Credentials``
.. |WrongCredentials| replace:: Raised when a wrong |CREDENTIALS| is passed.
