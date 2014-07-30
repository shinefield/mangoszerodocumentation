.. _db-world-command:

===============
"command" table
===============

The ``command`` table holds help and security information for commands.
This table does NOT create new commands, it only sets / overrides
security and provides help.

Table structure
---------------

+------------+-----------------------+--------+-------+-----------+---------+
| Field      | Type                  | Null   | Key   | Default   | Extra   |
+============+=======================+========+=======+===========+=========+
| name       | varchar(50)           | NO     | PRI   |           |         |
+------------+-----------------------+--------+-------+-----------+---------+
| security   | tinyint(3) unsigned   | NO     |       | 0         |         |
+------------+-----------------------+--------+-------+-----------+---------+
| help       | longtext              | YES    |       | NULL      |         |
+------------+-----------------------+--------+-------+-----------+---------+

Fields
------

name
----

A unique name for the command.

security
--------

The security level required to use the command. This references the
`account <../realm/account>`__ tables ``gmlevel`` key.

help
----

The help text displayed by the ``.help`` command.
