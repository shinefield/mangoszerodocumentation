.. _db-world-db-version:

===================
"db\_version" table
===================

The ``db_version`` identifies the realm server data store to the
*mangos-zero server* by prodiving a bit field with a revision
number/name combination as name.

Table structure
---------------

+-----------------------------------------------------------------------+----------------+--------+-------+-----------+---------+
| Field                                                                 | Type           | Null   | Key   | Default   | Extra   |
+=======================================================================+================+========+=======+===========+=========+
| version                                                               | varchar(120)   | YES    | PRI   | NULL      |         |
+-----------------------------------------------------------------------+----------------+--------+-------+-----------+---------+
| creature\_ai\_version                                                 | varchar(120)   | YES    |       | NULL      |         |
+-----------------------------------------------------------------------+----------------+--------+-------+-----------+---------+
| required\_z2482\_s2128\_12654\_01\_mangos\_creature\_template_power   | bit(1)         | YES    |       | NULL      |         |
+-----------------------------------------------------------------------+----------------+--------+-------+-----------+---------+

Fields
------

Descriptions for each field with their meaning, usage and relations are
available below.

version
-------

A version string, describing the release version of the database
content.

creature\_ai\_version
---------------------

A version string, describing the release version of the scripted
creature AI.

required\_z2482\_s2128\_12654\_01\_mangos\_creature\_template_power
-------------------------------------------------------------------

This field is used to indicate the last database structure update
applied. Each applied update will renamed the field, in order to allow
users to select the required database upgrade query from the provided
upgrade queries.
