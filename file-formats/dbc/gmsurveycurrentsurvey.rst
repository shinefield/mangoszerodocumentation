.. _file-formats-dbc-gmsurveycurrentsurvey:

=========================
GMSurveyCurrentSurvey.dbc
=========================

The *game master current survey* table contains definitions for
connecting languages to game master surveys.

Table structure
---------------

+------+--------------+--------------------+-----------+--------------------------------------------+
| ID   | Name         | Type               | Default   | Description                                |
+======+==============+====================+===========+============================================+
| 1    | langID       | Integer            | 0         | See below.                                 |
+------+--------------+--------------------+-----------+--------------------------------------------+
| 2    | gmSurveyID   | Integer (signed)   | 0         | The current survey for a given language.   |
+------+--------------+--------------------+-----------+--------------------------------------------+

Fields
------

langID
------

-  ``0``: English
-  ``1``: Korean
-  ``2``: French
-  ``3``: German
-  ``4``: Chinese
-  ``5``: Taiwanese
-  ``6``: Spanish Spain
-  ``7``: Spanish Latin America
-  ``8``: Russian

Relations
---------

-  ``gmSurveyID`` references the primary key of ``GMSurveySurveys.dbc``.

