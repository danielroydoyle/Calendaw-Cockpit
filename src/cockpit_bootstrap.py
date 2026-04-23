# # CALENDAW: COCKPIT BOOTSTRAP (V1.4)
# ## Location: Home/Calendaw/src

import sys
import os
import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw, Gio

class CalendawCockpit(Adw.Application):
    def __init__(self):
        super().__init__(application_id='com.calendaw.cockpit',
                         flags=Gio.ApplicationFlags.FLAGS_NONE)

    def do_activate(self):
        # 1. THE SKIN TRANSPLANT: Load and Apply CSS
        css_provider = Gtk.CssProvider()
        # Pointing to your specific cockpit.css artifact
        css_path = os.path.expanduser("~/Calendaw/resources/css/cockpit.css")
        
        if os.path.exists(css_path):
            css_provider.load_from_path(css_path)
            # This is the "Megaphone" that tells the display to use our CSS
            Gtk.StyleContext.add_provider_for_display(
                Gtk.Widget.get_display(Gtk.Box()), 
                css_provider,
                Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
            )
            print("🎨 CSS INJECTED: The Surgical Dye is in the system.")
        else:
            print(f"⚠️ CSS MISSING: Could not find {css_path}")

        # 2. THE BONES: Load UI
        builder = Gtk.Builder()
        try:
            builder.add_from_file("resources/ui/main_window.ui")
            builder.add_from_file("resources/ui/transport_controls.ui")
        except Exception as e:
            print(f"❌ SKELETON ERROR: {e}")
            return

        self.win = builder.get_object("MainWindowWidget")
        if not self.win:
            self.win = Adw.ApplicationWindow(application=self)
            self.win.set_title("Calendaw Cockpit (Cosmic Root)")
        
        self.win.set_application(self)
        self.win.present()

if __name__ == "__main__":
    app = CalendawCockpit()
    app.run(sys.argv)