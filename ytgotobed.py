#!/usr/bin/env python3
import webbrowser

useri = input("What's the url?: ")
newurl = useri.replace("watch?v=", "embed/")
webbrowser.open(newurl)
