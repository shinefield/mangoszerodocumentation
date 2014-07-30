.. _db-world-pool-creature:

======================
"pool\_creature" table
======================

The ``pool_creature`` table holds creatures that are tied to a specific
pool.

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

This references the `creature <creature>`__ tables unique ID for which
the entry is valid.

pool\_entry
-----------

The identifier of a pool template to which this creature belongs. The
value has to match with a pool identifier defined in the
`pool\_template <pool_template>`__.

chance
------

The explicit percentage chance that this creature will be spawned.

If the pool spawns just one creature (max\_limit = 1 in the respective
pool\_template), the core selects the creature to be spawned in a
two-step process:

First, only the explicitly-chanced (chance > 0) creatures of the pool
are rolled. If this roll does not produce any creature, all the
creatures without explicit chance (chance = 0) are rolled with equal
chance.

If the pool spawns more than one creature, the chance is ignored and all
the creatures in the pool are rolled in one step with equal chance.

In case the pool spawns just one creature and all the creatures have a
non-zero chance, the sum of the chances for all the creatures must equal
to 100, otherwise the pool won't be spawned.

description
-----------

This field usually names the creature corresponding to the guid and
mentions which spawn point it is.

Example: ``RARE Snarlflare (14272) - Spawn 1``
