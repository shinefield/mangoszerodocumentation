.. _db-world-gameobject-involvedrelation:

====================================
"gameobject\_involvedrelation" table
====================================

The ``gameobject_involvedrelation`` table holds holds connections
between game objects and quests. Links made here define that a creature
should end a quest.

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

This references the `gameobject\_template <gameobject_template>`__
tables unique ID for which the entry is valid.

.. note::

    game object templates need to be of type quest giver.

quest
-----

This references the `quest\_template <quest_template>`__ tables unique
ID for which the entry is valid.
