.. _file-formats-dbc-languagewords:

=================
LanguageWords.dbc
=================

The *language words* table contains definitions for syllables connected
to specific in-game languages. These are mostly used when a character
can not understand a language.

Table structure
---------------

+------+--------------+--------------------+-----------+--------------------------+
| ID   | Name         | Type               | Default   | Description              |
+======+==============+====================+===========+==========================+
| 1    | ID           | Integer            | -         | Unique ID                |
+------+--------------+--------------------+-----------+--------------------------+
| 2    | language     | Integer            | 0         | The language used.       |
+------+--------------+--------------------+-----------+--------------------------+
| 3    | word         | String             | -         | The language syllable.   |
+------+--------------+--------------------+-----------+--------------------------+

Relations
---------

-  ``language`` references the primary key of ``Languages.dbc``.
