.. _file-formats-dbc-talenttab:

=============
TalentTab.dbc
=============

The *talent tab* table contains definitions for the class talent tabs as
seen ingame on the talent window.

Table structure
---------------

+------+------------------+----------------------+-----------+-----------------------------------------------------------------------------------------+
| ID   | Name             | Type                 | Default   | Description                                                                             |
+======+==================+======================+===========+=========================================================================================+
| 1    | ID               | Integer              | -         | Unique ID                                                                               |
+------+------------------+----------------------+-----------+-----------------------------------------------------------------------------------------+
| 2    | name             | String (localized)   | -         | The name of the talent tree.                                                            |
+------+------------------+----------------------+-----------+-----------------------------------------------------------------------------------------+
| 3    | spellIcon        | Integer              | 0         | The talent tree's icon.                                                                 |
+------+------------------+----------------------+-----------+-----------------------------------------------------------------------------------------+
| 4    | raceMask         | Integer (signed)     | 0         | The race(s) to which the talent tab applies, might not be ID, but rather masked ID.     |
+------+------------------+----------------------+-----------+-----------------------------------------------------------------------------------------+
| 5    | classMask        | Integer (signed)     | 0         | The class(es) to which the talent tab applies, might not be ID, but rather masked ID.   |
+------+------------------+----------------------+-----------+-----------------------------------------------------------------------------------------+
| 6    | orderIndex       | Integer              | 0         | An order for the tab.                                                                   |
+------+------------------+----------------------+-----------+-----------------------------------------------------------------------------------------+
| 7    | backgroundFile   | String               | 0         | The base name of the talent trees' background image.                                    |
+------+------------------+----------------------+-----------+-----------------------------------------------------------------------------------------+

Relations
---------

-  ``raceMask`` reference the primary key of :doc:`chrraces`.
-  ``classMask`` reference the primary key of :doc:`chrclasses`.
-  ``spellIcon`` reference the primary key of :doc:`spellicon`.

Notes
-----

The ``backgroundFile`` column only references the base name of the
talent tree's background image. The full image is contained in
``Interface\TalentFrame\``, split into four parts, named
``backgroundFile-BottomLeft``, ``backgroundFile-TopLeft``,
``backgroundFile-TopRight``, and ``backgroundFile-BottomRight``.
