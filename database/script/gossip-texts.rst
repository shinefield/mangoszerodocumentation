.. _db-script-gossip-texts:

=====================
"gossip\_texts" table
=====================

The ``gossip_texts`` table holds gossip texts assigned to scripted
creatures.

Table structure
---------------

+--------------------+----------------+--------+-------+-----------+---------+
| Field              | Type           | Null   | Key   | Default   | Extra   |
+====================+================+========+=======+===========+=========+
| entry              | mediumint(8)   | NO     | PRI   | NULL      |         |
+--------------------+----------------+--------+-------+-----------+---------+
| content\_default   | text           | NO     |       | NULL      |         |
+--------------------+----------------+--------+-------+-----------+---------+
| content\_loc1      | text           | YES    |       | NULL      |         |
+--------------------+----------------+--------+-------+-----------+---------+
| content\_loc2      | text           | YES    |       | NULL      |         |
+--------------------+----------------+--------+-------+-----------+---------+
| content\_loc3      | text           | YES    |       | NULL      |         |
+--------------------+----------------+--------+-------+-----------+---------+
| content\_loc4      | text           | YES    |       | NULL      |         |
+--------------------+----------------+--------+-------+-----------+---------+
| content\_loc5      | text           | YES    |       | NULL      |         |
+--------------------+----------------+--------+-------+-----------+---------+
| content\_loc6      | text           | YES    |       | NULL      |         |
+--------------------+----------------+--------+-------+-----------+---------+
| content\_loc7      | text           | YES    |       | NULL      |         |
+--------------------+----------------+--------+-------+-----------+---------+
| content\_loc8      | text           | YES    |       | NULL      |         |
+--------------------+----------------+--------+-------+-----------+---------+
| comment            | text           | YES    |       | NULL      |         |
+--------------------+----------------+--------+-------+-----------+---------+

Fields
------

entry
~~~~~

The unique identifier of the gossip text entry. Identifiers here have to
match with the identifier set in the string using the text.

.. note::

    identifiers use a fixed format of ``-3<map-identifier><three-digit-counter>``.

content\_default
~~~~~~~~~~~~~~~~

The default text to be displayed in English.

content\_loc1
~~~~~~~~~~~~~

*Korean* localization of ``content_default``.

content\_loc2
~~~~~~~~~~~~~

*French* localization of ``content_default``.

content\_loc3
~~~~~~~~~~~~~

*German* localization of ``content_default``.

content\_loc4
~~~~~~~~~~~~~

*Chinese* localization of ``content_default``.

content\_loc5
~~~~~~~~~~~~~

*Taiwanese* localization of ``content_default``.

content\_loc6
~~~~~~~~~~~~~

*Spanish Spain* localization of ``content_default``.

content\_loc7
~~~~~~~~~~~~~

*Spanish Latin America* localization of ``content_default``.

content\_loc8
~~~~~~~~~~~~~

*Russian* localization of ``content_default``.

comment
~~~~~~~

Comments should always reflect where a gossip text will be used. Usually
a creature's name to which the gossip is added should be mentioned, and
the variable given to the gossip in the script using it.
