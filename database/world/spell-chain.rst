.. _db-world-spell-chain:

====================
"spell\_chain" table
====================

The ``spell_chain`` table holds information on the chain of spells with
ranks.

Table structure
---------------

+----------------+----------------+--------+-------+-----------+---------+
| Field          | Type           | Null   | Key   | Default   | Extra   |
+================+================+========+=======+===========+=========+
| spell\_id      | mediumint(9)   | NO     | PRI   | 0         |         |
+----------------+----------------+--------+-------+-----------+---------+
| prev\_spell    | mediumint(9)   | NO     |       | 0         |         |
+----------------+----------------+--------+-------+-----------+---------+
| first\_spell   | mediumint(9)   | NO     |       | 0         |         |
+----------------+----------------+--------+-------+-----------+---------+
| rank           | tinyint(4)     | NO     |       | 0         |         |
+----------------+----------------+--------+-------+-----------+---------+
| req\_spell     | mediumint(9)   | NO     |       | 0         |         |
+----------------+----------------+--------+-------+-----------+---------+

Fields
------

spell\_id
---------

The spell identifier. The value has to match with a spell identifier
defined in `Spell.dbc <../dbc/Spell.dbc>`__.

prev\_spell
-----------

The spell identifier. The value has to match with a spell identifier
defined in `Spell.dbc <../dbc/Spell.dbc>`__. This is the previous rank
in the spell chain.

first\_spell
------------

The spell identifier. The value has to match with a spell identifier
defined in `Spell.dbc <../dbc/Spell.dbc>`__. This is the rank 1 spell in
the spell chain

rank
----

The rank of the spell referenced in ``spell_id``.

req\_spell
----------

The spell identifier. The value has to match with a spell identifier
defined in `Spell.dbc <../dbc/Spell.dbc>`__. This references a spell
required to use the spell referenced in ``spell_id``.
