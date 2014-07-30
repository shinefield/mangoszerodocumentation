.. _db-world-pet-name-generation:

=============================
"pet\_name\_generation" table
=============================

The ``pet_name_generation`` table holds available pieces for server
generated pet names, including first and last half of the name.

Table structure
---------------

+---------+-------------------------+--------+-------+-----------+-------------------+
| Field   | Type                    | Null   | Key   | Default   | Extra             |
+=========+=========================+========+=======+===========+===================+
| id      | mediumint(8) unsigned   | NO     | PRI   | NULL      | auto\_increment   |
+---------+-------------------------+--------+-------+-----------+-------------------+
| word    | tinytext                | NO     |       | NULL      |                   |
+---------+-------------------------+--------+-------+-----------+-------------------+
| entry   | mediumint(8) unsigned   | NO     |       | 0         |                   |
+---------+-------------------------+--------+-------+-----------+-------------------+
| half    | tinyint(4)              | NO     |       | 0         |                   |
+---------+-------------------------+--------+-------+-----------+-------------------+

Fields
------

id
--

The unique identifier for the entry.

word
----

The actual name part for the entry.

entry
-----

The creature for which this name fragment should apply. This references
the `creature\_template <creature_template>`__ tables unique ID.

half
----

A flag signalling if the name fragment is intended for the first of the
last half of the name.

+---------+---------------+
| Value   | Description   |
+=========+===============+
| 0       | First half    |
+---------+---------------+
| 1       | Last half     |
+---------+---------------+

