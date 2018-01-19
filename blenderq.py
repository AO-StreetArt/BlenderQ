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
