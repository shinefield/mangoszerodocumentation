.. _db-realm-account:

===============
"account" table
===============

The ``account`` table holds information on all accounts created.

Table structure
---------------

+---------------------+-----------------------+--------+-------+-----------------------+-------------------+
| Field               | Type                  | Null   | Key   | Default               | Extra             |
+=====================+=======================+========+=======+=======================+===================+
| id                  | int(11) unsigned      | NO     | PRI   | NULL                  | auto\_increment   |
+---------------------+-----------------------+--------+-------+-----------------------+-------------------+
| username            | varchar(32)           | NO     | UNI   |                       |                   |
+---------------------+-----------------------+--------+-------+-----------------------+-------------------+
| sha\_pass\_hash     | varchar(40)           | NO     |       |                       |                   |
+---------------------+-----------------------+--------+-------+-----------------------+-------------------+
| gmlevel             | tinyint(3) unsigned   | NO     | MUL   | 0                     |                   |
+---------------------+-----------------------+--------+-------+-----------------------+-------------------+
| sessionkey          | longtext              | YES    |       | NULL                  |                   |
+---------------------+-----------------------+--------+-------+-----------------------+-------------------+
| v                   | longtext              | YES    |       | NULL                  |                   |
+---------------------+-----------------------+--------+-------+-----------------------+-------------------+
| s                   | longtext              | YES    |       | NULL                  |                   |
+---------------------+-----------------------+--------+-------+-----------------------+-------------------+
| email               | text                  | YES    |       | NULL                  |                   |
+---------------------+-----------------------+--------+-------+-----------------------+-------------------+
| joindate            | timestamp             | NO     |       | CURRENT\_TIMESTAMP    |                   |
+---------------------+-----------------------+--------+-------+-----------------------+-------------------+
| last\_ip            | varchar(30)           | NO     |       | 0.0.0.0               |                   |
+---------------------+-----------------------+--------+-------+-----------------------+-------------------+
| failed\_logins      | int(11) unsigned      | NO     |       | 0                     |                   |
+---------------------+-----------------------+--------+-------+-----------------------+-------------------+
| locked              | tinyint(3) unsigned   | NO     |       | 0                     |                   |
+---------------------+-----------------------+--------+-------+-----------------------+-------------------+
| last\_login         | timestamp             | NO     |       | 0000-00-00 00:00:00   |                   |
+---------------------+-----------------------+--------+-------+-----------------------+-------------------+
| active\_realm\_id   | int(11) unsigned      | NO     |       | 0                     |                   |
+---------------------+-----------------------+--------+-------+-----------------------+-------------------+
| expansion           | tinyint(3) unsigned   | NO     |       | 0                     |                   |
+---------------------+-----------------------+--------+-------+-----------------------+-------------------+
| mutetime            | bigint(40) unsigned   | NO     |       | 0                     |                   |
+---------------------+-----------------------+--------+-------+-----------------------+-------------------+
| locale              | tinyint(3) unsigned   | NO     |       | 0                     |                   |
+---------------------+-----------------------+--------+-------+-----------------------+-------------------+

Fields
------

Descriptions for each field with their meaning, usage and relations are
available below.

id
--

The unique identifier for an account.

username
--------

The unique username for an account.

sha\_pass\_hash
---------------

This field contains the encrypted password. The encryption is SHA1 and
is in the following format: ``username:password``.

The SQL to create the password (or to compare with the current hash) is:

.. code-block:: sql

    SELECT
        `username`,
        SHA1(CONCAT(UPPER(`username`), ':', UPPER('password'))),
        `sha_pass_hash`
    FROM `account`;

gmlevel
-------

The access level for an account.

Valid values are:

-  ``0``: Player
-  ``1``: Moderator
-  ``2``: Gamemaster
-  ``3``: Administrator

Additionally an account level of ``4`` is available, but it only applies
to access control within the world server console.

sessionkey
----------

**TODO**

v
-

**TODO**

s
-

**TODO**

email
-----

A well-formed, unique email address for the account.

joindate
--------

The date when the account was created.

last\_ip
--------

A valid `IP address <http://en.wikipedia.org/wiki/IP_address>`__ which
was last used to connect to the realm list.

failed\_logins
--------------

The amount of failed logins for this account. Monitoring this field may
help spotting users who try to gain access to accounts which are not
their own, or who have forgotten their passwords.

locked
------

This is a boolean field, which will lock an account to the IP address
recorded in the ``last_ip`` field when set to ``1``. If set to ``0``, a
user may log in from any IP address and following logins with also
update the ``last_ip`` field.

last\_login
-----------

The date when the account was last logged in.

active\_realm\_id
-----------------

This references the `realmlist <realmlist>`__ tables unique ID of the
realm server on which the account is currently active. This will allow
the game client to connect to the realm the account was active on at the
last login.

expansion
---------

The field controls to which expansion's content a user has access. By
default this is set to ``0``, allowing access to vanilla WoW content. In
mangos-zero, other values can be ignored, since there is no expansion.

mutetime
--------

The time, in Unix time, when the account will be unmuted. To see when
mute will be expired you can use this query:

::

    SELECT `username`, FROM_UNIXTIME(`mutetime`) FROM `account`;

locale
------

The locale used by the client logged into this account. If multiple
locale data has been configured and added to the world servers, the
world servers will return the proper locale strings to the client.

-  ``0``: English
-  ``1``: Korean
-  ``2``: French
-  ``3``: German
-  ``4``: Chinese
-  ``5``: Taiwanese
-  ``6``: Spanish Spain
-  ``7``: Spanish Latin America
-  ``8``: Russian

