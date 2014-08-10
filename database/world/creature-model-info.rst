.. _db-world-creature-model-info:

=============================
"creature\_model\_info" table
=============================

The ``creature_model_info`` table holds all models of mobs, their gender
and other information that are model related. This means that when a
creature uses another model, this information will change as well.

Table structure
---------------

+--------------------------+-------------------------+--------+-------+-----------+---------+
| Field                    | Type                    | Null   | Key   | Default   | Extra   |
+==========================+=========================+========+=======+===========+=========+
| modelid                  | mediumint(8) unsigned   | NO     | PRI   | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| bounding\_radius         | float                   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| combat\_reach            | float                   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| gender                   | tinyint(3) unsigned     | NO     |       | 2         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| modelid\_other\_gender   | mediumint(8) unsigned   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| modelid\_other\_team     | mediumint(8) unsigned   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+

Fields
------

modelid
-------

A display model identifier. The value has to match with a model
identifier defined in :doc:`../../file-formats/dbc/creaturedisplayinfo`.

bounding\_radius
----------------

This is the distance the creature stands from the player to attack him
while in melee.

combat\_reach
-------------

This is the maximum distance the creature can reach the player in ranged
attack.

gender
------

Gender of the creature

+---------+----------+
| Value   | Gender   |
+=========+==========+
| 0       | Male     |
+---------+----------+
| 1       | Female   |
+---------+----------+
| 2       | None     |
+---------+----------+

modelid\_other\_gender
----------------------

If the model information entry is set to *male* or *female*, this
references the :doc:`creature-model-info` tables unique ID for the
entry of the other gender's model information.

modelid\_other\_team
--------------------

If the model information entry has different display information for the
other faction, this references the :doc:`creature-model-info` tables unique
ID for the entry of the other faction's model information.
