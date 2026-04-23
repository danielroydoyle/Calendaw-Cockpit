# # CALENDAW: INTERFACE MODULE (V1.1 - ATTRIBUTED)
# ## 🧬 PROVENANCE:
# ## Original Layout Concepts: Zrythm (src/gui/backend/gtk_widgets)
# ## SPDX-FileCopyrightText: © 2018-2025 Alexandros Theodotou <alex@zrythm.org>
# ## SPDX-License-Identifier: LicenseRef-ZrythmLicense
#
# ## #HTCP-Type: Graphical_User_Interface
# ## #HTCP-Context: GTK4 bridge for performance initialization.
# ## #HTCP-Purpose: Low-entropy, high-contrast cockpit for performance capture.

import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk, GLib
import os
import subprocess

class CalendawWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_title("CALENDAW: PERFORMANCE COCKPIT")
        self.set_default_size(800, 600)

        # High-contrast vertical layout
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        self.box.set_valign(Gtk.Align.CENTER)
        self.box.set_halign(Gtk.Align.CENTER)
        self.set_child(self.box)

        # Tactical Record Button
        self.button = Gtk.Button(label="⭕ START PERFORMANCE")
        self.button.set_size_request(200, 100)
        self.button.connect('clicked', self.on_record_clicked)
        self.box.append(self.button)

    def on_record_clicked(self, button):
        print("Initializing High-Precision Capture...")
        button.set_label("⏺️ RECORDING ACTIVE")
        button.set_sensitive(False)
        
        # Deploy the attributed recorder
        subprocess.Popen(["python3", os.path.expanduser("~/Calendaw/src/recorder.py")])

class CalendawApp(Gtk.Application):
    def __init__(self):
        super().__init__(application_id='com.calendaw.cockpit')
    def do_activate(self):
        win = CalendawWindow(application=self)
        win.present()

if __name__ == "__main__":
    app = CalendawApp()
    app.run(None)