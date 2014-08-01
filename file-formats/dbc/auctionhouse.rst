.. _file-formats-dbc-auctionhouse:

================
AuctionHouse.dbc
================

The *auction house* table contains definitions for available auction
houses for each faction including payments for placing auctions.

Table structure
---------------

+------+-------------------+----------------------+-----------+--------------------------------------------------------------+
| ID   | Name              | Type                 | Default   | Description                                                  |
+======+===================+======================+===========+==============================================================+
| 1    | ID                | Integer (signed)     | -         | Unique ID                                                    |
+------+-------------------+----------------------+-----------+--------------------------------------------------------------+
| 2    | factionID         | Integer (signed)     | 0         | References the faction to which the auction house belongs.   |
+------+-------------------+----------------------+-----------+--------------------------------------------------------------+
| 3    | depositRate       | Integer              | 0         | The auction house's cut of the final earnings.               |
+------+-------------------+----------------------+-----------+--------------------------------------------------------------+
| 4    | consignmentRate   | Integer              | 0         | The deposit fee based on the sale price.                     |
+------+-------------------+----------------------+-----------+--------------------------------------------------------------+
| 5    | name              | String (localized)   | -         | The name of the auction house.                               |
+------+-------------------+----------------------+-----------+--------------------------------------------------------------+

Relations
---------

-  ``factionID`` references the primary key of ``Faction.dbc``.
