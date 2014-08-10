.. _db-world-battleground-events:

============================
"battleground\_events" table
============================

The ``battleground_events`` table holds definitions of battleground
events.

Table structure
---------------

+---------------+-----------------------+--------+-------+-----------+---------+
| Field         | Type                  | Null   | Key   | Default   | Extra   |
+===============+=======================+========+=======+===========+=========+
| map           | smallint(5)           | NO     | PRI   | NULL      |         |
+---------------+-----------------------+--------+-------+-----------+---------+
| event1        | tinyint(3) unsigned   | NO     | PRI   | NULL      |         |
+---------------+-----------------------+--------+-------+-----------+---------+
| event2        | tinyint(3) unsigned   | NO     | PRI   | NULL      |         |
+---------------+-----------------------+--------+-------+-----------+---------+
| description   | varchar(255)          | NO     |       | NULL      |         |
+---------------+-----------------------+--------+-------+-----------+---------+

Fields
------

map
---

A map identifier. The value has to match with a map identifier defined
in :doc:`../../file-formats/dbc/map`.

event1
------

The identifier for the event node in the battleground. Event nodes
usually are defined in the battleground's script.

event2
------

The state of the event node. Node status is defined differently in every
battleground script.

.. note::

    If you update battleground scripts and make changes to node
    status values ensure that you provide database update scripts which
    update the battleground events accordingly.

description
-----------

A description for the battleground event. This is only used for
documentation purposes to help identifying events.
