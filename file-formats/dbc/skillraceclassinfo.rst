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
| 1    | ID               | Integer (signed)   | -         | Unique ID                             |
+------+------------------+--------------------+-----------+---------------------------------------+
| 2    | skillID          | Integer (signed)   | 0         | References the skill line.            |
+------+------------------+--------------------+-----------+---------------------------------------+
| 3    | raceMask         | Integer            | 0         | The race.                             |
+------+------------------+--------------------+-----------+---------------------------------------+
| 4    | classMask        | Integer            | 0         | The class.                            |
+------+------------------+--------------------+-----------+---------------------------------------+
| 5    | flags            | Integer            | 0         | See below.                            |
+------+------------------+--------------------+-----------+---------------------------------------+
| 6    | minLevel         | Integer            | 0         | Minimum Level to access this skill.   |
+------+------------------+--------------------+-----------+---------------------------------------+
| 7    | skillTierID      | Integer (signed)   | 0         | A skill tier.                         |
+------+------------------+--------------------+-----------+---------------------------------------+
| 8    | skillCostIndex   | Integer (signed)   | 0         | A cost index.                         |
+------+------------------+--------------------+-----------+---------------------------------------+

Fields
------

flags
-----

**TODO**

Relations
---------

-  ``skillID`` references the primary key of ``SkillLine.dbc``.
-  ``raceMask`` references the primary key of ``ChrRaces.dbc``.
-  ``classMask`` references the primary key of ``ChrClasses.dbc``.
-  ``skillTierID`` references the primary key of ``SkillTiers.dbc``.
-  ``skillCostIndex`` references the primary key of
   ``SkillCostsData.dbc``.

