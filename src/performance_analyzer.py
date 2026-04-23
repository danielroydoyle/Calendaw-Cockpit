# # CALENDAW: SCRY MODULE (V1.0 - ATTRIBUTED)
# ## 🧬 PROVENANCE:
# ## Original Logic: Calendaw Internal (Collaborative Build)
# ## Inspiration/Math: Zrythm (src/dsp/snap_grid.h) for tick-mapping logic.
# ## #HTCP-Type: Analysis_Visualization
# ## #HTCP-Context: Post-performance scry of MIDI data against 960 PPQN grid.
# ## #HTCP-Purpose: Generate a "Manual Cleaning Roadmap" for the Google Pixel video sync.

import mido
import matplotlib.pyplot as plt
import os

def scry_performance(midi_filename="Performance_Hindsight.mid"):
    # Target the official data hangar
    midi_path = os.path.expanduser(f"~/Calendaw/data/Audio/Midi/{midi_filename}")
    output_image = os.path.expanduser("~/Calendaw/data/Visuals/performance_scry.png")
    
    # Ensure visuals directory exists
    os.makedirs(os.path.dirname(output_image), exist_ok=True)
    
    if not os.path.exists(midi_path):
        print(f"ERROR: Artifact not found at {midi_path}")
        return

    mid = mido.MidiFile(midi_path)
    tpb = mid.ticks_per_beat # Should be 960
    grid_16th = tpb // 4
    
    notes = []
    track_time = 0
    active_notes = {}

    for track in mid.tracks:
        for msg in track:
            track_time += msg.time
            if msg.type == 'note_on' and msg.velocity > 0:
                active_notes[msg.note] = track_time
            elif msg.type == 'note_off' or (msg.type == 'note_on' and msg.velocity == 0):
                if msg.note in active_notes:
                    start_tick = active_notes.pop(msg.note)
                    notes.append((msg.note, start_tick, track_time))

    if not notes:
        print("Scry Failed: No note data found in the artifact.")
        return

    # Create the Visual Roadmap
    plt.figure(figsize=(12, 6))
    for pitch, start, end in notes:
        plt.barh(pitch, end - start, left=start, color='steelblue', height=0.8)
        
        # Calculate Deviation for Manual Cleaning
        nearest_grid = round(start / grid_16th) * grid_16th
        deviation = start - nearest_grid
        if abs(deviation) > 10:
            plt.text(start, pitch + 0.3, f"{deviation:+}", fontsize=7, color='red')

    # Draw the Grid (The "Truth")
    max_tick = max(n[2] for n in notes)
    for x in range(0, max_tick + grid_16th, grid_16th):
        plt.axvline(x=x, color='gray', linewidth=0.5, alpha=0.5)

    plt.title(f"Performance Scry: {midi_filename} (960 PPQN)")
    plt.xlabel("Ticks")
    plt.ylabel("MIDI Pitch")
    plt.savefig(output_image)
    print(f"✅ Scry Complete. Roadmap saved to: {output_image}")

if __name__ == "__main__":
    scry_performance()