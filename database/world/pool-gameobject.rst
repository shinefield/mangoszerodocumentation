.. _db-world-pool-gameobject:

========================
"pool\_gameobject" table
========================

The ``pool_gameobject`` table holds game objects that are tied to a
specific pool.

This table can only contain game objects that have a type of
GAMEOBJECT\_TYPE\_CHEST, GAMEOBJECT\_TYPE\_GOOBER,
GAMEOBJECT\_TYPE\_FISHINGHOLE.

Table structure
---------------

+---------------+-------------------------+--------+-------+-----------+---------+
| Field         | Type                    | Null   | Key   | Default   | Extra   |
+===============+=========================+========+=======+===========+=========+
| guid          | int(10) unsigned        | NO     | PRI   | 0         |         |
+---------------+-------------------------+--------+-------+-----------+---------+
| pool\_entry   | mediumint(8) unsigned   | NO     | MUL   | 0         |         |
+---------------+-------------------------+--------+-------+-----------+---------+
| chance        | float unsigned          | NO     |       | 0         |         |
+---------------+-------------------------+--------+-------+-----------+---------+
| description   | varchar(255)            | NO     |       | NULL      |         |
+---------------+-------------------------+--------+-------+-----------+---------+

Fields
------

guid
----

This references the `gameobject <gameobject>`__ tables unique ID for
which the entry is valid.

pool\_entry
-----------

The identifier of a pool template to which this game object belongs. The
value has to match with a pool identifier defined in the
`pool\_template <pool_template>`__.

chance
------

The explicit percentage chance that this game object will be spawned.

If the pool spawns just one game object (max\_limit = 1 in the
respective pool\_template), the core selects the game object to be
spawned in a two-step process:

First, only the explicitly-chanced (chance > 0) game objects of the pool
are rolled. If this roll does not produce any game object, all the game
objects without explicit chance (chance = 0) are rolled with equal
chance.

If the pool spawns more than one game object, the chance is ignored and
all the game objects in the pool are rolled in one step with equal
chance.

In case the pool spawns just one game object and all the game objects
have a non-zero chance, the sum of the chances for all the game objects
must equal to 100, otherwise the pool won't be spawned.

description
-----------

This field usually names the game object corresponding to the guid and
mentions which spawn point it is.

Example: ``Spawn Point 1 - Copper Vein``
