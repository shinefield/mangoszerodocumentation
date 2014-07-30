.. _db-realm-realmcharacters:

=======================
"realmcharacters" table
=======================

The ``realmcharacters`` table holds information on how many characters
an account has on a specific realm.

Table structure
---------------

+------------+-----------------------+--------+-------+-----------+---------+
| Field      | Type                  | Null   | Key   | Default   | Extra   |
+============+=======================+========+=======+===========+=========+
| realmid    | int(11) unsigned      | NO     | PRI   | 0         |         |
+------------+-----------------------+--------+-------+-----------+---------+
| acctid     | int(11) unsigned      | NO     | PRI   | NULL      |         |
+------------+-----------------------+--------+-------+-----------+---------+
| numchars   | tinyint(3) unsigned   | NO     |       | 0         |         |
+------------+-----------------------+--------+-------+-----------+---------+

Fields
------

Descriptions for each field with their meaning, usage and relations are
available below.

realmid
-------

This references the `realmlist <realmlist>`__ tables unique ID of the
realm server for which the entry is valid.

acctid
------

This references the `account <account>`__ tables unique ID of the user
account for which the entry is valid.

numchars
--------

This field contains the number of characters stored on a realm for the
account.
