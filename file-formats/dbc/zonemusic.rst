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
| 1    | ID                        | Integer            | -         | Unique ID                                                                                           |
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
| 7    | daySoundEntry             | Integer            | 0         | The sound entry being played during day time.                                                       |
+------+---------------------------+--------------------+-----------+-----------------------------------------------------------------------------------------------------+
| 8    | nightSoundEntry           | Integer            | 0         | The sound entry being played during night time.                                                     |
+------+---------------------------+--------------------+-----------+-----------------------------------------------------------------------------------------------------+

Relations
---------

-  ``daySoundEntry`` and ``nightSoundEntry`` reference the primary key of ``SoundEntries.dbc``.
