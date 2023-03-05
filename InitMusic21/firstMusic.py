from music21 import *

note1 = note.Note("C4")
note2 = note.Note("F#4")

note1.duration.type = 'half'
note1.duration.quarterLength

note2.duration.quarterLength

print(note1.step)
""" C """
print(note2.step)
""" F """
noteList = [note1, note2]

print(noteList)
""" [<music21.note.Note C>, <music21.note.Note F#>] """

for thisNote in noteList:
    print(thisNote.step)
""" C
    F """
note3 = note.Note("B-2")
noteList.append(note3)

print(noteList)

len(noteList)
""" [<music21.note.Note C>, <music21.note.Note F#>, <music21.note.Note B->] """

for thisNote in noteList:
    print(thisNote.step)
""" C
    F
    B """
noteList[0]
"""  <music21.note.Note C> """
noteList[1]
"""  <music21.note.Note F#> """

noteList.index(note2)
""" 1 """

noteList[-1]
"""  <music21.note.Note B-> """

noteList[-1] is noteList[2]
""" True """