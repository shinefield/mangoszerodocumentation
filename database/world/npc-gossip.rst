.. _db-world-npc-gossip:

===================
"npc\_gossip" table
===================

The ``npc_gossip`` table holds the link between creatures and gossip
text.

Table structure
---------------

+-------------+-------------------------+--------+-------+-----------+---------+
| Field       | Type                    | Null   | Key   | Default   | Extra   |
+=============+=========================+========+=======+===========+=========+
| npc\_guid   | int(10) unsigned        | NO     | PRI   | 0         |         |
+-------------+-------------------------+--------+-------+-----------+---------+
| textid      | mediumint(8) unsigned   | NO     |       | 0         |         |
+-------------+-------------------------+--------+-------+-----------+---------+

Fields
------

npc\_guid
---------

This references the `creature <creature>`__ tables ``guid`` field for
which the entry is valid.

textid
------

This references the `npc\_text <npc_text>`__ tables unique ID of the NPC
text for which the entry is valid.

*Notice*: to actually make a creature display a gossip dialogue with the
linked text, you will have to update the
`creature\_template <creature_template>`__ as follows:

::

        SET @CREATURE_FLAG_NPC_GOSSIP                   = 1;

        UPDATE `creature_template`
        SET
            `NpcFlags`              = `NpcFlags` | @CREATURE_FLAG_NPC_GOSSIP,
        WHERE
            `entry`                 = YOUR-CREATURE;

This will add the gossip flag to any existing flags and thus enable the
link text to be displayed.
