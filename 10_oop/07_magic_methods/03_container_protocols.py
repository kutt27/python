"""
Topic: Container Protocols.

Special methods that make your object behave like a list or dictionary.
`__len__`: Support for len(obj)
`__getitem__`: Support for obj[idx]
"""

class Playlist:
    def __init__(self):
        self._songs = []
        
    def add_song(self, name):
        self._songs.append(name)
        
    def __len__(self):
        return len(self._songs)
        
    def __getitem__(self, index):
        return self._songs[index]

if __name__ == "__main__":
    p = Playlist()
    p.add_song("Song A")
    p.add_song("Song B")
    
    print(f"playlist length: {len(p)}")
    print(f"First song: {p[0]}")
    
    # Since it supports indexing, it also supports simple iteration
    for song in p:
        print(f"  Playing: {song}")
