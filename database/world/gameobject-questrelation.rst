.. _db-world-gameobject-questrelation:

=================================
"gameobject\_questrelation" table
=================================

The ``gameobject_questrelation`` table holds connections between game
objects and quests. Links made here define that a creature should start
a quest.

Table structure
---------------

+---------+-------------------------+--------+-------+-----------+---------+
| Field   | Type                    | Null   | Key   | Default   | Extra   |
+=========+=========================+========+=======+===========+=========+
| id      | mediumint(8) unsigned   | NO     | PRI   | 0         |         |
+---------+-------------------------+--------+-------+-----------+---------+
| quest   | mediumint(8) unsigned   | NO     | PRI   | 0         |         |
+---------+-------------------------+--------+-------+-----------+---------+

Fields
------

id
--

This references the :doc:`gameobject-template`
tables unique ID for which the entry is valid.

.. note::

    Game object templates need to be of type quest giver.

quest
-----

This references the :doc:`quest-template` tables unique
ID for which the entry is valid.
