.. _file-formats-dbc-camerashakes:

================
CameraShakes.dbc
================

The *camera shakes* table contains definitions for shaking the game
camera when certain spells are cast.

Table structure
---------------

+------+---------------+--------------------+-----------+---------------+
| ID   | Name          | Type               | Default   | Description   |
+======+===============+====================+===========+===============+
| 1    | ID            | Integer            | -         | Unique ID     |
+------+---------------+--------------------+-----------+---------------+
| 2    | shakeType     | Integer (signed)   | 0         | See below.    |
+------+---------------+--------------------+-----------+---------------+
| 3    | direction     | Integer (signed)   | 0         | See below.    |
+------+---------------+--------------------+-----------+---------------+
| 4    | amplitude     | Float              | 0         | **TODO**      |
+------+---------------+--------------------+-----------+---------------+
| 5    | frequency     | Float              | 0         | **TODO**      |
+------+---------------+--------------------+-----------+---------------+
| 6    | duration      | Float              | 0         | **TODO**      |
+------+---------------+--------------------+-----------+---------------+
| 7    | phase         | Float              | 0         | **TODO**      |
+------+---------------+--------------------+-----------+---------------+
| 8    | coefficient   | Float              | 0         | **TODO**      |
+------+---------------+--------------------+-----------+---------------+

Fields
------

shakeType
~~~~~~~~~

It is assumed that this flag describes either different variants of
camera shaking, or that it is a boolean flag telling if the camera
*should* be shaken.

-  ``0``: **TODO**,
-  ``1``: **TODO**.

direction
~~~~~~~~~

This flag seems to indicate the direction towards which a camera shake
will point.

-  ``0``: **TODO**,
-  ``1``: **TODO**,
-  ``2``: **TODO**.
