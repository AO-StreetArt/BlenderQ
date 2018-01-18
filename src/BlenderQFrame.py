#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Simple UI to do queued Blender Renders
"""

from Tkinter import LEFT, RIGHT, BOTH, RAISED, Text, X, N
from ttk import Frame, Button, Style, Label, Entry

import tkFileDialog

import logging

import ntpath

def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

class BlenderQFrame(Frame):

    def __init__(self, renderer, default_ops=None, hidden_ops=None):
        # Renderer
        self._renderer = renderer
        # Default Options
        self._default_ops = default_ops
        # Hidden Options
        self._hidden_ops = hidden_ops
        # Internal list of filenames
        self._files = []
        # File frame that needs to be dynamically updated
        self._file_frame = None
        # Call the parent constructor
        Frame.__init__(self)
        # Initialize the UI
        self.initUI()

    def renderFiles(self):
        logging.info("Render Called")
        for elt in self._files:
            logging.debug("File: %s" % elt['filename'])
            logging.debug("Ops: %s" % elt['ops_box'].get())
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

            lbl = Label(inner_frame, text=path_leaf(elt), width=18)
            lbl.pack(side=LEFT, padx=5, pady=5)

            entry = Entry(inner_frame)
            entry.pack(fill=X, padx=5, expand=True)
            if self._default_ops is not None:
                entry.insert(0, self._default_ops)

            file_dict = {"filename": elt, "ops_box": entry, "file_label": lbl}
            self._files.append(elt)

    def initUI(self):
        # Window title and style
        self.master.title("BlenderQ")
        self.style = Style()
        self.style.theme_use("default")

        # Master frame which contains the others
        master_frame = Frame(self)
        master_frame.pack(fill=X)

        # Title Labels
        lbl1 = Label(master_frame, text="File", width=6)
        lbl1.pack(side=LEFT, padx=5, pady=5)

        lbl2 = Label(master_frame, text="Options", width=6)
        lbl2.pack(side=RIGHT, padx=5, pady=5)

        # Create the file list frame, but don't populate anything
        list_frame = Frame(self)
        list_frame.pack(fill=BOTH, expand=True)
        self._file_frame = list_frame

        # Frame for showing buttons
        button_frame = Frame(self, relief=RAISED, borderwidth=1)
        button_frame.pack(fill=X, expand=True)

        self.pack(fill=BOTH, expand=True)

        openButton = Button(self, text="Open", command=self.findFiles)
        openButton.pack(side=LEFT, padx=5, pady=5)
        runButton = Button(self, text="Run", command=self.renderFiles)
        runButton.pack(side=RIGHT)
