.. _file-formats-dbc-taxipath:

============
TaxiPath.dbc
============

The *taxi path* table contains definitions for transports, including
source, destination and price.

Table structure
---------------

+------+-------------------------+--------------------+-----------+--------------------------------------+
| ID   | Name                    | Type               | Default   | Description                          |
+======+=========================+====================+===========+======================================+
| 1    | ID                      | Integer            | -         | Unique ID                            |
+------+-------------------------+--------------------+-----------+--------------------------------------+
| 2    | sourceTaxiNode          | Integer            | 0         | Where the transport starts.          |
+------+-------------------------+--------------------+-----------+--------------------------------------+
| 3    | destinationTaxiNode     | Integer            | 0         | Where the transport ends.            |
+------+-------------------------+--------------------+-----------+--------------------------------------+
| 4    | cost                    | Integer (signed)   | 0         | Price for the transport in copper.   |
+------+-------------------------+--------------------+-----------+--------------------------------------+

Relations
---------

-  ``sourceTaxiNode`` and ``destinationTaxiNode`` references the primary key of ``TaxiNodes.dbc``.
