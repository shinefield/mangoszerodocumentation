.. _file-formats-dbc-zoneintromusictable:

=======================
ZoneIntroMusicTable.dbc
=======================

The *zone intro music* table contains definitions for ambience sounds to
be played upon entering various areas.

Table structure
---------------

+------+-------------------+--------------------+-----------+-------------------------------------------------------------------------------------+
| ID   | Name              | Type               | Default   | Description                                                                         |
+======+===================+====================+===========+=====================================================================================+
| 1    | ID                | Integer            | -         | Unique ID                                                                           |
+------+-------------------+--------------------+-----------+-------------------------------------------------------------------------------------+
| 2    | name              | String             | 0         | The name of the ambience sound.                                                     |
+------+-------------------+--------------------+-----------+-------------------------------------------------------------------------------------+
| 3    | introSound        | Integer            | 0         | The sound entry being played upon entering an area.                                 |
+------+-------------------+--------------------+-----------+-------------------------------------------------------------------------------------+
| 4    | priority          | Integer            | 1         | See below.                                                                          |
+------+-------------------+--------------------+-----------+-------------------------------------------------------------------------------------+
| 5    | minDelay          | Integer            | 10        | The number of seconds playing the intro music will be delayed upon zone entering.   |
+------+-------------------+--------------------+-----------+-------------------------------------------------------------------------------------+

Fields
------

priority
~~~~~~~~

-  ``0``: no priority over default ambience sound.
-  ``1``: has priority over default ambience sound.

Relations
---------

-  ``introSound`` references the primary key of :doc:`soundentries`.
