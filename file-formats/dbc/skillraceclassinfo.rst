.. _file-formats-dbc-skillraceclassinfo:

======================
SkillRaceClassInfo.dbc
======================

The *skill race/class info* table contains definitions for which races /
classes have access to what skills.

Table structure
---------------

+------+------------------+--------------------+-----------+---------------------------------------+
| ID   | Name             | Type               | Default   | Description                           |
+======+==================+====================+===========+=======================================+
| 1    | ID               | Integer            | -         | Unique ID                             |
+------+------------------+--------------------+-----------+---------------------------------------+
| 2    | skill            | Integer            | 0         | References the skill line.            |
+------+------------------+--------------------+-----------+---------------------------------------+
| 3    | raceMask         | Integer (signed)   | 0         | The race.                             |
+------+------------------+--------------------+-----------+---------------------------------------+
| 4    | classMask        | Integer (signed)   | 0         | The class.                            |
+------+------------------+--------------------+-----------+---------------------------------------+
| 5    | flags            | Integer (signed)   | 0         | See below.                            |
+------+------------------+--------------------+-----------+---------------------------------------+
| 6    | minLevel         | Integer (signed)   | 0         | Minimum Level to access this skill.   |
+------+------------------+--------------------+-----------+---------------------------------------+
| 7    | skillTier        | Integer            | 0         | A skill tier.                         |
+------+------------------+--------------------+-----------+---------------------------------------+
| 8    | skillCostIndex   | Integer (signed)   | 0         | A cost index.                         |
+------+------------------+--------------------+-----------+---------------------------------------+

Fields
------

flags
~~~~~

**TODO**

Relations
---------

-  ``skill`` references the primary key of :doc:`skillline`.
-  ``raceMask`` references the primary key of :doc:`chrraces`.
-  ``classMask`` references the primary key of :doc:`chrclasses`.
-  ``skillTier`` references the primary key of :doc:`skilltiers`.
-  ``skillCostIndex`` references the primary key of :doc:`skillcostsdata`.
