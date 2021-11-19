import unittest
from classes.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Happy Birthday", 1.5)

    
    def test_song_has_name(self):
        self.assertEqual("Happy Birthday", self.song.name)

    def test_song_has_duration(self):
        self.assertEqual(1.5, self.song.duration)