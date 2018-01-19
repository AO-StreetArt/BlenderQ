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

from Tkinter import LEFT, RIGHT, BOTH, RAISED, Text, X, N, PhotoImage, Menu
from ttk import Frame, Button, Style, Label, Entry

import tkFileDialog

import logging

import ntpath

def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

class BlenderQFrame(Frame):

    def __init__(self, renderer, loader, default_ops=None, hidden_ops=None):
        # Renderer
        self._renderer = renderer
        # Loader
        self._loader = loader
        # Default Options
        self._default_ops = default_ops
        # Hidden Options
        self._hidden_ops = hidden_ops
        # Internal list of filenames
        self._files = []
        # frame that need to be dynamically updated
        self._file_frame = None
        self._button_frame = None
        self._props_frame = None
        self._hidden_ops_entry = None
        # Icons so they don't get garbage collected
        self.runIcon = None
        self.openIcon = None
        # Call the parent constructor
        Frame.__init__(self)
        # Initialize the UI
        self.initUI()

    def newProject(self):
        logging.info("New Project Called")

        # Clear the internal file list
        self._files = []

        # Destroy the frames
        self._file_frame.destroy()
        self._button_frame.destroy()

        # Re-Create the file list frame, but don't populate anything
        self.genFileListFrame()

        # Re-Build the buttons frame
        self.genButtons()

    def loadProject(self):
        logging.info("Load Project Called")
        # Find filenames of projects to load
        file_name = tkFileDialog.askopenfilename(parent=self,
                                                   title='Choose Project File')
        logging.debug(file_name)
        project_map = self._loader.loadProject(file_name)
        file_tuple = project_map['files']
        self._hidden_ops = project_map['hidden_ops']
        # Update the file list with the new files
        self.newProject()
        for elt in file_tuple:
            inner_frame = Frame(self._file_frame)
            inner_frame.pack(fill=X, expand=True)

            lbl = Label(inner_frame, text=path_leaf(elt['filename']), width=24)
            lbl.pack(side=LEFT, padx=5, pady=5)

            entry = Entry(inner_frame)
            entry.pack(fill=X, padx=5, expand=True)
            entry.insert(0, elt['ops'])

            file_dict = {"filename": elt, "ops_box": entry, "file_label": lbl}
            self._files.append(elt)

    def saveProject(self):
        logging.info("Save Project Called")
        file_name = tkFileDialog.asksaveasfilename(parent=self,
                                                   title='Choose Project File Name')
        logging.debug(self._files)
        self._loader.writeProject(file_name, self._files, self._hidden_ops_entry.get())

    def renderFiles(self):
        logging.info("Render Called")
        for elt in self._files:
            logging.debug("File: %s" % elt['filename'])
            logging.debug("Ops: %s" % elt['ops_box'].get())
            self._hidden_ops = self._hidden_ops_entry.get()
            return_code = self._renderer.render_file(elt,
                                                     '%s %s' % (elt['ops_box'].get(),
                                                                self._hidden_ops))
            if return_code != 0:
                logging.error("Error encountered in Render: %s" % elt['filename'])
                elt['file_label'].config(activeforeground="red")
            else:
                elt['file_label'].config(activeforeground="green")

    def findFiles(self):
        logging.info("Find Files Called")
        file_tuple = tkFileDialog.askopenfilenames(parent=self,
                                                   title='Choose Blender Files',
                                                   filetypes = (("blend files","*.blend"),
                                                                ("all files","*.*")))
        logging.debug(file_tuple)
        for elt in file_tuple:
            inner_frame = Frame(self._file_frame)
            inner_frame.pack(fill=X, expand=True)

            lbl = Label(inner_frame, text=path_leaf(elt), width=24)
            lbl.pack(side=LEFT, padx=5, pady=5)

            entry = Entry(inner_frame)
            entry.pack(fill=X, padx=5, expand=True)
            if self._default_ops is not None:
                entry.insert(0, self._default_ops)

            file_dict = {"filename": elt, "ops_box": entry, "file_label": lbl}
            self._files.append(file_dict)

    def genHeaders(self):
        # Header frame
        master_frame = Frame(self)
        master_frame.pack(fill=X)

        # Title Labels
        lbl1 = Label(master_frame, text="Blender File", width=18)
        lbl1.pack(side=LEFT, padx=10, pady=5)

        lbl2 = Label(master_frame, text="Render Options", width=12)
        lbl2.pack(side=RIGHT, padx=10, pady=5)

    def genFileListFrame(self):
        # Create the file list frame, but don't populate anything
        list_frame = Frame(self)
        list_frame.pack(fill=BOTH, expand=True)
        self._file_frame = list_frame

    def genFileList(self):
        for elt in self._files:
            inner_frame = Frame(self._file_frame)
            inner_frame.pack(fill=X, expand=True)

            lbl = Label(inner_frame, text=path_leaf(elt['filename']), width=18)
            lbl.pack(side=LEFT, padx=5, pady=5)

            entry = Entry(inner_frame)
            entry.pack(fill=X, padx=5, expand=True)
            if self._default_ops is not None:
                entry.insert(0, self._default_ops)

    def genButtons(self):
        # Frame for showing buttons
        self._button_frame = Frame(self, relief=RAISED, borderwidth=1)
        self._button_frame.pack(fill=X, expand=True)

        self.pack(fill=BOTH, expand=True)
        self.runIcon = PhotoImage(file="icons/run.png")
        runButton = Button(self._button_frame, image=self.runIcon, command=self.renderFiles)
        runButton.pack(side=RIGHT, padx=5, pady=5)
        self.openIcon = PhotoImage(file="icons/open.png")
        openButton = Button(self._button_frame, image=self.openIcon, command=self.findFiles)
        openButton.pack(side=RIGHT, padx=5, pady=5)

    def genPropsPanel(self):
        # Header frame
        self._props_frame = Frame(self)
        self._props_frame.pack(fill=X)

        # Title Labels
        lbl1 = Label(self._props_frame, text="Global Ops", width=18)
        lbl1.pack(side=LEFT, padx=10, pady=5)

        self._hidden_ops_entry = Entry(self._props_frame)
        self._hidden_ops_entry.pack(fill=X, padx=5, expand=True)
        if self._default_ops is not None:
            self._hidden_ops_entry.insert(0, self._hidden_ops)

    def initUI(self):
        # Window title and style
        self.master.title("BlenderQ")
        self.style = Style()
        self.style.theme_use("default")

        # Setup the Menu
        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label="New", command=self.newProject)
        fileMenu.add_command(label="Save", command=self.saveProject)
        fileMenu.add_command(label="Load", command=self.loadProject)
        fileMenu.add_command(label="Exit", command=self.onExit)
        menubar.add_cascade(label="Project", menu=fileMenu)

        self.genPropsPanel()
        # Build the header frame
        self.genHeaders()

        # Create the file list frame, but don't populate anything
        self.genFileListFrame()

        # Build the buttons frame
        self.genButtons()

    def onExit(self):
        self.quit()
