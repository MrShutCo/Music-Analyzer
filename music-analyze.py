import midi

class MidiReaderThing:

    def __init__(self, name):
        song = midi.read_midifile(name+".mid")
        notesList = []
        for tracks in song:
            for notes in tracks:
                if (notes.name == "Note On"):
                    notesList.append(notes.get_pitch())
        notesList = self.ConvertToNotes(notesList)
        for i in notesList:
            print i

    def ConvertToNotes(self, noteBytes):
        Notes = [];
        noteNames = [ "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
        noteOctaves = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        for byte in noteBytes:
            rowNo = byte / 12
            colNo = byte % 12
            Notes.append(noteNames[colNo] + noteOctaves[rowNo])
        return Notes
        

def main():
    test = MidiReaderThing("Glycerine")

main()



