
.. |coro| replace:: This function is a |corourl|_.
.. |corourl| replace:: *coroutine*
.. _corourl: https://docs.python.org/3/library/asyncio-task.html#coroutine

.. _PaladinsGame: https://www.paladins.com/
.. _RealmRoyale: https://www.realmroyale.com/
.. _SmiteGame: https://www.smitegame.com/

.. |DailyException| replace:: pyrez.exceptions.DailyLimit: |DailyExceptionDescrip|
.. _DailyException: pyrez.exceptions.DailyLimit: |DailyExceptionDescrip|
.. |DailyExceptionDescrip| replace:: Raised when the daily request limit is reached.

.. |NONE| replace:: ``None``
.. |STR| replace:: :class:`str`
.. |INT| replace:: :class:`int`
.. |BOOL| replace:: :class:`bool`
.. |LIST| replace:: :class:`list`
.. |TUPLE| replace:: :class:`tuple`

.. |PassingNone| replace:: Passing in |NONE| or an invalid value will use the default instead of the passed in value.

.. |MatchIdDescrip| replace:: The id of the match. Can be obtained from getMatchHistory(), getTopMatches() & getMatchIds().

.. |PrivacyMode| replace:: Any player with ``Privacy Mode`` enabled in-game will return a null dataset from methods that require a playerId or playerName.

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
