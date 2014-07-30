.. _db-world-scripted-event:

=======================
"scripted\_event" table
=======================

The ``scripted_event`` table holds informations for spells which trigger
a scripted event.

This only applies to spells which have a SPELL\_EFFECT\_SEND\_EVENT
effect.

Table structure
---------------

+--------------+----------------+--------+-------+-----------+---------+
| Field        | Type           | Null   | Key   | Default   | Extra   |
+==============+================+========+=======+===========+=========+
| id           | mediumint(8)   | NO     | PRI   | NULL      |         |
+--------------+----------------+--------+-------+-----------+---------+
| ScriptName   | char(64)       | NO     |       | NULL      |         |
+--------------+----------------+--------+-------+-----------+---------+

Fields
------

id
--

The spell effect identifier given as parameter for the
SPELL\_EFFECT\_SEND\_EVENT effect.

ScriptName
----------

To assign a script from the script library to the scripted event, set
this string to the script's exported name.
