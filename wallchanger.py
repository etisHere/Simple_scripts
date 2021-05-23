#!/usr/bin/env python3

from time import sleep
import os

def mai():
    pics = "~/Pictures/wp/*"
    mast = "feh --randomize --bg-fill "
    mastd = mast+pics
    os.system(mastd)
    ti =  sleep(120)
    mai()


mai()
