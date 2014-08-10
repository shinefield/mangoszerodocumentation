.. _db-world-creature-template-addon:

=================================
"creature\_template\_addon" table
=================================

The ``creature_template_addon`` table holds definitions which modify a
``creature_template`` entries visuals, behaviour and state.

Table structure
---------------

+-----------------+-------------------------+--------+-------+-----------+---------+
| Field           | Type                    | Null   | Key   | Default   | Extra   |
+=================+=========================+========+=======+===========+=========+
| entry           | mediumint(8) unsigned   | NO     | PRI   | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| mount           | mediumint(8) unsigned   | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| bytes1          | int(10) unsigned        | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| b2\_0\_sheath   | tinyint(3) unsigned     | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| b2\_1\_flags    | tinyint(3) unsigned     | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| emote           | mediumint(8) unsigned   | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| moveflags       | int(10) unsigned        | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| auras           | text                    | YES    |       | NULL      |         |
+-----------------+-------------------------+--------+-------+-----------+---------+

Fields
------

entry
-----

This references the `creature\_template <creature_template>`__ tables
unique ID for which the entry is valid.

mount
-----

A display model identifier used as mount for the creature\_template.
This references the `creature\_model\_info <creature_model_info>`__
tables unique ID for which this entry is valid.

bytes1
------

**TODO**

b2\_0\_sheath
-------------

Defines the sheath state of the creature\_template.

+---------+----------------------------+
| Value   | State                      |
+=========+============================+
| 0       | All weapons sheathed       |
+---------+----------------------------+
| 1       | Melee weapon unsheathed    |
+---------+----------------------------+
| 2       | Ranged weapon unsheathed   |
+---------+----------------------------+

b2\_1\_flags
------------

**TODO**

emote
-----

An emote identifier. The value has to match with an emote identifier
defined in :doc:`../../file-formats/dbc/emotes`.

moveflags
---------

The flag controls how a creature\_template will be animated while
moving.

+--------------+-------------------------------+
| Value        | Movement animation            |
+==============+===============================+
| 0x00000000   | MOVEFLAG\_NONE                |
+--------------+-------------------------------+
| 0x00000001   | MOVEFLAG\_FORWARD             |
+--------------+-------------------------------+
| 0x00000002   | MOVEFLAG\_BACKWARD            |
+--------------+-------------------------------+
| 0x00000004   | MOVEFLAG\_STRAFE\_LEFT        |
+--------------+-------------------------------+
| 0x00000008   | MOVEFLAG\_STRAFE\_RIGHT       |
+--------------+-------------------------------+
| 0x00000010   | MOVEFLAG\_TURN\_LEFT          |
+--------------+-------------------------------+
| 0x00000020   | MOVEFLAG\_TURN\_RIGHT         |
+--------------+-------------------------------+
| 0x00000040   | MOVEFLAG\_PITCH\_UP           |
+--------------+-------------------------------+
| 0x00000080   | MOVEFLAG\_PITCH\_DOWN         |
+--------------+-------------------------------+
| 0x00000100   | MOVEFLAG\_WALK\_MODE          |
+--------------+-------------------------------+
| 0x00000400   | MOVEFLAG\_LEVITATING          |
+--------------+-------------------------------+
| 0x00000800   | MOVEFLAG\_ROOT                |
+--------------+-------------------------------+
| 0x00002000   | MOVEFLAG\_FALLING             |
+--------------+-------------------------------+
| 0x00004000   | MOVEFLAG\_FALLINGFAR          |
+--------------+-------------------------------+
| 0x00200000   | MOVEFLAG\_SWIMMING            |
+--------------+-------------------------------+
| 0x00400000   | MOVEFLAG\_ASCENDING           |
+--------------+-------------------------------+
| 0x00800000   | MOVEFLAG\_CAN\_FLY            |
+--------------+-------------------------------+
| 0x01000000   | MOVEFLAG\_FLYING              |
+--------------+-------------------------------+
| 0x02000000   | MOVEFLAG\_ONTRANSPORT         |
+--------------+-------------------------------+
| 0x04000000   | MOVEFLAG\_SPLINE\_ELEVATION   |
+--------------+-------------------------------+
| 0x08000000   | MOVEFLAG\_SPLINE\_ENABLED     |
+--------------+-------------------------------+
| 0x10000000   | MOVEFLAG\_WATERWALKING        |
+--------------+-------------------------------+
| 0x20000000   | MOVEFLAG\_SAFE\_FALL          |
+--------------+-------------------------------+
| 0x40000000   | MOVEFLAG\_HOVER               |
+--------------+-------------------------------+

auras
-----

Allows to attach auras to a creature\_template entry. This includes
visual auras and spell effects. The field is a string containing a spell
identifier defined in :doc:`../../file-formats/dbc/spell` with an index to
the spell effect.

Multiple spells can be concatenated. Spells and effect indexes are
separated by space characters.

*Examples*

+---------------------+-----------------------------------------------------------------------+
| Value               | Result                                                                |
+=====================+=======================================================================+
| '16380 0'           | Makes the creature\_template invisible                                |
+---------------------+-----------------------------------------------------------------------+
| '18950 0 18950 1'   | Makes the creature\_template detect invisible creatures and players   |
+---------------------+-----------------------------------------------------------------------+

