.. _file-formats-dbc-wowerror-strings:

=====================
WowError\_Strings.dbc
=====================

The *Wow error strings* table contains definitions for error messages
used in the World of Warcraft crash reporting utility.

.. note::

    This file is not reference from any other DBC files and does not
    reference other DBC files.

Table structure
---------------

+------+---------------+----------------------+-----------+------------------------------------------------------------------------------------------------+
| ID   | Name          | Type                 | Default   | Description                                                                                    |
+======+===============+======================+===========+================================================================================================+
| 1    | ID            | Integer              | -         | Unique ID                                                                                      |
+------+---------------+----------------------+-----------+------------------------------------------------------------------------------------------------+
| 2    | errorName     | String               | -         | A hard-coded name used in the crash reporting utility to identify and load the error string.   |
+------+---------------+----------------------+-----------+------------------------------------------------------------------------------------------------+
| 3    | errorString   | String (localized)   | -         | The actual string to be printed in the crash reporting utilities interface.                    |
+------+---------------+----------------------+-----------+------------------------------------------------------------------------------------------------+
