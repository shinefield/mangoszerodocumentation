.. _db-world-game-event-mail:

=========================
"game\_event\_mail" table
=========================

The ``game_event_mail`` table holds definitions for mails send out
during game events and conditions for when to send the mail.

Table structure
---------------

+------------------+-------------------------+--------+-------+-----------+---------+
| Field            | Type                    | Null   | Key   | Default   | Extra   |
+==================+=========================+========+=======+===========+=========+
| event            | smallint(6)             | NO     | PRI   | 0         |         |
+------------------+-------------------------+--------+-------+-----------+---------+
| raceMask         | mediumint(8) unsigned   | NO     | PRI   | 0         |         |
+------------------+-------------------------+--------+-------+-----------+---------+
| quest            | mediumint(8) unsigned   | NO     | PRI   | 0         |         |
+------------------+-------------------------+--------+-------+-----------+---------+
| mailTemplateId   | mediumint(8) unsigned   | NO     |       | 0         |         |
+------------------+-------------------------+--------+-------+-----------+---------+
| senderEntry      | mediumint(8) unsigned   | NO     |       | 0         |         |
+------------------+-------------------------+--------+-------+-----------+---------+

Fields
------

event
-----

This references the :doc:`game-event` tables unique ID for
which the entry is valid.

raceMask
--------

A bit-mask corresponding to races that should get the mail. The value
has to match with races defined in :doc:`../../file-formats/dbc/chrraces`.

quest
-----

This references the :doc:`quest-template` tables entry if
the mail is related to a quest.

mailTemplateId
--------------

This references an entry from the
:doc:`../../file-formats/dbc/mailtemplate` table.

senderEntry
-----------

This references the :doc:`creature-template` entry to
be used as sender for the mail.
