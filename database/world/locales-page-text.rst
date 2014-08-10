.. _db-world-locales-page-text:

===========================
"locales\_page\_text" table
===========================

The ``locales_page_text`` table holds localized text strings for page
texts.

Table structure
---------------

+--------------+-------------------------+--------+-------+-----------+---------+
| Field        | Type                    | Null   | Key   | Default   | Extra   |
+==============+=========================+========+=======+===========+=========+
| entry        | mediumint(8) unsigned   | NO     | PRI   | 0         |         |
+--------------+-------------------------+--------+-------+-----------+---------+
| Text\_loc1   | longtext                | YES    |       | NULL      |         |
+--------------+-------------------------+--------+-------+-----------+---------+
| Text\_loc2   | longtext                | YES    |       | NULL      |         |
+--------------+-------------------------+--------+-------+-----------+---------+
| Text\_loc3   | longtext                | YES    |       | NULL      |         |
+--------------+-------------------------+--------+-------+-----------+---------+
| Text\_loc4   | longtext                | YES    |       | NULL      |         |
+--------------+-------------------------+--------+-------+-----------+---------+
| Text\_loc5   | longtext                | YES    |       | NULL      |         |
+--------------+-------------------------+--------+-------+-----------+---------+
| Text\_loc6   | longtext                | YES    |       | NULL      |         |
+--------------+-------------------------+--------+-------+-----------+---------+
| Text\_loc7   | longtext                | YES    |       | NULL      |         |
+--------------+-------------------------+--------+-------+-----------+---------+
| Text\_loc8   | longtext                | YES    |       | NULL      |         |
+--------------+-------------------------+--------+-------+-----------+---------+

Fields
------

entry
-----

This references the :doc:`page-text` tables unique ID for
which the entry is valid.

Text\_loc1
----------

*Korean* localization of ``Text`` in the :doc:`page-text`
table.

Text\_loc2
----------

*French* localization of ``Text`` in the :doc:`page-text`
table.

Text\_loc3
----------

*German* localization of ``Text`` in the :doc:`page-text`
table.

Text\_loc4
----------

*Chinese* localization of ``Text`` in the :doc:`page-text`
table.

Text\_loc5
----------

*Taiwanese* localization of ``Text`` in the :doc:`page-text`
table.

Text\_loc6
----------

*Spanish Spain* localization of ``Text`` in the
:doc:`page-text` table.

Text\_loc7
----------

*Spanish Latin America* localization of ``Text`` in the
:doc:`page-text` table.

Text\_loc8
----------

*Russian* localization of ``Text`` in the :doc:`page-text`
table.
