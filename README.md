# MIDI2Chime
Converts MIDI files to Chime numbers. Outputs a text file with notes and rests.   
`*` = hold note  
`-` = rest

## Usage
`pip install -r requirements.txt`  
`python main.py`

### Inputs:  
filename: midi file (notes must be between A#3 and E5)  
output filename: output text file to write to  
number of parts: number of chime parts (notes played at the same time)
smallest quarter division: smallest note in terms of quarter divisions  

To change the number of characters before wrap: edit `max_line_length` (line 27)

