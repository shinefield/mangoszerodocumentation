.. _db-world-mangos-string:

======================
"mangos\_string" table
======================

The ``mangos_string`` table holds strings used internally by the server
to allow translations.

Table structure
---------------

+--------------------+-------------------------+--------+-------+-----------+---------+
| Field              | Type                    | Null   | Key   | Default   | Extra   |
+====================+=========================+========+=======+===========+=========+
| entry              | mediumint(8) unsigned   | NO     | PRI   | 0         |         |
+--------------------+-------------------------+--------+-------+-----------+---------+
| content\_default   | text                    | NO     |       | NULL      |         |
+--------------------+-------------------------+--------+-------+-----------+---------+
| content\_loc1      | text                    | YES    |       | NULL      |         |
+--------------------+-------------------------+--------+-------+-----------+---------+
| content\_loc2      | text                    | YES    |       | NULL      |         |
+--------------------+-------------------------+--------+-------+-----------+---------+
| content\_loc3      | text                    | YES    |       | NULL      |         |
+--------------------+-------------------------+--------+-------+-----------+---------+
| content\_loc4      | text                    | YES    |       | NULL      |         |
+--------------------+-------------------------+--------+-------+-----------+---------+
| content\_loc5      | text                    | YES    |       | NULL      |         |
+--------------------+-------------------------+--------+-------+-----------+---------+
| content\_loc6      | text                    | YES    |       | NULL      |         |
+--------------------+-------------------------+--------+-------+-----------+---------+
| content\_loc7      | text                    | YES    |       | NULL      |         |
+--------------------+-------------------------+--------+-------+-----------+---------+
| content\_loc8      | text                    | YES    |       | NULL      |         |
+--------------------+-------------------------+--------+-------+-----------+---------+

Fields
------

entry
-----

The ID that the core uses to identify a string. These IDs are contained
and used internally and need to correspond to what the core expects.

.. note::

    The core will not operate if strings are missing from this table.

content\_default
----------------

The English translation.

.. note::

    the ``%`` arguments need to be used in the exact same order for any translation.

content\_loc1
-------------

*Korean* localization of ``content_default``.

content\_loc2
-------------

*French* localization of ``content_default``.

content\_loc3
-------------

*German* localization of ``content_default``.

content\_loc4
-------------

*Chinese* localization of ``content_default``.

content\_loc5
-------------

*Taiwanese* localization of ``content_default``.

content\_loc6
-------------

*Spanish Spain* localization of ``content_default``.

content\_loc7
-------------

*Spanish Latin America* localization of ``content_default``.

content\_loc8
-------------

*Russian* localization of ``content_default``.
