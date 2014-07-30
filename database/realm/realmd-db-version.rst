.. _db-realm-realmd-db-version:

===========================
"realmd\_db\_version" table
===========================

The ``realmd_db_version`` identifies the realm list data store to the
realm server by providing a bit field with a revision number/name
combination as name.

Table structure
---------------

+------------------------------------------+----------+--------+-------+-----------+---------+
| Field                                    | Type     | Null   | Key   | Default   | Extra   |
+==========================================+==========+========+=======+===========+=========+
| required\_z2426\_01\_realmd\_relations   | bit(1)   | YES    |       | NULL      |         |
+------------------------------------------+----------+--------+-------+-----------+---------+

Fields
------

Descriptions for each field with their meaning, usage and relations are
available below.

required\_z2426\_01\_realmd\_relations
--------------------------------------

This field is used to indicate the last database structure update
applied. Each applied update will renamed the field, in order to allow
users to select the required database upgrade query from the provided
upgrade queries.
