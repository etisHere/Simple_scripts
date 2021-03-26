#!/usr/bin/env python3
import webbrowser

useri = input("What's the url?: ")
newurl = useri.replace("watch?v=", "embed/")
webbrowser.open(newurl)

#Paste script in with a alias in bash for quick access (i have it set to yte)
#et
