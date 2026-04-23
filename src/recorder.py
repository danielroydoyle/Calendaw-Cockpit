# # CALENDAW: RECORDER MODULE (V2.2 - VELOCITY FIX)
# ## 🧬 PROVENANCE: Zrythm (src/dsp/transport.h) | Alexandros Theodotou
# ## #HTCP-Type: Performance_Capture
# ## #HTCP-Context: Preserves Note-On velocity for dynamic capture.

import mido
import time
from midiutil import MIDIFile
import os

TICKS_PER_BEAT = 960

def record_performance(bpm=120):
    print(f"--- CALENDAW CLOCK INITIALIZED ({bpm} BPM) ---")
    input_names = mido.get_input_names()
    if len(input_names) < 2:
        print("ERROR: Yamaha not found at expected port. Check connections.")
        return
    
    captured_events = []
    start_time = time.perf_counter() 
    
    try:
        # Listening to Port [1] (Your Yamaha)
        with mido.open_input(input_names[1]) as inport:
            print("⏺️ PERFORMANCE ACTIVE. PRESS CTRL+C TO SEAL.")
            while True:
                for msg in inport.iter_pending():
                    if msg.type in ['note_on', 'note_off']:
                        elapsed_seconds = time.perf_counter() - start_time
                        ticks = int(elapsed_seconds * (bpm / 60) * TICKS_PER_BEAT)
                        captured_events.append((msg, ticks))
                        print(f"[{ticks} ticks] {msg.note} | Velocity: {msg.velocity}")
                        
    except KeyboardInterrupt:
        print("\n--- PERFORMANCE SEALED ---")
        save_performance(captured_events, bpm)

def save_performance(events, bpm):
    mf = MIDIFile(1, removeDuplicates=True)
    mf.addTempo(0, 0, bpm)
    active_notes = {} # Format: {note: (start_tick, velocity)}
    
    for msg, ticks in events:
        if msg.type == 'note_on' and msg.velocity > 0:
            # Store BOTH the start time AND the velocity
            active_notes[msg.note] = (ticks, msg.velocity)
        elif msg.type == 'note_off' or (msg.type == 'note_on' and msg.velocity == 0):
            if msg.note in active_notes:
                start_tick, on_velocity = active_notes.pop(msg.note)
                duration = ticks - start_tick
                # Use the original ON_VELOCITY, not the zero velocity from Note Off
                mf.addNote(0, 0, msg.note, start_tick/TICKS_PER_BEAT, duration/TICKS_PER_BEAT, on_velocity)

    path = os.path.expanduser("~/Calendaw/data/Audio/Midi/Performance_Hindsight.mid")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as f:
        mf.writeFile(f)
    print(f"Sovereign MIDI artifact saved: {path}")

if __name__ == "__main__":
    record_performance()