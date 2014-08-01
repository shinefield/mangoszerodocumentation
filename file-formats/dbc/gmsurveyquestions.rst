.. _file-formats-dbc-gmsurveyquestions:

=====================
GMSurveyQuestions.dbc
=====================

The *game master survey questions* table contains definitions for
questions asked after game master support has been provided.

Table structure
---------------

+------+------------+----------------------+-----------+-----------------------------+
| ID   | Name       | Type                 | Default   | Description                 |
+======+============+======================+===========+=============================+
| 1    | ID         | Integer (signed)     | -         | Unique ID                   |
+------+------------+----------------------+-----------+-----------------------------+
| 2    | Question   | String (localized)   | -         | The question to be asked.   |
+------+------------+----------------------+-----------+-----------------------------+
