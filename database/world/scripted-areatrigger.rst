.. _db-world-scripted-areatrigger:

=============================
"scripted\_areatrigger" table
=============================

The ``scripted_areatrigger`` table holds informations for area trigger
which trigger a scripted event.

Table structure
---------------

+--------------+----------------+--------+-------+-----------+---------+
| Field        | Type           | Null   | Key   | Default   | Extra   |
+==============+================+========+=======+===========+=========+
| entry        | mediumint(8)   | NO     | PRI   | NULL      |         |
+--------------+----------------+--------+-------+-----------+---------+
| ScriptName   | char(64)       | NO     |       | NULL      |         |
+--------------+----------------+--------+-------+-----------+---------+

Fields
------

entry
-----

An areatrigger identifier. The value has to match with a areatrigger
identifier defined in :doc:`../../file-formats/dbc/areatrigger`.

ScriptName
----------

To assign a script from the script library to the area trigger, set this
string to the script's exported name.
