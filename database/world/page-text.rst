.. _db-world-page-text:

==================
"page\_text" table
==================

The ``page_text`` table holds texts for any readable item. This includes
letters as well as books, and other readable items such as game objects.

Each text entry is a *singular* page. For books, pages are connected.

Table structure
---------------

+--------------+-------------------------+--------+-------+-----------+---------+
| Field        | Type                    | Null   | Key   | Default   | Extra   |
+==============+=========================+========+=======+===========+=========+
| entry        | mediumint(8) unsigned   | NO     | PRI   | 0         |         |
+--------------+-------------------------+--------+-------+-----------+---------+
| text         | longtext                | NO     |       | NULL      |         |
+--------------+-------------------------+--------+-------+-----------+---------+
| next\_page   | mediumint(8) unsigned   | NO     |       | 0         |         |
+--------------+-------------------------+--------+-------+-----------+---------+

Fields
------

entry
-----

The unique identifier for the text.

text
----

The page's text message. This is shown in-game.

next\_page
----------

If the page is followed by another page, this references the unique ID
of the `page\_text <page_text>`__ table.
