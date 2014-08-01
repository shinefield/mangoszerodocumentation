.. _db-contributing-content-research:

================
Content Research
================

In order to populate the database with clean content, each update begins
with a *research* process, which you will get to know here.

Introduction
------------

Since the original release of `World of Warcraft`_ was in November 2004 for
US players and February 2005 for EU players, most original documentation
and sources of information provided by `Blizzard Entertainment`_ or by the
player community is gone.

Thankfully, a very active player base, a few game database sites and a
few other resources remain available to this day. Which these are and
how you can and should use them is the focus of this document.

Available resources
-------------------

There are several different types of resources available:

-  game database sites: these sites did use several methods to record
   game content, either via storing game data from within the games user
   interface in `Lua`_ files, or via gathering the game's cache files,
   commonly known as **WDB** files. Some even used a combination of both to
   cross-reference and verify game data.
-  fan sites: fan sites usually gather anything posted about the game
   and post it including their own view points on game updates. While
   these may not be resources for data, they may provide insight on how
   certain features worked during their release.
-  official sites: during the early days of the game, `Blizzard Entertainment`_
   ran dedicated websites for `World of Warcraft`_, which covered game
   features and updates. Sadly the original sites are not available any
   more and only little is left on the current site.
-  web archives: the `wayback machine`_ has been running for quite a few
   years, and allows us to look at old websites, archived versions of the
   site types described above. Most of the old sites long gone are still
   accessible there.
-  game guides, books: `BradyGames`_ has released several books on each
   game expansion. In common these books are of good quality, since
   BradyGames has used data provided by `Blizzard Entertainment`_ to
   populate the book's tables.
-  cached game data: on rare occasions there are **WDB** files available
   created by the game. These can be parsed to extract some basic and
   some advanced game data.

Ranking resources
-----------------

Sadly not all available resources are of equal value. Some contain
incomplete data, others already contain data for game content for
expansions of the game, and some may even contain wrong content.

Thus we provide a quick run-down of how each available resource is to be
valued, and which information should be valued "more" valid than others.

Resource list, books
--------------------

These books by `BradyGames`_ can be considered authoritative since they do
provide original game data:

-  `World of Warcraft Official Strategy Guide <http://www.wowpedia.org/World_of_Warcraft_Official_Strategy_Guide>`__
-  `World of Warcraft Master Guide, Second Edition <World of Warcraft Master Guide, Second Edition <http://www.wowpedia.org/World_of_Warcraft_Master_Guide,_Second_Edition>`__
-  `World of Warcraft Battle Chest Guide <http://www.wowpedia.org/World_of_Warcraft_Battle_Chest_Guide>`__
-  `World of Warcraft: Dungeon Companion <http://www.wowpedia.org/World_of_Warcraft:_Dungeon_Companion>`__

Please note that the *Strategy Guide* covers World of Warcraft version
1.0, which was the last version before the game's release version 1.1.
Using this as a base, it is possible to find out when content was added.

The *Master Guide*, the *Battle Chest Guide* and the *Dungeon Companion*
cover content for the game's release version 1.12, thus providing us
with a clear view on which content was available in the last branch of
vanilla WoW.

It is important to note that none of these books covers extended stats
for creatures, quests, etc.; only the basics are covered.

Thus it should be considered that these books at least provide a view on
what content actually existed and what did not exist during vanilla WoW.

Resource list, game databases
-----------------------------

Ever since the inception of `World of Warcraft`_, people have tried to
gather game content in online database to make it easier for other
players to explore and enjoy the game. Some are gone, others still
exist. This section will show you those still in existence.

-  `Wowhead <http://www.wowhead.com/>`__: ever since 2006, Wowhead
   gathers game data both via uploaded *WDB* files and gathering in-game
   data with the client's Lua interface. The most interesting feature of
   Wowhead still is the comments section for game data. Usually you will
   be able to lookup creatures, quests, items, game objects and spells,
   and can use the comments combined with the data displayed to find out
   more on game data.
-  `Wowhead archive site <http://old.wowhead.com/>`__: With the release
   of the `Cataclym <http://us.blizzard.com/en-us/games/cataclysm/>`__
   expansion, Wowhead moved old game data for every expansion up to
   `Wrath of the Lich
   King <http://us.blizzard.com/en-us/games/wrath/>`__
-  including `The Burning
   Crusade <http://us.blizzard.com/en-us/games/burningcrusade/>`__ -
   into their archive site. In many cases the archive site allows you to
   view game data, in an older state, and thus can be used to verify
   older data.
-  `WowPeek <http://www.wowpeek.com/>`__: WowPeek was targeted at `The
   Burning
   Crusade <http://us.blizzard.com/en-us/games/burningcrusade/>`__, and
   gathered game data via *WDB* files and in-game data via the client's
   Lua interface. While not as comprehensive as Wowhead, it still has
   benefits, and may be used to cross-reference data from the Wowhead
   archive site.
-  `Sigrie <http://db.mmo-champion.com/>`__: MMO-Champion started a game
   database of its' own with the `Wrath of the Lich
   King <http://us.blizzard.com/en-us/games/wrath/>`__, mainly to reduce
   reliance on Wowhead for linking game data in their news posts. What
   Sigrie excels in, is completeness. While Wowhead usually only offers
   game objects, that are somehow connected to quests, Sigrie simply
   imported *all* via *WDB* files. This is very useful to find missing
   game objects, and also missing creatures.
-  `WowDB <http://www.wowdb.com/>`__: with
   `Cataclysm <http://us.blizzard.com/en-us/games/cataclysm/>`__
   MMO-Champion wanted to do something different, and improve the
   integration of their game content site with the Curse network. To
   this day, WoWDB still is maintained and offers valuable data. Sadly
   it is not much of use for anything preceding the Cataclysm.

Resource list, fan sites
------------------------

Resource list, archived sites
-----------------------------

.. _Blizzard Entertainment:   http://blizzard.com/
.. _World of Warcraft:        http://blizzard.com/games/wow/

.. _Lua:                      http://www.lua.org/
.. _wayback machine:          http://web.archive.org/

.. _BradyGames:               http://www.bradygames.com/
