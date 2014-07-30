.. _db-world-creature-battleground:

==============================
"creature\_battleground" table
==============================

The ``creature_battleground`` table holds information on creatures
spawns which are used in battlegrounds.

Table structure
---------------

+----------+-----------------------+--------+-------+-----------+---------+
| Field    | Type                  | Null   | Key   | Default   | Extra   |
+==========+=======================+========+=======+===========+=========+
| guid     | int(10) unsigned      | NO     | PRI   | NULL      |         |
+----------+-----------------------+--------+-------+-----------+---------+
| event1   | tinyint(3) unsigned   | NO     |       | NULL      |         |
+----------+-----------------------+--------+-------+-----------+---------+
| event2   | tinyint(3) unsigned   | NO     |       | NULL      |         |
+----------+-----------------------+--------+-------+-----------+---------+

Fields
------

guid
----

This references the `creature <creature>`__ tables unique ``guid`` for
which the entry is valid.

event1
------

The identifier for the event node in the battleground. Event nodes
usually are defined in the battleground's script.

*Nodes* are locations in a battleground where characters of each faction
can perform actions, such as capturing a tower in Alterac Valley, or
taking control over the stables in Arathi Basin.

event2
------

The state of the event node. Node status is defined differently in every
battleground script.

*Node events* can occur for every node and usually describe changes due
to character interaction. E.g. if stables in Arathi Basin are taken over
by Alliance, the stables note state would become Alliance controlled.
Similar node states exist for every battleground note.

*Notice*: if you update battleground scripts and make changes to node
status values ensure that you provide database update scripts which
update the battleground events accordingly.
