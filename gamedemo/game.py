"""
    game.py
    -------

    This module contains the Game class that implements the actual game mechanics as well as
    the __main__ construct to make the game runnable.
"""

from gamedemo.player import Player
from gamedemo.weapons import Weapon, Sword, FireBreath
__author__ = "Reindert-Jan Ekker"

import random
import sys
import os

#sys.path.insert(0, os.path.abspath('..'))
# sphinx-apidoc gamedemo --full -o docs --force --separate --implicit-namespaces -a --module-first -H my_project -A Laci -V 100 -R 10
sys.path.insert(0, os.path.abspath('..'))
sys.path.insert(0, os.path.abspath('.'))


class Game:
    """
    The Game class implements the game mechanics for this demo. To understand the way the
    game works, read the documentation for the :meth:`run` method.
    """

    def __init__(self, player1, player2):
        """
        Create a new game with two players.

        :param player1: First player
        :param player2: Second player
        """
        self.p1 = player1
        self.p2 = player2

    def run(self):
        """
        This method implements the game mechanics. The game loops until one of the players
        runs out of health. Every turn, one of the players is randomly chosen to attack. We
        call the :meth:`~gamedemo.weapon.Weapon.attack` method on that player's weapon.
        The damage dealt by this attack is applied to the player by calling
        :meth:`gamedemo.player.Player.take_hit`.
        """
        print(self.p1)
        print(self.p2)
        while self.p1.is_alive and self.p2.is_alive:
            if random.choice([True, False]):
                attacker = self.p1
                defender = self.p2
            else:
                attacker = self.p2
                defender = self.p1
            dmg, sound = attacker.weapon.attack()
            print(attacker.name, "attacks:", sound)
            print(attacker.name, "did", dmg, "damage")
            defender.take_hit(dmg)
        print(attacker.name, "won with", attacker.health, "health left")


if __name__ == "__main__":
    random.seed()
    g = Game(
        Player("The Knight", Sword()),
        Player("The Dragon", FireBreath())
    )
    g.run()
