Servers
=======

To run your own `World of Warcraft`_ game, we provide two servers:

.. _World of Warcraft: : http://blizzard.com/games/wow/

* the authentication service, also known as *realmd* or ream list server,
* the world service, also known as *mangosd* or game world server.

Both services can be run as POSIX daemon, or Windows service in the
background, and rely on an active IP4 address to which they bind.

Each services store their data within a MySQL or PostgreSQL server,
which can be local or remote.

Authentication service
======================

The realm list server is listening on port **3724** - which might
have to be enabled in your firewall - for game client connections.

The realm list is responsible for various tasks:

* authenticate users using a variant of `SRP`_ coming from the game client,
* manage accounts, and their access rights,
* block accounts based on account name or IP address,
* deliver patch files for the game client,
* routing authenticated users to the game world.

.. _SRP: http://srp.stanford.edu/
