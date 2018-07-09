Pyrez: Easily way to connect to Hi-Rez API
=========================

.. image:: https://img.shields.io/pypi/v/pyrez.svg
    :target: https://pypi.org/project/pyrez

.. image:: https://readthedocs.org/projects/pyrez/badge/?version=latest
    :target: http://pyrez.readthedocs.io/en/latest/?badge=latest

.. image:: https://img.shields.io/badge/license-MIT-green.svg
    :target: https://github.com/luissilva1044894/Pyrez/blob/master/LICENSE

.. image:: https://img.shields.io/pypi/pyversions/pyrez.svg
    :target: https://pypi.org/project/pyrez

.. image:: https://img.shields.io/github/contributors/luissilva1044894/Pyrez.svg
    :target: https://github.com/luissilva1044894/Pyrez/graphs/contributors

**PyRez** is an open-source Python-based wrapper for `Hi-Rez <http://www.hirezstudios.com>`_ API that supports `*Paladins* <https://www.paladins.com>`_, `*Realm Royale* <https://github.com/apugh/realm-api-proposal/wiki>`_ and `*Smite* <https://www.smitegame.com>`_.

Requeriments
------------

Requests is ready for today's web.

- `Python <http://python.org>`_ 3.5 (or higher)
    - The following libraries are required: `*Requests* <https://pypi.org/project/requests>`_ and *requests-aeaweb*
- `Access <https://fs12.formsite.com/HiRez/form48/secure_index.html>`_ to Hi-Rez Studios' API

Installation
------------

The easiest way to install **Pyrez** is using *pip*, Python's package manager:

.. code-block:: bash

    pip install -U pyrez

The required dependencies will be installed automatically.
After that, you can use the library using:

.. code-block:: python

    import pyrez

Documentation
-------------

Official documentation is available at http://pyrez.readthedocs.io/en/latest/?badge=latest.


Example
-------

.. code-block:: python
    from pyrez.api import PaladinsAPI

    paladinsAPI = PaladinsAPI (devId=1004, authKey="23DF3C7E9BD14D84BF892AD206B6755C")
    championsRank = paladinsAPI.getGodRanks ("FeyRazzle")

    if championsRank is not None:
        for championRank in championsRank:
            print(championRank.getWinratio ())

This example will print the winrate with every `Champion <https://www.paladins.com/champions>`_ of player **`FeyRazzle <https://twitch.tv/FeyRazzle>`_**.
