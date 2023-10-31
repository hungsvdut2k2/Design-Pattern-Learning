import unittest
from unittest import TestCase
from player import Player
from team import Team


class Evaluate(TestCase):
    def setUp(self):
        self.player1 = Player("John Doe", "Forward", 10)
        self.player2 = Player("Jane Smith", "Midfielder", 8)
        self.player3 = Player("Mark Johnson", "Defender", 4)

        self.team1 = Team("Dream Team")
        self.team1.add_player(self.player1)
        self.team1.add_player(self.player2)

    def test_add_player(self):
        self.assertEqual(len(self.team1.players), 2)
        self.assertIn(self.player1, self.team1.players)
        self.assertIn(self.player2, self.team1.players)

    def test_get_player_info(self):
        self.assertEqual(self.team1.get_player_info(10), "John Doe (Forward) - 10")
        self.assertEqual(self.team1.get_player_info(8), "Jane Smith (Midfielder) - 8")
        self.assertEqual(self.team1.get_player_info(4), "Player not found")


if __name__ == "__main__":
    unittest.main()
