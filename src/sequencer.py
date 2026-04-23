# # CALENDAW: SEQUENCER MODULE
# ## 👁️ SYSTEM LOGIC: MIDI GENERATION
# This module creates a standard MIDI file for testing.
# [SOURCE: Inspired by MIDIUtil standard documentation]

from midiutil import MIDIFile
import os

def generate_test_pattern():
    print("Generating MIDI pattern...")
    mf = MIDIFile(1)
    track, time = 0, 0
    mf.addTrackName(track, time, "Calendaw_Test_Track")
    mf.addTempo(track, time, 120)

    # Add a Middle C (60)
    mf.addNote(track, 0, 60, time, 1, 100)

    output_path = os.path.expanduser("~/Calendaw/data/Audio/Midi/test_pattern.mid")
    
    # Ensure the directory exists [cite: 6]
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "wb") as outf:
        mf.writeFile(outf)
    print(f"MIDI successfully rendered to: {output_path}")

if __name__ == "__main__":
    generate_test_pattern()