.. _db-world-spell-area:

===================
"spell\_area" table
===================

The ``spell_area`` table holds information on spells applied to
creatures and characters in specific areas under given conditions.

Table structure
---------------

+------------------------+-------------------------+--------+-------+-----------+---------+
| Field                  | Type                    | Null   | Key   | Default   | Extra   |
+========================+=========================+========+=======+===========+=========+
| spell                  | mediumint(8) unsigned   | NO     | PRI   | 0         |         |
+------------------------+-------------------------+--------+-------+-----------+---------+
| area                   | mediumint(8) unsigned   | NO     | PRI   | 0         |         |
+------------------------+-------------------------+--------+-------+-----------+---------+
| quest\_start           | mediumint(8) unsigned   | NO     | PRI   | 0         |         |
+------------------------+-------------------------+--------+-------+-----------+---------+
| quest\_start\_active   | tinyint(1) unsigned     | NO     | PRI   | 0         |         |
+------------------------+-------------------------+--------+-------+-----------+---------+
| quest\_end             | mediumint(8) unsigned   | NO     |       | 0         |         |
+------------------------+-------------------------+--------+-------+-----------+---------+
| condition\_id          | mediumint(8) unsigned   | NO     |       | 0         |         |
+------------------------+-------------------------+--------+-------+-----------+---------+
| aura\_spell            | mediumint(8)            | NO     | PRI   | 0         |         |
+------------------------+-------------------------+--------+-------+-----------+---------+
| racemask               | mediumint(8) unsigned   | NO     | PRI   | 0         |         |
+------------------------+-------------------------+--------+-------+-----------+---------+
| gender                 | tinyint(1) unsigned     | NO     | PRI   | 2         |         |
+------------------------+-------------------------+--------+-------+-----------+---------+
| autocast               | tinyint(1) unsigned     | NO     |       | 0         |         |
+------------------------+-------------------------+--------+-------+-----------+---------+

Fields
------

spell
-----

The spell identifier. The value has to match with a spell identifier
defined in :doc:`../../file-formats/dbc/spell`.

area
----

An areatrigger identifier. The value has to match with a areatrigger
identifier defined in :doc:`../../file-formats/dbc/areatrigger`.

quest\_start
------------

This references the `quest\_template <quest_template>`__ tables unique
ID for which the entry is valid. The quest entry listed here has to be
available to a character or needs to be active for a character. Depends
on the value of ``quest_start_active``.

quest\_start\_active
--------------------

If set to ``0``, the quest listed in ``quest_start`` has to be available
to a character but *not* active on the character. If set to ``1``, the
quest listed in ``quest_start`` can be available or active on the
character.

quest\_end
----------

This references the `quest\_template <quest_template>`__ tables unique
ID for which the entry is valid. The quest listed here *must not* be
completed to apply the spell.

condition\_id
-------------

This references the `conditions <conditions>`__ tables unique ID for
which the entry is valid.

aura\_spell
-----------

The aura spell identifier. The value has to match with a spell
identifier defined in :doc:`../../file-formats/dbc/spell`. If set to a with
a positive value, characters *must* have this aura to activate the
spell, if set to the spell identifier with a negative sign, characters
*must not* have the aura.

racemask
--------

A bit-mask corresponding to races that should get the spell. The value
has to match with races defined in :doc:`../../file-formats/dbc/chrraces`.

gender
------

The gender of characters to which the spell is applied. The following
table list available values.

Gender of the creature

+---------+----------+
| Value   | Gender   |
+=========+==========+
| 0       | Male     |
+---------+----------+
| 1       | Female   |
+---------+----------+
| 2       | Both     |
+---------+----------+

autocast
--------

Set to ``1`` to autocast the spell.
