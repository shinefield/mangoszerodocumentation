.. _file-formats-dbc-gmsurveyquestions:

=====================
GMSurveyQuestions.dbc
=====================

The *game master survey questions* table contains questions to be asked during a game master survey,
which is usually issued after a ticket is closed.

Table structure
---------------

+------+------------+----------------------+-----------+-----------------------------+
| ID   | Name       | Type                 | Default   | Description                 |
+======+============+======================+===========+=============================+
| 1    | ID         | Integer              | -         | Unique ID                   |
+------+------------+----------------------+-----------+-----------------------------+
| 2    | question   | String (localized)   | -         | The question to be asked.   |
+------+------------+----------------------+-----------+-----------------------------+
