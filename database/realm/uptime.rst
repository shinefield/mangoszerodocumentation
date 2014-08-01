.. _db-realm-uptime:

==============
"uptime" table
==============

The ``uptime`` table holds information on how long a specific
(registered) world server has been up and running.

Table structure
---------------

+---------------+------------------------+--------+-------+-----------+---------+
| Field         | Type                   | Null   | Key   | Default   | Extra   |
+===============+========================+========+=======+===========+=========+
| realmid       | int(11) unsigned       | NO     | PRI   | NULL      |         |
+---------------+------------------------+--------+-------+-----------+---------+
| starttime     | bigint(20) unsigned    | NO     | PRI   | 0         |         |
+---------------+------------------------+--------+-------+-----------+---------+
| startstring   | varchar(64)            | NO     |       |           |         |
+---------------+------------------------+--------+-------+-----------+---------+
| uptime        | bigint(20) unsigned    | NO     |       | 0         |         |
+---------------+------------------------+--------+-------+-----------+---------+
| maxplayers    | smallint(5) unsigned   | NO     |       | 0         |         |
+---------------+------------------------+--------+-------+-----------+---------+

Fields
------

Descriptions for each field with their meaning, usage and relations are
available below.

realmid
~~~~~~~

This references the :doc:`realmlist <realmlist>` tables unique ID of the
realm server for which the entry is valid.

starttime
~~~~~~~~~

The time when the server was started, in Unix time.

startstring
~~~~~~~~~~~

The time when the server was started, in string format. This does not
include the current time zone.

uptime
~~~~~~

The uptime of the server, in seconds.

maxplayers
~~~~~~~~~~

The maximum number of players connected.
