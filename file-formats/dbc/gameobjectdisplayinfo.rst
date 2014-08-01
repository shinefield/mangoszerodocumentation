.. _file-formats-dbc-gameobjectdisplayinfo:

=========================
GameObjectDisplayInfo.dbc
=========================

The *game object display information* table links display IDs to
combinations of models and sounds.

Table structure
---------------

+------+------------------+--------------------+-----------+----------------------------------------------+
| ID   | Name             | Type               | Default   | Description                                  |
+======+==================+====================+===========+==============================================+
| 1    | ID               | Integer (signed)   | -         | Unique ID                                    |
+------+------------------+--------------------+-----------+----------------------------------------------+
| 2    | modelName        | String             | -         | The path to the model for the game object.   |
+------+------------------+--------------------+-----------+----------------------------------------------+
| 3    | soundEntryID1    | Integer (signed)   | 0         | A sound for the state *STAND*.               |
+------+------------------+--------------------+-----------+----------------------------------------------+
| 4    | soundEntryID2    | Integer (signed)   | 0         | A sound for the state *OPEN*.                |
+------+------------------+--------------------+-----------+----------------------------------------------+
| 5    | soundEntryID3    | Integer (signed)   | 0         | A sound for the state *LOOP*.                |
+------+------------------+--------------------+-----------+----------------------------------------------+
| 6    | soundEntryID4    | Integer (signed)   | 0         | A sound for the state *CLOSE*.               |
+------+------------------+--------------------+-----------+----------------------------------------------+
| 7    | soundEntryID5    | Integer (signed)   | 0         | A sound for the state *DESTROY*.             |
+------+------------------+--------------------+-----------+----------------------------------------------+
| 8    | soundEntryID6    | Integer (signed)   | 0         | A sound for the state *OPENED*.              |
+------+------------------+--------------------+-----------+----------------------------------------------+
| 9    | soundEntryID7    | Integer (signed)   | 0         | A sound for the state *CUSTOM0*.             |
+------+------------------+--------------------+-----------+----------------------------------------------+
| 10   | soundEntryID8    | Integer (signed)   | 0         | A sound for the state *CUSTOM1*.             |
+------+------------------+--------------------+-----------+----------------------------------------------+
| 11   | soundEntryID9    | Integer (signed)   | 0         | A sound for the state *CUSTOM2*.             |
+------+------------------+--------------------+-----------+----------------------------------------------+
| 12   | soundEntryID10   | Integer (signed)   | 0         | A sound for the state *CUSTOM3*.             |
+------+------------------+--------------------+-----------+----------------------------------------------+

Relations
---------

-  ``soundEntryID[1-10]`` reference the primary key of
   ``SoundEntries.dbc``.
