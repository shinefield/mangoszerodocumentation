.. _db-world-pool-pool:

==================
"pool\_pool" table
==================

The ``pool_pool`` table holds definitions for grouping multiple pools
into a larger pool.

Table structure
---------------

+----------------+-------------------------+--------+-------+-----------+---------+
| Field          | Type                    | Null   | Key   | Default   | Extra   |
+================+=========================+========+=======+===========+=========+
| pool\_id       | mediumint(8) unsigned   | NO     | PRI   | 0         |         |
+----------------+-------------------------+--------+-------+-----------+---------+
| mother\_pool   | mediumint(8) unsigned   | NO     | MUL   | 0         |         |
+----------------+-------------------------+--------+-------+-----------+---------+
| chance         | float                   | NO     |       | 0         |         |
+----------------+-------------------------+--------+-------+-----------+---------+
| description    | varchar(255)            | NO     |       | NULL      |         |
+----------------+-------------------------+--------+-------+-----------+---------+

Fields
------

pool\_id
--------

The identifier of a pool template which should be included in the pool
group. The value has to match with a pool identifier defined in the
:doc:`pool-template`.

mother\_pool
------------

The identifier of a pool template which acts as parent pool for multiple
pool templates. The value has to match with a pool identifier defined in
the :doc:`pool-template`.

chance
------

The explicit percentage chance that this pool will be spawned.

If the parent pool spawns just one child pool (max\_limit = 1 in the
respective mother pool's pool\_template), the core selects the child
pool to be spawned in a two-step process:

First, only the explicitly-chanced (chance > 0) child pools of the
mother pool are rolled. If this roll does not produce any child pool,
all the child pools without explicit chance (chance = 0) are rolled with
equal chance.

If the parent pool spawns more than one child pool, the chance is
ignored and all the child pools in the mother pool are rolled in one
step with equal chance.

In case the parent pool spawns just one child pool and all the child
pools have a non-zero chance, the sum of the chances for all the child
pools must equal to 100, otherwise the parent pool won't function
correctly.

description
-----------

A text field to describe what this pool group is for.
