.. _db-world-battlemaster-entry:

===========================
"battlemaster\_entry" table
===========================

The ``battlemaster_entry`` table holds informations on creatures that
can start battlegrounds.

Table structure
---------------

+----------------+-------------------------+--------+-------+-----------+---------+
| Field          | Type                    | Null   | Key   | Default   | Extra   |
+================+=========================+========+=======+===========+=========+
| entry          | mediumint(8) unsigned   | NO     | PRI   | 0         |         |
+----------------+-------------------------+--------+-------+-----------+---------+
| bg\_template   | mediumint(8) unsigned   | NO     |       | 0         |         |
+----------------+-------------------------+--------+-------+-----------+---------+

Fields
------

entry
-----

This references the `creature\_template <creature_template>`__ tables
unique ID for which the entry is valid.

bg\_template
------------

This references the `battleground\_template <battleground_template>`__
tables unique ID for which the entry is valid.
