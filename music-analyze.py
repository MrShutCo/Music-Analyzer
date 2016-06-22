import midi

class MidiReaderThing:

    def __init__(self, name):
        self.tracks = []
        self.name = name
        self.song = midi.read_midifile(name+".mid")

    def create_song(self):
        for tracks in self.song:
            track = Track()
            for note in track.notes:
                #Just slowly fill this in with the different cases for adding notes other events
                if (notes.name == "Note On"):
                    noteTemp = Note(notes.get_pitch())
                    track.add_note(noteTemp)
                #TODO: If theres no tempo in at track, just assume the first found tempo
                if (notes.name == "Set Tempo"):
                    track.set_tempo(notes.get_bpm())
                    
            self.tracks.append(tracks)
        return Song(self.name)

    def convert_to_notes(self, noteBytes):
        Notes = [];
        noteNames = [ "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
        noteOctaves = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        for byte in noteBytes:
            rowNo = byte / 12
            colNo = byte % 12
            Notes.append(noteNames[colNo] + noteOctaves[rowNo])
        return Notes
        

#Song class will no longer contain the Events, but instead our custom notes, with proper timing
class Song:

    def __init__(self, name):
        self.name = name
        self.timeSig = "4/4"
        self.Tracks = []

class Track:

    def __init__(self):
        self.name = None
        self.tempo = None
        self.notes = [] #Replace with n-vector later

    def set_name(self, name):
        self.name = name

    def set_tempo(self, tempo):
        self.tempo = tempo

    #Gonna have to change this later to include length of note, but assume quarter note now
    def add_note(self, note):
        self.notes.append(note)

class Note:

    def __init__(self, track, note):
        self.note = note
        self.track = track
        #self.length = length #Change this to convert to note

def main():
    test = MidiReaderThing("mary")
    song = test.create_song()

main()

