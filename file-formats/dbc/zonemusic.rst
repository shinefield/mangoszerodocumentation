.. _file-formats-dbc-zonemusic:

=============
ZoneMusic.dbc
=============

The *zone music* table contains definitions for ambience sounds to be
played during day and night time in various areas.

Table structure
---------------

+------+---------------------------+--------------------+-----------+-----------------------------------------------------------------------------------------------------+
| ID   | Name                      | Type               | Default   | Description                                                                                         |
+======+===========================+====================+===========+=====================================================================================================+
| 1    | ID                        | Integer (signed)   | -         | Unique ID                                                                                           |
+------+---------------------------+--------------------+-----------+-----------------------------------------------------------------------------------------------------+
| 2    | setName                   | String             | -         | The name of the ambience sound.                                                                     |
+------+---------------------------+--------------------+-----------+-----------------------------------------------------------------------------------------------------+
| 3    | silenceIntervalMinDay     | Integer            | 180000    | The minimum amount of milliseconds to wait before replaying the ambience sound during day time.     |
+------+---------------------------+--------------------+-----------+-----------------------------------------------------------------------------------------------------+
| 4    | silenceIntervalMinNight   | Integer            | 180000    | The minimum amount of milliseconds to wait before replaying the ambience sound during night time.   |
+------+---------------------------+--------------------+-----------+-----------------------------------------------------------------------------------------------------+
| 5    | silenceIntervalMaxDay     | Integer            | 300000    | The maximum amount of milliseconds to wait before replaying the ambience sound during day time.     |
+------+---------------------------+--------------------+-----------+-----------------------------------------------------------------------------------------------------+
| 6    | silenceIntervalMaxNight   | Integer            | 300000    | The maximum amount of milliseconds to wait before replaying the ambience sound during night time.   |
+------+---------------------------+--------------------+-----------+-----------------------------------------------------------------------------------------------------+
| 7    | daySoundEntryID           | Integer (signed)   | 0         | The sound entry being played during day time.                                                       |
+------+---------------------------+--------------------+-----------+-----------------------------------------------------------------------------------------------------+
| 8    | nightSoundEntryID         | Integer (signed)   | 0         | The sound entry being played during night time.                                                     |
+------+---------------------------+--------------------+-----------+-----------------------------------------------------------------------------------------------------+

Relations
---------

-  ``daySoundEntryID`` and ``nightSoundEntryID`` reference the primary
   key of ``SoundEntries.dbc``.
