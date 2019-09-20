from music21 import *

map = {
    "A#3": 1,
    "B-3": 1,
    "B3": 2,
    "C4": 3,
    "C#4": 4,
    "D-4": 4,
    "D4": 5,
    "D#4": 6,
    "E-4": 6,
    "E4": 7,
    "F4": 8,
    "F#4": 9,
    "G-4": 9,
    "G4": 10,
    "G#4": 11,
    "A-4": 11,
    "A4": 12,
    "A#4": 13,
    "B-4": 13,
    "B4": 14,
    "C5": 15,
    "C#5": 16,
    "D-5": 16,
    "D5": 17,
    "D#5": 18,
    "E-5": 18,
    "E5": 19
}

# each note is 3 chars long
# number of chars before line wrap
max_line_length = 16 * 3

# splits output string into chunks of max_line_length size
def chunker(l, max_line_length):
    length = len(l[0])
    cur_length = 0
    while cur_length + max_line_length < length:
        yield [x[cur_length: cur_length + max_line_length] for x in l]
        cur_length += max_line_length
    yield [x[cur_length:] for x in l]

def main():
    filename = input("Filename: ")
    outfile = input("Output filename: ")

    s = converter.parse(filename)
    simultaneous_lines = int(input("Number of parts (at least 1): "))
    if simultaneous_lines < 1:
        print("Needs at least 1 part.")
        return 1
    
    lines = [""] * simultaneous_lines
    #smallest note in terms of quarter divisions eg 16th = 4, 8th = 2, quarter = 1
    smallest_quarter_division = int(input("Smallest Quarter Division (16th=4, 8th=2, Quarter=1): "))
    
    for note in s.recurse(classFilter=('Note', 'Rest', 'Chord')):
        if (note.isRest):
            dashes = round(note.duration.quarterLength * smallest_quarter_division - 1)
            lines[0] += ('*  ' + ('*  ' * dashes))
            for i in range(1, simultaneous_lines):
                lines[i] += ('*  ' + ('*  ' * dashes))

        if (note.isNote):
            stars = round(note.duration.quarterLength * smallest_quarter_division - 1)
            note_name = str(map[note.nameWithOctave])
            lines[0] += (note_name + (' ' * (3 -len(note_name))) + ('-  ' * stars))
            for i in range(1, simultaneous_lines):
                lines[i] += ('*  ' + ('*  ' * stars))

        if (note.isChord):
            max_i = 0
            stars = round(note.duration.quarterLength * smallest_quarter_division - 1)
            for (i, note_) in enumerate(note):
                note_name = str(map[note_.nameWithOctave])
                lines[i] += (note_name + (' ' * (3 - len(note_name)))+ ('-  ' * stars))
                max_i = i
            for i in range(max_i + 1, simultaneous_lines):
                lines[i] += ('*  ' + ('*  ' * stars))


    with open(outfile, "w") as f:
        f.write("Quarter = (" + '  '.join(['-'] * smallest_quarter_division) + ')\n\n')
        for chunk in chunker(lines, max_line_length):
            f.write('\n'.join(chunk))
            f.write('\n\n')


if __name__ == '__main__':
    main()