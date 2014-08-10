.. _db-world-spell-threat:

=====================
"spell\_threat" table
=====================

The ``spell_threat`` table holds threat values for any spells that
increase or decrease threat.

Entries here may be used to modify threat values which are original
defined in :doc:`../../file-formats/dbc/spell`.

Table structure
---------------

+--------------+-------------------------+--------+-------+-----------+---------+
| Field        | Type                    | Null   | Key   | Default   | Extra   |
+==============+=========================+========+=======+===========+=========+
| entry        | mediumint(8) unsigned   | NO     | PRI   | NULL      |         |
+--------------+-------------------------+--------+-------+-----------+---------+
| Threat       | smallint(6)             | NO     |       | NULL      |         |
+--------------+-------------------------+--------+-------+-----------+---------+
| multiplier   | float                   | NO     |       | 1         |         |
+--------------+-------------------------+--------+-------+-----------+---------+
| ap\_bonus    | float                   | NO     |       | 0         |         |
+--------------+-------------------------+--------+-------+-----------+---------+

Fields
------

entry
-----

The spell identifier. The value has to match with a spell identifier
defined in :doc:`../../file-formats/dbc/spell`.

.. note::

    Any spell referenced is required to be rank 1 in the spell
    chain, and has to have threat values set in the original spell
    definition.

Threat
------

The value of threat to add to the characters threat, or to remove from a
characters threat. Negative values reduce threat, positive values
increase threat.

multiplier
----------

Any value here will modify the spells threat with the factor given here.

ap\_bonus
---------

Any value here will modify the spells attack power with the factor given
here.
