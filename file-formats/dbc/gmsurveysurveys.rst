.. _file-formats-dbc-gmsurveysurveys:

===================
GMSurveySurveys.dbc
===================

The *game master surveys* table contains definitions for questions
contained in a survey.

Table structure
---------------

+------+----------------+--------------------+-----------+---------------------------+
| ID   | Name           | Type               | Default   | Description               |
+======+================+====================+===========+===========================+
| 1    | ID             | Integer (signed)   | -         | Unique ID                 |
+------+----------------+--------------------+-----------+---------------------------+
| 2    | QuestionID1    | Integer (signed)   | 0         | A question to be asked.   |
+------+----------------+--------------------+-----------+---------------------------+
| 3    | QuestionID2    | Integer (signed)   | 0         | A question to be asked.   |
+------+----------------+--------------------+-----------+---------------------------+
| 4    | QuestionID3    | Integer (signed)   | 0         | A question to be asked.   |
+------+----------------+--------------------+-----------+---------------------------+
| 5    | QuestionID4    | Integer (signed)   | 0         | A question to be asked.   |
+------+----------------+--------------------+-----------+---------------------------+
| 6    | QuestionID5    | Integer (signed)   | 0         | A question to be asked.   |
+------+----------------+--------------------+-----------+---------------------------+
| 7    | QuestionID6    | Integer (signed)   | 0         | A question to be asked.   |
+------+----------------+--------------------+-----------+---------------------------+
| 8    | QuestionID7    | Integer (signed)   | 0         | A question to be asked.   |
+------+----------------+--------------------+-----------+---------------------------+
| 9    | QuestionID8    | Integer (signed)   | 0         | A question to be asked.   |
+------+----------------+--------------------+-----------+---------------------------+
| 10   | QuestionID9    | Integer (signed)   | 0         | A question to be asked.   |
+------+----------------+--------------------+-----------+---------------------------+
| 11   | QuestionID10   | Integer (signed)   | 0         | A question to be asked.   |
+------+----------------+--------------------+-----------+---------------------------+

Relations
---------

-  ``QuestionID[1-10]`` reference the primary key of
   ``GMSurveyQuestions.dbc``.
