.. _file-formats-dbc-skillline:

=============
SkillLine.dbc
=============

The *skill line* table contains definitions for skills.

Skills include attributes, weapon skills, class skills, armor skills,
secondary skills, languages, professions and hidden skills.

Table structure
---------------

+------+----------------+----------------------+-----------+------------------------------------------------+
| ID   | Name           | Type                 | Default   | Description                                    |
+======+================+======================+===========+================================================+
| 1    | ID             | Integer              | -         | Unique ID                                      |
+------+----------------+----------------------+-----------+------------------------------------------------+
| 2    | category       | Integer (signed)     | 0         | References the skill line category.            |
+------+----------------+----------------------+-----------+------------------------------------------------+
| 3    | skillCosts     | Integer              | 0         | References the skill learning costs.           |
+------+----------------+----------------------+-----------+------------------------------------------------+
| 4    | displayName    | String (localized)   | -         | The name of the skill line.                    |
+------+----------------+----------------------+-----------+------------------------------------------------+
| 5    | description    | String (localized)   | -         | The description of the skill line.             |
+------+----------------+----------------------+-----------+------------------------------------------------+
| 6    | spellIcon      | Integer              | 0         | References the icon used for the skill line.   |
+------+----------------+----------------------+-----------+------------------------------------------------+

Relations
---------

-  ``category`` references the primary key of ``SkillLineCategory.dbc``.
-  ``skillCosts`` references the primary key of ``SkillCostsData.dbc``.
-  ``spellIcon`` references the primary key of ``SpellIcon.dbc``.
