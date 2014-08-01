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
| 1    | ID             | Integer (signed)   | -         | Unique ID                                      |
+------+----------------+--------------------+-----------+------------------------------------------------+
| 2    | flags          | Integer            | 0         | **TODO**                                       |
+------+----------------+--------------------+-----------+------------------------------------------------+
| 3    | foleySoundID   | Integer (signed)   | 0         | References to sound to use for the material.   |
+------+----------------+--------------------+-----------+------------------------------------------------+

Fields
------

flags
-----

**TODO**

Relations
---------

-  ``foleySoundID`` references the primary key of ``SoundEntries.dbc``.

