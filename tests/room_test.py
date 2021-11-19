import unittest
from classes.room import Room 
from classes.guest import Guest
from classes.song import Song


class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room = Room("room 1", 8)
        #above we have room_name and room_capacity
        self.guest_1 = Guest("Mario", 20)
        self.guest_2 = Guest("Sandra", 25)
        self.song_1 = Song("Bad Birthday", 2.5)
        self.song_2 = Song("Smily Birthday", 3.0)

    def test_room_has_name(self):
        self.assertEqual("room 1", self.room.name)

    def test_room_has_capacity(self):
        self.assertEqual(8, self.room.capacity)

    def test_room_can_add_guests(self):
        self.room.add_guest(self.guest_1)
        self.assertEqual(1, self.room.guest_count())

    def test_room_can_remove_guests(self):
        self.room.add_guest(self.guest_1)
        self.room.add_guest(self.guest_2)
        self.room.remove_guest(self.guest_2)
        self.assertEqual(1, self.room.guest_count())



    def test_room_can_add_songs(self):
        self.room.add_song(self.song_1)
        self.assertEqual(0, self.room.song_count())



    # def test_room_can_remove_songs(self):
    #     self.room.add_song(self.song_1)
    #     self.room.add_song(self.song_2)
    #     self.room.remove_song(self.guest_2)
    #     self.assertEqual(1, self.room.song_count())

