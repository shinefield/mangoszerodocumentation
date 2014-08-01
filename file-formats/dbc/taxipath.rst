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
| 1    | ID                      | Integer (signed)   | -         | Unique ID                            |
+------+-------------------------+--------------------+-----------+--------------------------------------+
| 2    | sourceTaxiNodeID        | Integer (signed)   | 0         | Where the transport starts.          |
+------+-------------------------+--------------------+-----------+--------------------------------------+
| 3    | destinationTaxiNodeID   | Integer (signed)   | 0         | Where the transport ends.            |
+------+-------------------------+--------------------+-----------+--------------------------------------+
| 4    | cost                    | Integer            | 0         | Price for the transport in copper.   |
+------+-------------------------+--------------------+-----------+--------------------------------------+

Relations
---------

-  ``sourceTaxiNodeID`` and ``destinationTaxiNodeID`` references the
   primary key of ``TaxiNodes.dbc``.
