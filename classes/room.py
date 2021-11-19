
class Room:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.song_list = []
        self.guest_list = [] 


    def add_guest(self, guest):
        self.guest_list.append(guest) 

    def guest_count(self):
        return len(self.guest_list)

    def remove_guest(self, guest):
        self.guest_list.remove(guest)



    def add_song(self, song):
        self.song_list.append(song)

    def song_count(self):
        return len(self.song_list)

    def remove_song(self, song):
        self.song_list.remove(song)


