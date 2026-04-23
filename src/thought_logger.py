# # CALENDAW: BUFFER MODULE
# ## 👁️ SYSTEM LOGIC: TEXT INGESTION
# This module captures active thoughts and serializes them into the data root.

import os
from datetime import datetime

def save_thought(text):
    # Expert Term: Serialization (saving data to a format for storage)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    filename = f"Thought_{timestamp}.txt"
    directory = os.path.expanduser("~/Calendaw/data/Text")
    
    if not os.path.exists(directory):
        os.makedirs(directory)
        
    path = os.path.join(directory, filename)
    
    with open(path, "w") as f:
        f.write(f"--- HINDSIGHT LOG: {timestamp} ---\n")
        f.write(text)
    
    print(f"Thought successfully serialized to: {path}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        # Join all arguments into a single string of text
        save_thought(" ".join(sys.argv[1:]))
    else:
        print("Buffer requires text input.")