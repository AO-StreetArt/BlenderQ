#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Apache2 License Notice
Copyright 2018 Alex Barry

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

"""
Simple UI to do queued Blender Renders
"""

from Tkinter import Tk

import logging

from src.BlenderQFrame import BlenderQFrame
from src.ProjectLoader import ProjectLoader
from src.Renderer import BlenderRenderer
from src.Session import Session

def main():

    session = Session()
    #Set up the logging config
    logger = logging.getLogger("blenderq")

    # create logging handlers
    handler = logging.FileHandler(session['log_file'])
    ch = logging.StreamHandler()

    # create a logging format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    ch.setFormatter(formatter)

    # add the handlers to the logger
    logger.addHandler(handler)
    logger.addHandler(ch)

    if session['log_level'] == 'Debug':
        logger.setLevel(logging.DEBUG)
        handler.setLevel(logging.DEBUG)
        ch.setLevel(logging.DEBUG)
    elif session['log_level'] == 'Info':
        logger.setLevel(logging.INFO)
        handler.setLevel(logging.INFO)
        ch.setLevel(logging.INFO)
    elif session['log_level'] == 'Warning':
        logger.setLevel(logging.WARNING)
        handler.setLevel(logging.WARNING)
        ch.setLevel(logging.WARNING)
    elif session['log_level'] == 'Error':
        logger.setLevel(logging.ERROR)
        handler.setLevel(logging.ERROR)
        ch.setLevel(logging.ERROR)
    else:
        print("Log level not set to one of the given options, defaulting to debug level")
        logger.setLevel(logging.DEBUG)
        handler.setLevel(logging.DEBUG)
        ch.setLevel(logging.DEBUG)

    # Start the main app
    renderer = BlenderRenderer(session['blender_location'])
    loader = ProjectLoader()
    root = Tk()
    root.geometry("750x550+300+300")
    app = BlenderQFrame(renderer, loader,
                        default_ops=session['default_ops'],
                        hidden_ops=session['hidden_ops'])
    root.mainloop()


if __name__ == '__main__':
    main()
