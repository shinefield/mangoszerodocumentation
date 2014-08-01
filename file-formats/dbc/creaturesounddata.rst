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
| 1    | ID                          | Integer (signed)   | -         | Unique ID                      |
+------+-----------------------------+--------------------+-----------+--------------------------------+
| 2    | soundExertionID             | Integer (signed)   | 0         | Sound played for this event.   |
+------+-----------------------------+--------------------+-----------+--------------------------------+
| 3    | soundExertionCriticalID     | Integer (signed)   | 0         | Sound played for this event.   |
+------+-----------------------------+--------------------+-----------+--------------------------------+
| 4    | soundInjuryID               | Integer (signed)   | 0         | Sound played for this event.   |
+------+-----------------------------+--------------------+-----------+--------------------------------+
| 5    | soundInjuryCriticalID       | Integer (signed)   | 0         | Sound played for this event.   |
+------+-----------------------------+--------------------+-----------+--------------------------------+
| 6    | soundInjuryCrushingBlowID   | Integer (signed)   | 0         | Sound played for this event.   |
+------+-----------------------------+--------------------+-----------+--------------------------------+
| 7    | soundDeathID                | Integer (signed)   | 0         | Sound played for this event.   |
+------+-----------------------------+--------------------+-----------+--------------------------------+
| 8    | soundStunID                 | Integer (signed)   | 0         | Sound played for this event.   |
+------+-----------------------------+--------------------+-----------+--------------------------------+
| 9    | soundStandID                | Integer (signed)   | 0         | Sound played for this event.   |
+------+-----------------------------+--------------------+-----------+--------------------------------+
| 10   | soundFootstepID             | Integer (signed)   | 0         | Sound played for this event.   |
+------+-----------------------------+--------------------+-----------+--------------------------------+
| 11   | soundAggroID                | Integer (signed)   | 0         | Sound played for this event.   |
+------+-----------------------------+--------------------+-----------+--------------------------------+
| 12   | soundWingFlapID             | Integer (signed)   | 0         | Sound played for this event.   |
+------+-----------------------------+--------------------+-----------+--------------------------------+
| 13   | soundWingGlideID            | Integer (signed)   | 0         | Sound played for this event.   |
+------+-----------------------------+--------------------+-----------+--------------------------------+
| 14   | soundAlertID                | Integer (signed)   | 0         | Sound played for this event.   |
+------+-----------------------------+--------------------+-----------+--------------------------------+
| 15   | soundFidgetID               | Integer (signed)   | 0         | Sound played for this event.   |
+------+-----------------------------+--------------------+-----------+--------------------------------+
| 16   | customAttack                | Integer (signed)   | 0         | Sound played for this event.   |
+------+-----------------------------+--------------------+-----------+--------------------------------+
| 17   | NPCSoundID                  | Integer (signed)   | 0         | Sound played for this event.   |
+------+-----------------------------+--------------------+-----------+--------------------------------+
| 18   | loopSoundID                 | Integer (signed)   | 0         | Sound played for this event.   |
+------+-----------------------------+--------------------+-----------+--------------------------------+
| 19   | creatureImpactType          | Integer            | 0         | **TODO**                       |
+------+-----------------------------+--------------------+-----------+--------------------------------+
| 20   | soundJumpStartID            | Integer (signed)   | 0         | Sound played for this event.   |
+------+-----------------------------+--------------------+-----------+--------------------------------+
| 21   | soundJumpEndID              | Integer (signed)   | 0         | Sound played for this event.   |
+------+-----------------------------+--------------------+-----------+--------------------------------+
| 22   | soundPetAttackID            | Integer (signed)   | 0         | Sound played for this event.   |
+------+-----------------------------+--------------------+-----------+--------------------------------+
| 23   | soundPetOrderID             | Integer (signed)   | 0         | Sound played for this event.   |
+------+-----------------------------+--------------------+-----------+--------------------------------+
| 24   | soundPetDismissID           | Integer (signed)   | 0         | Sound played for this event.   |
+------+-----------------------------+--------------------+-----------+--------------------------------+
| 25   | fidgetDelaySecondsMin       | Integer            | 0         | Delay for fidgeting sound.     |
+------+-----------------------------+--------------------+-----------+--------------------------------+
| 26   | fidgetDelaySecondsMax       | Integer            | 0         | Delay for fidgeting sound.     |
+------+-----------------------------+--------------------+-----------+--------------------------------+
| 27   | birthSoundID                | Integer (signed)   | 0         | Sound played for this event.   |
+------+-----------------------------+--------------------+-----------+--------------------------------+
| 28   | spellCastDirectedSoundID    | Integer (signed)   | 0         | Sound played for this event.   |
+------+-----------------------------+--------------------+-----------+--------------------------------+
| 29   | submergeSoundID             | Integer (signed)   | 0         | Sound played for this event.   |
+------+-----------------------------+--------------------+-----------+--------------------------------+
| 30   | submergedSoundID            | Integer (signed)   | 0         | Sound played for this event.   |
+------+-----------------------------+--------------------+-----------+--------------------------------+

Fields
------

creatureImpactType
------------------

**TODO**

Relations
---------

-  ``soundExertionID``, ``soundExertionCriticalID``, ``soundInjuryID``,
   ``soundInjuryCriticalID``, ``soundInjuryCrushingBlowID``,
   ``soundDeathID``, ``soundStunID``, ``soundStandID``,
   ``soundFootstepID``, ``soundAggroID``, ``soundWingFlapID``,
   ``soundWingGlideID`` and ``soundAlertID`` reference the primary key
   of ``SoundEntries.dbc``.

