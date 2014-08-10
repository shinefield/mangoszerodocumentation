.. _file-formats-dbc-material:

============
Material.dbc
============

The *material* table contains definitions for sound to be made by
specific materials.

Table structure
---------------

+------+----------------+--------------------+-----------+------------------------------------------------+
| ID   | Name           | Type               | Default   | Description                                    |
+======+================+====================+===========+================================================+
| 1    | ID             | Integer            | -         | Unique ID                                      |
+------+----------------+--------------------+-----------+------------------------------------------------+
| 2    | flags          | Integer (signed)   | 0         | **TODO**                                       |
+------+----------------+--------------------+-----------+------------------------------------------------+
| 3    | foleySound     | Integer            | 0         | References to sound to use for the material.   |
+------+----------------+--------------------+-----------+------------------------------------------------+

Fields
------

flags
~~~~~

**TODO**

Relations
---------

-  ``foleySound`` references the primary key of :doc:`soundentries`.
