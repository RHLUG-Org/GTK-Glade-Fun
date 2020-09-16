# (c) 2020 siliconninja.
# Licensed under the MIT License.

# I'd recommend installing GTK Glade first and open up "gtk interface.glade"
# to see what it looks like. It's sort of intuitive to play around with,
# looking up some tutorials or documentation (especially:
# https://python-gtk-3-tutorial.readthedocs.io/en/latest/introduction.html and
# for centering things, https://developer.gnome.org/gtk3/stable/ch30s02.html and
# for text views, https://python-gtk-3-tutorial.readthedocs.io/en/latest/textview.html) may help you.
# This uses the PyGTK library which contains Python bindings for a GTK application
# (so you can use the GTK UI toolkit, but in the Python programming languages!).
# It can make it easier to start with than a C program. A C program may be better
# later on, if you need more performance, though.

# These next 3 lines import the necessary libraries for the GTK UI toolkit to run.
# You need to include them if you're writing a simple GTK app like this one.
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

# it's often better to generalize things if you have many buttons,
# like in this function \/
def on_button_clicked(button_name):
    # f-strings are very flexible for formatting.
	print(f'You clicked {button_name}')
	# You could also do something in the application to show the user, like
	# (uncomment the line below (remove the #) and run using python app.py to try it out!):
	#textbox.get_buffer().set_text('Good job! :)')

#def on_button1_clicked():
#

# This constructs a Builder object.
builder = Gtk.Builder()
# Loads all the UI objects (windows, buttons, etc.) in the file we created from GTK Glade
builder.add_from_file('gtk interface.glade')

# It is useful to give components an ID in GTK Glade to access them like this.
# The ID of the window in GTK Glade is window1.
win = builder.get_object('window1')

# Similarly, the ID of the button I created is called button1.
button1 = builder.get_object('button1')
# This "registers" a signal, so that when a button is clicked, it calls a specific function. Here, we pass it the argument 'button1' (which is a string).
# Check your terminal after you run the program with python app.py to see some text appear!
# This lambda is used as an anonymous function here.
button1.connect('clicked', lambda x: on_button_clicked('button1'))

# Each text box has a "text buffer" which basically holds the text that
# it is displaying. You can change the text simply using get_text() on
# the text buffer.
textbox = builder.get_object('textbox1')
textbox.get_buffer().set_text('Linux Users Group is awesome!')

# This avoids you from having to press ctrl+c in the terminal to quit the app.
win.connect("destroy", Gtk.main_quit)
win.show_all()

# This runs the main application.
Gtk.main()
