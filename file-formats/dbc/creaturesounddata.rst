.. _file-formats-dbc-creaturesoundata:

=====================
CreatureSoundData.dbc
=====================

The *creature sound data* table contains definitions for which sounds
should be used for a creature.

Table structure
---------------

+------+-----------------------------+--------------------+-----------+--------------------------------+
| ID   | Name                        | Type               | Default   | Description                    |
+======+=============================+====================+===========+================================+
| 1    | ID                          | Integer            | -         | Unique ID                      |
+------+-----------------------------+--------------------+-----------+--------------------------------+
| 2    | soundExertion               | Integer            | 0         | Sound played for this event.   |
+------+-----------------------------+--------------------+-----------+--------------------------------+
| 3    | soundExertionCritical       | Integer            | 0         | Sound played for this event.   |
+------+-----------------------------+--------------------+-----------+--------------------------------+
| 4    | soundInjury                 | Integer            | 0         | Sound played for this event.   |
+------+-----------------------------+--------------------+-----------+--------------------------------+
| 5    | soundInjuryCritical         | Integer            | 0         | Sound played for this event.   |
+------+-----------------------------+--------------------+-----------+--------------------------------+
| 6    | soundInjuryCrushingBlow     | Integer            | 0         | Sound played for this event.   |
+------+-----------------------------+--------------------+-----------+--------------------------------+
| 7    | soundDeath                  | Integer            | 0         | Sound played for this event.   |
+------+-----------------------------+--------------------+-----------+--------------------------------+
| 8    | soundStun                   | Integer            | 0         | Sound played for this event.   |
+------+-----------------------------+--------------------+-----------+--------------------------------+
| 9    | soundStand                  | Integer            | 0         | Sound played for this event.   |
+------+-----------------------------+--------------------+-----------+--------------------------------+
| 10   | soundFootstep               | Integer            | 0         | Sound played for this event.   |
+------+-----------------------------+--------------------+-----------+--------------------------------+
| 11   | soundAggro                  | Integer            | 0         | Sound played for this event.   |
+------+-----------------------------+--------------------+-----------+--------------------------------+
| 12   | soundWingFlap               | Integer            | 0         | Sound played for this event.   |
+------+-----------------------------+--------------------+-----------+--------------------------------+
| 13   | soundWingGlide              | Integer            | 0         | Sound played for this event.   |
+------+-----------------------------+--------------------+-----------+--------------------------------+
| 14   | soundAlert                  | Integer            | 0         | Sound played for this event.   |
+------+-----------------------------+--------------------+-----------+--------------------------------+
| 15   | soundFidget                 | Integer            | 0         | Sound played for this event.   |
+------+-----------------------------+--------------------+-----------+--------------------------------+
| 16   | customAttack                | Integer            | 0         | Sound played for this event.   |
+------+-----------------------------+--------------------+-----------+--------------------------------+
| 17   | NPCSound                    | Integer            | 0         | Sound played for this event.   |
+------+-----------------------------+--------------------+-----------+--------------------------------+
| 18   | loopSound                   | Integer            | 0         | Sound played for this event.   |
+------+-----------------------------+--------------------+-----------+--------------------------------+
| 19   | creatureImpactType          | Integer (signed)   | 0         | **TODO**                       |
+------+-----------------------------+--------------------+-----------+--------------------------------+
| 20   | soundJumpStart              | Integer            | 0         | Sound played for this event.   |
+------+-----------------------------+--------------------+-----------+--------------------------------+
| 21   | soundJumpEnd                | Integer            | 0         | Sound played for this event.   |
+------+-----------------------------+--------------------+-----------+--------------------------------+
| 22   | soundPetAttack              | Integer            | 0         | Sound played for this event.   |
+------+-----------------------------+--------------------+-----------+--------------------------------+
| 23   | soundPetOrder               | Integer            | 0         | Sound played for this event.   |
+------+-----------------------------+--------------------+-----------+--------------------------------+
| 24   | soundPetDismiss             | Integer            | 0         | Sound played for this event.   |
+------+-----------------------------+--------------------+-----------+--------------------------------+
| 25   | fidgetDelaySecondsMin       | Integer (signed)   | 0         | Delay for fidgeting sound.     |
+------+-----------------------------+--------------------+-----------+--------------------------------+
| 26   | fidgetDelaySecondsMax       | Integer (signed)   | 0         | Delay for fidgeting sound.     |
+------+-----------------------------+--------------------+-----------+--------------------------------+
| 27   | birthSound                  | Integer            | 0         | Sound played for this event.   |
+------+-----------------------------+--------------------+-----------+--------------------------------+
| 28   | spellCastDirectedSound      | Integer            | 0         | Sound played for this event.   |
+------+-----------------------------+--------------------+-----------+--------------------------------+
| 29   | submergeSound               | Integer            | 0         | Sound played for this event.   |
+------+-----------------------------+--------------------+-----------+--------------------------------+
| 30   | submergedSound              | Integer            | 0         | Sound played for this event.   |
+------+-----------------------------+--------------------+-----------+--------------------------------+

Fields
------

creatureImpactType
~~~~~~~~~~~~~~~~~~

**TODO**

Relations
---------

-  ``soundExertion``, ``soundExertionCritical``, ``soundInjury``,
   ``soundInjuryCritical``, ``soundInjuryCrushingBlow``,
   ``soundDeath``, ``soundStun``, ``soundStand``,
   ``soundFootstep``, ``soundAggro``, ``soundWingFlap``,
   ``soundWingGlide`` and ``soundAlert`` reference the primary key
   of :doc:`soundentries`.
