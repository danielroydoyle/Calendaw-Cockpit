import sys
import os
import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw, Gio

class CockpitApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(application_id='org.calendaw.cockpit', **kwargs)

    def do_activate(self):
        # 0. PATH-AGNOSTIC NAVIGATION
        # This prevents the "NoneType" error by always finding the root folder
        script_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(script_dir)
        ui_path = os.path.join(project_root, "resources", "ui", "cockpit.ui")
        css_path = os.path.join(project_root, "resources", "css", "cockpit.css")

        # 1. BUILD THE UI (The Bones)
        builder = Gtk.Builder()
        builder.add_from_file(ui_path)
        
        # 2. LOAD THE SKIN (The CSS)
        css_provider = Gtk.CssProvider()
        # We use a try-except block just in case the CSS file is empty or missing
        try:
            css_provider.load_from_path(css_path)
            Gtk.StyleContext.add_provider_for_display(
                Gtk.Widget.get_display(Gtk.Box()),
                css_provider,
                Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
            )
        except Exception as e:
            print(f"⚠️ SKIN WARNING: {e}")

        # 3. THE SOVEREIGN OVERRIDE (Inside the correct room)
        record_button = builder.get_object("trans_record")
        if record_button:
            record_button.add_css_class("record-active")
            print("💉 SOVEREIGN OVERRIDE: Record button dyed in the marrow.")

        # 4. MANIFEST THE WINDOW
        self.window = builder.get_object("cockpit_window")
        self.window.set_application(self)
        self.window.present()

if __name__ == '__main__':
    app = CockpitApp()
    sys.exit(app.run(sys.argv))