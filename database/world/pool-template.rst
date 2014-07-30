.. _db-world-pool-template:

======================
"pool\_template" table
======================

The ``pool_template`` table holds definitions for pooling of game
content.

Table structure
---------------

+---------------+-------------------------+--------+-------+-----------+---------+
| Field         | Type                    | Null   | Key   | Default   | Extra   |
+===============+=========================+========+=======+===========+=========+
| entry         | mediumint(8) unsigned   | NO     | PRI   | 0         |         |
+---------------+-------------------------+--------+-------+-----------+---------+
| max\_limit    | int(10) unsigned        | NO     |       | 0         |         |
+---------------+-------------------------+--------+-------+-----------+---------+
| description   | varchar(255)            | NO     |       | NULL      |         |
+---------------+-------------------------+--------+-------+-----------+---------+

Fields
------

entry
-----

The pool ID. This is an arbitrary number that is only used to link the
game objects, creatures or quests in this pool.

max\_limit
----------

The maximum amount of game objects, creatures or quests to spawn from
the pool.

description
-----------

Describes the pool. By default the name and entry ID of the game object,
creature or quest is used.
