# Add this after you load the UI in cockpit_bootstrap.py
record_button = builder.get_object("trans_record")
if record_button:
    # We find the 'Image' inside the button and 'Dye' it manually
    child = record_button.get_child()
    if isinstance(child, Gtk.Image):
        # We set a CSS class specifically for this one widget 
        # that we know we can target with high priority.
        record_button.add_css_class("record-active")
        print("💉 SOVEREIGN OVERRIDE: Record button dyed in the marrow.")