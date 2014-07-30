.. _db-realm-account-banned:

=======================
"account\_banned" table
=======================

The ``account_banned`` table holds information on all accounts which
have been banned from logging in.

Table structure
---------------

+-------------+--------------------+--------+-------+-----------+---------+
| Field       | Type               | Null   | Key   | Default   | Extra   |
+=============+====================+========+=======+===========+=========+
| id          | int(11) unsigned   | NO     | PRI   | NULL      |         |
+-------------+--------------------+--------+-------+-----------+---------+
| bandate     | bigint(40)         | NO     | PRI   | 0         |         |
+-------------+--------------------+--------+-------+-----------+---------+
| unbandate   | bigint(40)         | NO     |       | 0         |         |
+-------------+--------------------+--------+-------+-----------+---------+
| bannedby    | varchar(50)        | NO     |       | NULL      |         |
+-------------+--------------------+--------+-------+-----------+---------+
| banreason   | varchar(255)       | NO     |       | NULL      |         |
+-------------+--------------------+--------+-------+-----------+---------+
| active      | tinyint(4)         | NO     |       | 1         |         |
+-------------+--------------------+--------+-------+-----------+---------+

Fields
------

Descriptions for each field with their meaning, usage and relations are
available below.

id
--

The account of the user banned. This references the unique key of the
`account <account>`__ table.

bandate
-------

The date on which the IP address has been banned.

unbandate
---------

The date on which the IP address will be unbanned. If not set, the IP
address will be banned indefinitely.

bannedby
--------

The account name of the user who banned the IP address. This references
the `account <account>`__ tables ``username`` field.

banreason
---------

A short comment describing the reason for the IP address ban.

active
------

Describes if a ban is currently active, or not.

-  ``0``: ban is inactive,
-  ``1``: ban is active

