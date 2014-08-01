.. _file-formats-dbc-lightintband:

================
LightIntBand.dbc
================

The *light integer band* table contains definitions for daytime
modifiers of lighting.

Table structure
---------------

+------+----------+--------------------+-----------+----------------------------------------------------------------------------------------------------+
| ID   | Name     | Type               | Default   | Description                                                                                        |
+======+==========+====================+===========+====================================================================================================+
| 1    | ID       | Integer (signed)   | -         | Unique ID                                                                                          |
+------+----------+--------------------+-----------+----------------------------------------------------------------------------------------------------+
| 2    | num      | Integer            | 0         | Number of lighting modifiers set.                                                                  |
+------+----------+--------------------+-----------+----------------------------------------------------------------------------------------------------+
| 3    | time1    | Integer            | 0         | Time Values from 0 to 2880 where each number represents a half minute from midnight to midnight.   |
+------+----------+--------------------+-----------+----------------------------------------------------------------------------------------------------+
| 4    | time2    | Integer            | 0         | Time Values from 0 to 2880 where each number represents a half minute from midnight to midnight.   |
+------+----------+--------------------+-----------+----------------------------------------------------------------------------------------------------+
| 5    | time3    | Integer            | 0         | Time Values from 0 to 2880 where each number represents a half minute from midnight to midnight.   |
+------+----------+--------------------+-----------+----------------------------------------------------------------------------------------------------+
| 6    | time4    | Integer            | 0         | Time Values from 0 to 2880 where each number represents a half minute from midnight to midnight.   |
+------+----------+--------------------+-----------+----------------------------------------------------------------------------------------------------+
| 7    | time5    | Integer            | 0         | Time Values from 0 to 2880 where each number represents a half minute from midnight to midnight.   |
+------+----------+--------------------+-----------+----------------------------------------------------------------------------------------------------+
| 8    | time6    | Integer            | 0         | Time Values from 0 to 2880 where each number represents a half minute from midnight to midnight.   |
+------+----------+--------------------+-----------+----------------------------------------------------------------------------------------------------+
| 9    | time7    | Integer            | 0         | Time Values from 0 to 2880 where each number represents a half minute from midnight to midnight.   |
+------+----------+--------------------+-----------+----------------------------------------------------------------------------------------------------+
| 10   | time8    | Integer            | 0         | Time Values from 0 to 2880 where each number represents a half minute from midnight to midnight.   |
+------+----------+--------------------+-----------+----------------------------------------------------------------------------------------------------+
| 11   | time9    | Integer            | 0         | Time Values from 0 to 2880 where each number represents a half minute from midnight to midnight.   |
+------+----------+--------------------+-----------+----------------------------------------------------------------------------------------------------+
| 12   | time10   | Integer            | 0         | Time Values from 0 to 2880 where each number represents a half minute from midnight to midnight.   |
+------+----------+--------------------+-----------+----------------------------------------------------------------------------------------------------+
| 13   | time11   | Integer            | 0         | Time Values from 0 to 2880 where each number represents a half minute from midnight to midnight.   |
+------+----------+--------------------+-----------+----------------------------------------------------------------------------------------------------+
| 14   | time12   | Integer            | 0         | Time Values from 0 to 2880 where each number represents a half minute from midnight to midnight.   |
+------+----------+--------------------+-----------+----------------------------------------------------------------------------------------------------+
| 15   | time13   | Integer            | 0         | Time Values from 0 to 2880 where each number represents a half minute from midnight to midnight.   |
+------+----------+--------------------+-----------+----------------------------------------------------------------------------------------------------+
| 16   | time14   | Integer            | 0         | Time Values from 0 to 2880 where each number represents a half minute from midnight to midnight.   |
+------+----------+--------------------+-----------+----------------------------------------------------------------------------------------------------+
| 17   | time15   | Integer            | 0         | Time Values from 0 to 2880 where each number represents a half minute from midnight to midnight.   |
+------+----------+--------------------+-----------+----------------------------------------------------------------------------------------------------+
| 18   | time16   | Integer            | 0         | Time Values from 0 to 2880 where each number represents a half minute from midnight to midnight.   |
+------+----------+--------------------+-----------+----------------------------------------------------------------------------------------------------+
| 19   | data1    | Integer            | 0         | Modifier corresponding with the time value.                                                        |
+------+----------+--------------------+-----------+----------------------------------------------------------------------------------------------------+
| 20   | data2    | Integer            | 0         | Modifier corresponding with the time value.                                                        |
+------+----------+--------------------+-----------+----------------------------------------------------------------------------------------------------+
| 21   | data3    | Integer            | 0         | Modifier corresponding with the time value.                                                        |
+------+----------+--------------------+-----------+----------------------------------------------------------------------------------------------------+
| 22   | data4    | Integer            | 0         | Modifier corresponding with the time value.                                                        |
+------+----------+--------------------+-----------+----------------------------------------------------------------------------------------------------+
| 23   | data5    | Integer            | 0         | Modifier corresponding with the time value.                                                        |
+------+----------+--------------------+-----------+----------------------------------------------------------------------------------------------------+
| 24   | data6    | Integer            | 0         | Modifier corresponding with the time value.                                                        |
+------+----------+--------------------+-----------+----------------------------------------------------------------------------------------------------+
| 25   | data7    | Integer            | 0         | Modifier corresponding with the time value.                                                        |
+------+----------+--------------------+-----------+----------------------------------------------------------------------------------------------------+
| 26   | data8    | Integer            | 0         | Modifier corresponding with the time value.                                                        |
+------+----------+--------------------+-----------+----------------------------------------------------------------------------------------------------+
| 27   | data9    | Integer            | 0         | Modifier corresponding with the time value.                                                        |
+------+----------+--------------------+-----------+----------------------------------------------------------------------------------------------------+
| 28   | data10   | Integer            | 0         | Modifier corresponding with the time value.                                                        |
+------+----------+--------------------+-----------+----------------------------------------------------------------------------------------------------+
| 29   | data11   | Integer            | 0         | Modifier corresponding with the time value.                                                        |
+------+----------+--------------------+-----------+----------------------------------------------------------------------------------------------------+
| 30   | data12   | Integer            | 0         | Modifier corresponding with the time value.                                                        |
+------+----------+--------------------+-----------+----------------------------------------------------------------------------------------------------+
| 31   | data13   | Integer            | 0         | Modifier corresponding with the time value.                                                        |
+------+----------+--------------------+-----------+----------------------------------------------------------------------------------------------------+
| 32   | data14   | Integer            | 0         | Modifier corresponding with the time value.                                                        |
+------+----------+--------------------+-----------+----------------------------------------------------------------------------------------------------+
| 33   | data15   | Integer            | 0         | Modifier corresponding with the time value.                                                        |
+------+----------+--------------------+-----------+----------------------------------------------------------------------------------------------------+
| 34   | data16   | Integer            | 0         | Modifier corresponding with the time value.                                                        |
+------+----------+--------------------+-----------+----------------------------------------------------------------------------------------------------+

Notes
-----

Controls the various values that are related to floats in .LIT files
which was believed just to be the sky positions. There is 18 rows
corresponding to every ID so take the ID\*18 to get the proper start ID
to look at it and the next 17 rows after it go along with it as well

To get the right ID out from Light.dbc (skyParam) you need to calculate
it the following way:

.. math::

    idLightIntBand = lightEntry.skyParam * 18 - 17

The reason is that DBCs always start with entry 1 and in computer fields
you usually have 0 as primary index.
