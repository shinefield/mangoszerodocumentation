.. _db-script-sd2-db-version:

========================
"sd2\_db\_version" table
========================

The ``sd2_db_version`` table holds version information for the script
library database to help users identify which release they have
installed.

Table structure
---------------

+-----------+----------------+--------+-------+-----------+---------+
| Field     | Type           | Null   | Key   | Default   | Extra   |
+===========+================+========+=======+===========+=========+
| version   | varchar(255)   | NO     |       |           |         |
+-----------+----------------+--------+-------+-----------+---------+

Fields
------

version
-------

A string describing the version of the script library database.
