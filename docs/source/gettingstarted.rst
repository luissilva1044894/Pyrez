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

+----------------+----------------------------------+
|     devId      |             authKey              |
+================+==================================+
|     1004       | 23DF3C7E9BD14D84BF892AD206B6755C |
+----------------+----------------------------------+


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

.. raw:: html

   <ul class="simple">
        <li>
            <p><strong>devId</strong> (<a class="reference external" href="https://docs.python.org/3/library/functions.html#int" title="(in Python v3.7)" target="_blank"><code class="xref py py-class docutils literal notranslate"><span class="pre">int</span></code></a>) – This is the Developer ID that you receive from Hi-Rez Studios.
            </p>
        </li>
        <li>
            <p><strong>authKey</strong> (<a class="reference external" href="https://docs.python.org/3/library/functions.html#func-str" title="(in Python v3.7)" target="_blank"><code class="xref py py-class docutils literal notranslate"><span class="pre">str</span></code></a>) – This is the Authentication Key that you receive from Hi-Rez Studios.
            </p>
        </li>
        <li>
            <p><strong>responseFormat</strong> (Optional[<a class="reference internal" href="https://github.com/luissilva1044894/Pyrez/blob/master/pyrez/enumerations/Format.py#L2" title="Format class definition" target="_blank"><code class="xref py py-class docutils literal notranslate"><span class="pre">Format</span></code></a>]) – The response format that will be used by default when making requests. Passing in <cite><a class="reference external" href="https://docs.python.org/3/library/constants.html#None" title="(in Python v3.7)" target="_blank"><code class="xref py py-class docutils literal notranslate"><span class="pre">None</span></code></a></cite> or an invalid value will use the default instead of the passed in value.
            </p>
        </li>
        <li>
            <p><strong>sessionId</strong> (Optional[<a class="reference external" href="https://docs.python.org/3/library/functions.html#func-str" title="(in Python v3.7)" target="_blank"><code class="xref py py-class docutils literal notranslate"><span class="pre">str</span></code></a>]) – Manually sets an active sessionId. Passing in <cite><a class="reference external" href="https://docs.python.org/3/library/constants.html#None" title="(in Python v3.7)" target="_blank"><code class="xref py py-class docutils literal notranslate"><span class="pre">None</span></code></a></cite> or an invalid value will use the default instead of the passed in value.
            </p>
        </li>
        <li>
            <p><strong>storeSession</strong> (Optional[<a class="reference external" href="https://docs.python.org/3/library/functions.html#bool" title="(in Python v3.7)" target="_blank"><code class="xref py py-class docutils literal notranslate"><span class="pre">bool</span></code></a>]) – Allows Pyrez to read and store sessionId in a <cite>.json</cite> file.
            </p>
        </li>
    </ul>

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