.. _db-world-reserved-name:

======================
"reserved\_name" table
======================

The ``reserved_name`` table holds possible character names which may not
be used by characters with no special rights.

*Notice*: any character with any access level bigger than default player
level may create a character using a reserved name.

Table structure
---------------

+---------+---------------+--------+-------+-----------+---------+
| Field   | Type          | Null   | Key   | Default   | Extra   |
+=========+===============+========+=======+===========+=========+
| name    | varchar(12)   | NO     | PRI   |           |         |
+---------+---------------+--------+-------+-----------+---------+

Fields
------

name
----

The name to disallow for characters created on normal player accounts.
