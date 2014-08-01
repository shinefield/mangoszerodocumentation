.. _file-formats-dbc-loadingscreens:

==================
LoadingScreens.dbc
==================

The *loading screens* table contains definitions for available zone
loading screens.

Table structure
---------------

+------+------------+--------------------+-----------+-----------------------------------------+
| ID   | Name       | Type               | Default   | Description                             |
+======+============+====================+===========+=========================================+
| 1    | ID         | Integer (signed)   | -         | Unique ID                               |
+------+------------+--------------------+-----------+-----------------------------------------+
| 2    | name       | String             | -         | The name of the loading screen.         |
+------+------------+--------------------+-----------+-----------------------------------------+
| 3    | fileName   | String             | -         | The path to the loading screen image.   |
+------+------------+--------------------+-----------+-----------------------------------------+
