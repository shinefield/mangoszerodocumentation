.. _db-realm-ip-banned:

==================
"ip\_banned" table
==================

The ``ip_banned`` table holds information on all IP addresses which have
been banned from logging in.

Table structure
---------------

+-------------+----------------+--------+-------+-------------+---------+
| Field       | Type           | Null   | Key   | Default     | Extra   |
+=============+================+========+=======+=============+=========+
| ip          | varchar(32)    | NO     | PRI   | 0.0.0.0     |         |
+-------------+----------------+--------+-------+-------------+---------+
| bandate     | bigint(40)     | NO     | PRI   | NULL        |         |
+-------------+----------------+--------+-------+-------------+---------+
| unbandate   | bigint(40)     | NO     |       | NULL        |         |
+-------------+----------------+--------+-------+-------------+---------+
| bannedby    | varchar(50)    | NO     |       | [Console]   |         |
+-------------+----------------+--------+-------+-------------+---------+
| banreason   | varchar(255)   | NO     |       | no reason   |         |
+-------------+----------------+--------+-------+-------------+---------+

Fields
------

Descriptions for each field with their meaning, usage and relations are
available below.

ip
~~

A valid `IP address`_ which is blocked from connecting to the realm list
server and thus from connecting to world servers, too.

bandate
~~~~~~~

The date on which the IP address has been banned. This is saved as a
`Unix timestamp`_.

unbandate
~~~~~~~~~

The date on which the IP address will be unbanned. If not set, the IP
address will be banned indefinitely. This is saved as a `Unix timestamp`_.

bannedby
~~~~~~~~

The account name of the user who banned the IP address. This references
the :doc:`account <account>` tables ``username`` field.

banreason
~~~~~~~~~

A short comment describing the reason for the IP address ban.

.. _IP address:     http://en.wikipedia.org/wiki/IP_address
.. _Unix timestamp: http://en.wikipedia.org/wiki/Unix_time
