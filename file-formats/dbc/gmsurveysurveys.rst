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
| 1    | ID             | Integer            | -         | Unique ID                 |
+------+----------------+--------------------+-----------+---------------------------+
| 2    | question1      | Integer            | 0         | A question to be asked.   |
+------+----------------+--------------------+-----------+---------------------------+
| 3    | question2      | Integer            | 0         | A question to be asked.   |
+------+----------------+--------------------+-----------+---------------------------+
| 4    | question3      | Integer            | 0         | A question to be asked.   |
+------+----------------+--------------------+-----------+---------------------------+
| 5    | question4      | Integer            | 0         | A question to be asked.   |
+------+----------------+--------------------+-----------+---------------------------+
| 6    | question5      | Integer            | 0         | A question to be asked.   |
+------+----------------+--------------------+-----------+---------------------------+
| 7    | question6      | Integer            | 0         | A question to be asked.   |
+------+----------------+--------------------+-----------+---------------------------+
| 8    | question7      | Integer            | 0         | A question to be asked.   |
+------+----------------+--------------------+-----------+---------------------------+
| 9    | question8      | Integer            | 0         | A question to be asked.   |
+------+----------------+--------------------+-----------+---------------------------+
| 10   | question9      | Integer            | 0         | A question to be asked.   |
+------+----------------+--------------------+-----------+---------------------------+
| 11   | question10     | Integer            | 0         | A question to be asked.   |
+------+----------------+--------------------+-----------+---------------------------+

Relations
---------

-  ``question[1-10]`` reference the primary key of :doc:`gmsurveyquestions`.
