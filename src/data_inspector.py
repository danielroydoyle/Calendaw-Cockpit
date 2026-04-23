# # CALENDAW: XRAY MODULE (V2.1 - TRUE SNIPER)
# ## 👁️ SYSTEM LOGIC: DATA & CONTENT RETRIEVAL
# This version ignores partial matches when extracting file content.

import os
import sys

def search_and_inject(query, target_root=None):
    if target_root is None:
        target_root = os.path.expanduser("~/Calendaw/data")
    else:
        target_root = os.path.abspath(os.path.expanduser(target_root))

    print(f"Scanning Target: {target_root} for pattern: '{query}'...")
    
    results = []
    file_content = ""
    
    for root, dirs, files in os.walk(target_root):
        for file in files:
            # 1. Map all partial matches (the 'Continent')
            if query.lower() in file.lower():
                results.append(os.path.join(root, file))
            
            # 2. Extract content ONLY for the exact match (the 'City')
            if file.lower() == query.lower():
                try:
                    with open(os.path.join(root, file), 'r') as f:
                        file_content = f.read()
                except Exception as e:
                    file_content = f"[ERROR: {str(e)}]"

    # --- THE SINK LOGIC ---
    sink_path = os.path.expanduser("~/Calendaw/bridge/Scripts/Data.gs")
    with open(sink_path, "w") as f:
        f.write("// CALENDAW DYNAMIC CARGO (SNIPER MODE)\n")
        f.write(f"const XRAY_QUERY = '{query}';\n")
        f.write("const XRAY_RESULTS = [\n")
        for res in results:
            f.write(f"  '{res}',\n")
        f.write("];\n\n")
        
        f.write("const XRAY_CONTENT = `\n")
        # Sanitize for Javascript template literal
        f.write(file_content.replace('`', '\\`').replace('${', '\\${'))
        f.write("\n`;\n")
        
    print(f"Injected {len(results)} paths and {len(file_content)} chars into Data.gs")

if __name__ == "__main__":
    pattern = sys.argv[1] if len(sys.argv) > 1 else ""
    custom_path = sys.argv[2] if len(sys.argv) > 2 else None
    search_and_inject(pattern, custom_path)