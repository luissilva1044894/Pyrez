Registration
----------------

A `Credentials`_ that will provide access to Hi-Rez Studios API.

If you don't already have a Credentials, `click here`_ to become
developer.

If your application is accepted, you will receive an e-mail from Hi-Rez
Studios containing your personal `Credentials`_ within a few
days.

Credentials
---------------
To access the API you'll need your own set of Credentials which consist of a Developer ID (devId) and an Authentication Key (authKey).

Here are the Credentials for a sample account:

=======  ==================================
 devId                  authKey
-------  ----------------------------------
  1004    23DF3C7E9BD14D84BF892AD206B6755C
=======  ==================================

Importing
-------------

.. code:: py

   import pyrez
   import pyrez.api
   from pyrez.api import PaladinsAPI, SmiteAPI, RealmRoyaleAPI
   import pyrez.enumerations
   import pyrez.models

Creating API object
---------------------

.. code:: py

   paladins = PaladinsAPI(options)

   #or
   smite = SmiteAPI(options)

   #or
   reamlRoyale = RealmRoyaleAPI(options)

Options can have the following fields:

- devId (|INT|) – |DevId|
- authKey (|STR|) – |AuthKey|
- responseFormat (:class:`.Format`) – |Format|
- sessionId (|STR|) – |Format|
- storeSession (|STR|) – Allows Pyrez to read and store sessionId in a .json file.

Sessions
--------

Sessions are created automatically and self-managed by Pyrez so you really don't need to initialise / call this method directly. However, you can set it manually or even request a new Session.

Manually:

.. code:: py

    paladins = PaladinsAPI(devId=1004, authKey="23DF3C7E9BD14D84BF892AD206B6755C", sessionId="1465AFCA32DBDB800CEF8C72F296C52C")

Requesting a new Session:

.. code:: py

    paladins = PaladinsAPI(devId=1004, authKey="23DF3C7E9BD14D84BF892AD206B6755C")
    session = paladins._createSession()
    print(session.sessionId)

.. _Credentials: #credentials
.. _click here: https://fs12.formsite.com/HiRez/form48/secure_index.html