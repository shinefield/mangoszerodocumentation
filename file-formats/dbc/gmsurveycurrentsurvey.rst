.. _file-formats-dbc-gmsurveycurrentsurvey:

=========================
GMSurveyCurrentSurvey.dbc
=========================

The *game master current survey* table connects current game master surveys to client languages.

Table structure
---------------

+------+--------------+--------------------+-----------+--------------------------------------------+
| ID   | Name         | Type               | Default   | Description                                |
+======+==============+====================+===========+============================================+
| 1    | language     | Integer            | 0         | See below.                                 |
+------+--------------+--------------------+-----------+--------------------------------------------+
| 2    | gmSurvey     | Integer            | 0         | The current survey for a given language.   |
+------+--------------+--------------------+-----------+--------------------------------------------+

Fields
------

langID
~~~~~~

-  ``0``: English
-  ``1``: Korean
-  ``2``: French
-  ``3``: German
-  ``4``: Chinese
-  ``5``: Taiwanese
-  ``6``: Spanish - Spain
-  ``7``: Spanish - Latin America

Relations
---------

-  ``gmSurvey`` references the primary key of :doc:`gmsurveysurveys`.
