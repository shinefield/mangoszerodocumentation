.. _file-formats-dbc-transportanimation:

======================
TransportAnimation.dbc
======================

The *transport animation* table contains definitions most likely used to
play animations during characters being on a transport.

Table structure
---------------

+------+-------------------+--------------------+-----------+--------------------------+
| ID   | Name              | Type               | Default   | Description              |
+======+===================+====================+===========+==========================+
| 1    | ID                | Integer (signed)   | -         | Unique ID                |
+------+-------------------+--------------------+-----------+--------------------------+
| 2    | transportID       | Integer (signed)   | 0         | **TODO**                 |
+------+-------------------+--------------------+-----------+--------------------------+
| 3    | timeIndex         | Integer            | 0         | **TODO**                 |
+------+-------------------+--------------------+-----------+--------------------------+
| 4    | locationX         | Float              | 0         | **TODO**                 |
+------+-------------------+--------------------+-----------+--------------------------+
| 5    | locationY         | Float              | 0         | **TODO**                 |
+------+-------------------+--------------------+-----------+--------------------------+
| 6    | locationZ         | Float              | 0         | **TODO**                 |
+------+-------------------+--------------------+-----------+--------------------------+
| 7    | AnimationDataID   | Integer (signed)   | 0         | The animation sequence   |
+------+-------------------+--------------------+-----------+--------------------------+

Relations
---------

-  ``AnimationDataID`` references the primary key of
   ``AnimationData.dbc``.
