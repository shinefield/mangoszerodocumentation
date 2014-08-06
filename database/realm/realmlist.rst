.. _db-realm-realmlist:

=================
"realmlist" table
=================

The ``realmlist`` table holds information on all registered world
servers.

Table structure
---------------

+------------------------+-----------------------+--------+-------+-------------+-------------------+
| Field                  | Type                  | Null   | Key   | Default     | Extra             |
+========================+=======================+========+=======+=============+===================+
| id                     | int(11) unsigned      | NO     | PRI   | NULL        | auto\_increment   |
+------------------------+-----------------------+--------+-------+-------------+-------------------+
| name                   | varchar(32)           | NO     | UNI   |             |                   |
+------------------------+-----------------------+--------+-------+-------------+-------------------+
| address                | varchar(32)           | NO     |       | 127.0.0.1   |                   |
+------------------------+-----------------------+--------+-------+-------------+-------------------+
| port                   | int(11)               | NO     |       | 8085        |                   |
+------------------------+-----------------------+--------+-------+-------------+-------------------+
| icon                   | tinyint(3) unsigned   | NO     |       | 0           |                   |
+------------------------+-----------------------+--------+-------+-------------+-------------------+
| realmflags             | tinyint(3) unsigned   | NO     |       | 2           |                   |
+------------------------+-----------------------+--------+-------+-------------+-------------------+
| timezone               | tinyint(3) unsigned   | NO     |       | 0           |                   |
+------------------------+-----------------------+--------+-------+-------------+-------------------+
| allowedSecurityLevel   | tinyint(3) unsigned   | NO     |       | 0           |                   |
+------------------------+-----------------------+--------+-------+-------------+-------------------+
| population             | float unsigned        | NO     |       | 0           |                   |
+------------------------+-----------------------+--------+-------+-------------+-------------------+
| realmbuilds            | varchar(64)           | NO     |       |             |                   |
+------------------------+-----------------------+--------+-------+-------------+-------------------+

Fields
------

Descriptions for each field with their meaning, usage and relations are
available below.

id
~~

The unique identifier for a realm server.

name
~~~~

The name to be displayed in the realm selection list.

address
~~~~~~~

A valid `IP address`_ at which the world server is accessible. This can
be a private IP address, like ``192.168.0.1``, but also a public IP address
if your world server is publicly accessible.

The realm list server will redirect connections after logging in and
selecting a realm to this IP address.

Please note, that the IP address configured here has to match with the
IP address you have configured in the world server configuration file.

port
~~~~

A valid port number on which this realm server listens to connections.

icon
~~~~

The type of realm server.

Valid values are:

-  ``0``: Normal
-  ``1``: PvP
-  ``6``: RP
-  ``8``: RP PvP

realmflags
----------
Realm flags allow the users to highlight realms for certain situations.

-  ``2``: Marks the realm as offline
-  ``4``: Shows the realms supported version in realm list
-  ``32``: Highlight realm for new players
-  ``64``: Marks realm as recommended

timezone
~~~~~~~~

The realm time-zone, it will be displayed in the tabs of the realm list.

Valid values are:

- ``1``: United States (default)
- ``2``: Korea
- ``3``: English
- ``3``: German
- ``3``: French
- ``4``: Taiwan
- ``5``: China
- ``99``: Test Server
- ``101``: QA Server

allowedSecurityLevel
~~~~~~~~~~~~~~~~~~~~

The minimum :doc:`account <account>` ``gmlevel`` required for accounts to
log in to this realm. Changing this value will automatically update the
visible in-game realm list, but the realm server must be restarted for
it to take effect.

population
~~~~~~~~~~

This field is automatically updated at regular intervals and will have
the current population.

The formula to calculate the value in this field is:

.. math::

    playerCount / maxPlayerCount * 2

In the realm list in-game, the thresholds for low, medium and high
population are 0.5, 1.0 and 2.0 respectively.

realmbuilds
~~~~~~~~~~~

Accepted Client version for the realm, in form of comma separated value.

.. _IP address: http://en.wikipedia.org/wiki/IP_address
