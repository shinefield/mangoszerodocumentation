.. _db-world-locales-creature:

=========================
"locales\_creature" table
=========================

The ``locales_creature`` table holds localized text strings for creature
templates.

Table structure
---------------

+-----------------+-------------------------+--------+-------+-----------+---------+
| Field           | Type                    | Null   | Key   | Default   | Extra   |
+=================+=========================+========+=======+===========+=========+
| entry           | mediumint(8) unsigned   | NO     | PRI   | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| name\_loc1      | varchar(100)            | NO     |       |           |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| name\_loc2      | varchar(100)            | NO     |       |           |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| name\_loc3      | varchar(100)            | NO     |       |           |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| name\_loc4      | varchar(100)            | NO     |       |           |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| name\_loc5      | varchar(100)            | NO     |       |           |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| name\_loc6      | varchar(100)            | NO     |       |           |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| name\_loc7      | varchar(100)            | NO     |       |           |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| name\_loc8      | varchar(100)            | NO     |       |           |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| subname\_loc1   | varchar(100)            | YES    |       | NULL      |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| subname\_loc2   | varchar(100)            | YES    |       | NULL      |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| subname\_loc3   | varchar(100)            | YES    |       | NULL      |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| subname\_loc4   | varchar(100)            | YES    |       | NULL      |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| subname\_loc5   | varchar(100)            | YES    |       | NULL      |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| subname\_loc6   | varchar(100)            | YES    |       | NULL      |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| subname\_loc7   | varchar(100)            | YES    |       | NULL      |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| subname\_loc8   | varchar(100)            | YES    |       | NULL      |         |
+-----------------+-------------------------+--------+-------+-----------+---------+

Fields
------

entry
-----

This references the :doc:`creature-template` tables
unique ID for which the entry is valid.

name\_loc1
----------

*Korean* localization of ``name`` in the
:doc:`creature-template` table.

name\_loc2
----------

*French* localization of ``name`` in the
:doc:`creature-template` table.

name\_loc3
----------

*German* localization of ``name`` in the
:doc:`creature-template` table.

name\_loc4
----------

*Chinese* localization of ``name`` in the
:doc:`creature-template` table.

name\_loc5
----------

*Taiwanese* localization of ``name`` in the
:doc:`creature-template` table.

name\_loc6
----------

*Spanish Spain* localization of ``name`` in the
:doc:`creature-template` table.

name\_loc7
----------

*Spanish Latin America* localization of ``name`` in the
:doc:`creature-template` table.

name\_loc8
----------

*Russian* localization of ``name`` in the
:doc:`creature-template` table.

subname\_loc1
-------------

*Korean* localization of ``subname`` in the
:doc:`creature-template` table.

subname\_loc2
-------------

*French* localization of ``subname`` in the
:doc:`creature-template` table.

subname\_loc3
-------------

*German* localization of ``subname`` in the
:doc:`creature-template` table.

subname\_loc4
-------------

*Chinese* localization of ``subname`` in the
:doc:`creature-template` table.

subname\_loc5
-------------

*Taiwanese* localization of ``subname`` in the
:doc:`creature-template` table.

subname\_loc6
-------------

*Spanish Spain* localization of ``subname`` in the
:doc:`creature-template` table.

subname\_loc7
-------------

*Spanish Latin America* localization of ``subname`` in the
:doc:`creature-template` table.

subname\_loc8
-------------

*Russian* localization of ``subname`` in the
:doc:`creature-template` table.
