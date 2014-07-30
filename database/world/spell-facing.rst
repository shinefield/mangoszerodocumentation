.. _db-world-spell-facing:

=====================
"spell\_facing" table
=====================

The ``spell_facing`` table holds information if a caster needs to face
the target when casting a spell.

Table structure
---------------

+--------------------+--------------------+--------+-------+-----------+---------+
| Field              | Type               | Null   | Key   | Default   | Extra   |
+====================+====================+========+=======+===========+=========+
| entry              | int(11) unsigned   | NO     | PRI   | 0         |         |
+--------------------+--------------------+--------+-------+-----------+---------+
| facingcasterflag   | tinyint(1)         | NO     |       | 1         |         |
+--------------------+--------------------+--------+-------+-----------+---------+

Fields
------

entry
-----

The spell identifier. The value has to match with a spell identifier
defined in `Spell.dbc <../dbc/Spell.dbc>`__.

facingcasterflag
----------------

If the referenced spell requires to be cast when facing the target, this
field has to be set to ``1``.

*Notice*: setting this to zero would disable the need to face the
target.
