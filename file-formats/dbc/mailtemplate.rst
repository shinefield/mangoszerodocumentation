.. _file-formats-dbc-mailtemplate:

================
MailTemplate.dbc
================

The *mail template* table contains definitions for mails sent by
non-player characters.

Table structure
---------------

+------+--------+----------------------+-----------+------------------------------------+
| ID   | Name   | Type                 | Default   | Description                        |
+======+========+======================+===========+====================================+
| 1    | ID     | Integer (signed)     | -         | Unique ID                          |
+------+--------+----------------------+-----------+------------------------------------+
| 2    | body   | String (localized)   | -         | The mail templates body content.   |
+------+--------+----------------------+-----------+------------------------------------+

