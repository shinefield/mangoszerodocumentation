.. _db-world-game-weather:

=====================
"game\_weather" table
=====================

The ``game_weather`` table holds the percentages for weather changes in
various zones. For any given zone the percentage of all weather types
for each season, should total and not exceed 100%.

*Notice*: Not all zones can have their weather changed.

Table structure
---------------

+-------------------------+-------------------------+--------+-------+-----------+---------+
| Field                   | Type                    | Null   | Key   | Default   | Extra   |
+=========================+=========================+========+=======+===========+=========+
| zone                    | mediumint(8) unsigned   | NO     | PRI   | 0         |         |
+-------------------------+-------------------------+--------+-------+-----------+---------+
| spring\_rain\_chance    | tinyint(3) unsigned     | NO     |       | 25        |         |
+-------------------------+-------------------------+--------+-------+-----------+---------+
| spring\_snow\_chance    | tinyint(3) unsigned     | NO     |       | 25        |         |
+-------------------------+-------------------------+--------+-------+-----------+---------+
| spring\_storm\_chance   | tinyint(3) unsigned     | NO     |       | 25        |         |
+-------------------------+-------------------------+--------+-------+-----------+---------+
| summer\_rain\_chance    | tinyint(3) unsigned     | NO     |       | 25        |         |
+-------------------------+-------------------------+--------+-------+-----------+---------+
| summer\_snow\_chance    | tinyint(3) unsigned     | NO     |       | 25        |         |
+-------------------------+-------------------------+--------+-------+-----------+---------+
| summer\_storm\_chance   | tinyint(3) unsigned     | NO     |       | 25        |         |
+-------------------------+-------------------------+--------+-------+-----------+---------+
| fall\_rain\_chance      | tinyint(3) unsigned     | NO     |       | 25        |         |
+-------------------------+-------------------------+--------+-------+-----------+---------+
| fall\_snow\_chance      | tinyint(3) unsigned     | NO     |       | 25        |         |
+-------------------------+-------------------------+--------+-------+-----------+---------+
| fall\_storm\_chance     | tinyint(3) unsigned     | NO     |       | 25        |         |
+-------------------------+-------------------------+--------+-------+-----------+---------+
| winter\_rain\_chance    | tinyint(3) unsigned     | NO     |       | 25        |         |
+-------------------------+-------------------------+--------+-------+-----------+---------+
| winter\_snow\_chance    | tinyint(3) unsigned     | NO     |       | 25        |         |
+-------------------------+-------------------------+--------+-------+-----------+---------+
| winter\_storm\_chance   | tinyint(3) unsigned     | NO     |       | 25        |         |
+-------------------------+-------------------------+--------+-------+-----------+---------+

Fields
------

zone
----

A zone identifier. The value has to match with a zone identifier defined
in `AreaTable.dbc <../dbc/AreaTable.dbc>`__.

spring\_rain\_chance
--------------------

Percentage chance for rain in the Spring.

spring\_snow\_chance
--------------------

Percentage chance for snow in the Spring.

spring\_storm\_chance
---------------------

Percentage chance for a sand storm in the Spring.

summer\_rain\_chance
--------------------

Percentage chance for rain in the Summer.

summer\_snow\_chance
--------------------

Percentage chance for snow in the Summer.

summer\_storm\_chance
---------------------

Percentage chance for a sand storm in the Summer.

fall\_rain\_chance
------------------

Percentage chance for rain in the Fall.

fall\_snow\_chance
------------------

Percentage chance for snow in the Fall.

fall\_storm\_chance
-------------------

Percentage chance for storm in the Fall.

winter\_rain\_chance
--------------------

Percentage chance for rain in the Winter.

winter\_snow\_chance
--------------------

Percentage chance for snow in the Winter.

winter\_storm\_chance
---------------------

Percentage chance for storm in the Winter.
