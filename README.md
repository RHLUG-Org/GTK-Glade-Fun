# GTK-Glade-Fun
An awesome application using GTK Glade made for the Fall 2020 Installfest!

Coding an app in GTK is intuitive if you've worked with any Python before. Nonetheless, no experience is required to understand what this code does, because I've included a guide for understanding the code in the README, and I've included helpful comments in `app.py` which is the main piece of code that runs the app.

GTK Glade works in a similar way to Windows Forms, but WxWidgets and Tk may be good to look into as well. GTK is more "native" though and so I wanted to try it out.

## How to run
In a Linux terminal with GTK 3, Python 3, and PyGTK3 installed (most distros like Ubuntu and Fedora and desktops like KDE, GNOME, etc. have these already installed), type:

```shell
python app.py
```

## How to understand the code
Open up `gtk interface.glade` in GTK Glade. You can install it with your distro's package manager, like apt-get or pacman.

You should see a small button with text in the center. You will see a blank space on the right side of the window for the text box. I haven't yet figured out a way for Glade to change the default text or show the whole thing. I need to look at more tutorials with text boxes to confirm that this is or isn't possible.

The UI code is in `app.py`. That contains the dynamic logic, like what to do when a button is clicked. GTK Glade only lets you focus on what the UI layout looks like, and not as much of the code itself (though it will let you register signal handlers which are basically the "on clicked", etc. events).

These are some good documentation links I found that will help you learn GTK:
https://python-gtk-3-tutorial.readthedocs.io/en/latest/introduction.html

https://developer.gnome.org/gtk3/stable/ch30s02.html (the diagram is especially useful here. If you don't want your button covering the entire window and rather be in the center, remember to set the "Align" options to be "center", not "fill".)

https://python-gtk-3-tutorial.readthedocs.io/en/latest/textview.html
