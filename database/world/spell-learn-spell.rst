.. _db-world-spell-learn-spell:

===========================
"spell\_learn\_spell" table
===========================

The ``spell_learn_spell`` table holds information on spells which should
be learned by a character when learning a spell.

This is e.g. used when learning professions, where a character gains the
profession spell and an initial set of recipe spells.

.. note::

    Do not include spells with SPELL\_EFFECT\_LEARN\_SPELL here.

Table structure
---------------

+-----------+------------------------+--------+-------+-----------+---------+
| Field     | Type                   | Null   | Key   | Default   | Extra   |
+===========+========================+========+=======+===========+=========+
| entry     | smallint(5) unsigned   | NO     | PRI   | 0         |         |
+-----------+------------------------+--------+-------+-----------+---------+
| SpellID   | smallint(5) unsigned   | NO     | PRI   | 0         |         |
+-----------+------------------------+--------+-------+-----------+---------+
| Active    | tinyint(3) unsigned    | NO     |       | 1         |         |
+-----------+------------------------+--------+-------+-----------+---------+

Fields
------

entry
-----

The spell identifier. The value has to match with a spell identifier
defined in `Spell.dbc <../dbc/Spell.dbc>`__. This is the spell which
will teach the spell given by ``SpellID``.

SpellID
-------

The spell identifier. The value has to match with a spell identifier
defined in `Spell.dbc <../dbc/Spell.dbc>`__. This is the spell which a
character will actually learn.

Active
------

Decides if a learned spell will appear in the character's spell book.

+---------+--------------------------------------+
| Value   | Description                          |
+=========+======================================+
| 0       | Will not appear in the spell book.   |
+---------+--------------------------------------+
| 1       | Will appear in the spell book.       |
+---------+--------------------------------------+

