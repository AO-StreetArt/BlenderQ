#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Simple UI to do queued Blender Renders
"""

from Tkinter import Tk

import logging

from src.BlenderQFrame import BlenderQFrame
from src.Renderer import BlenderRenderer
from src.Session import Session

def main():

    session = Session()
    renderer = BlenderRenderer(session['blender_location'])
    root = Tk()
    root.geometry("750x550+300+300")
    app = BlenderQFrame(renderer,
                        default_ops=session['default_ops'],
                        hidden_ops=session['hidden_ops'])
    root.mainloop()


if __name__ == '__main__':
    main()
