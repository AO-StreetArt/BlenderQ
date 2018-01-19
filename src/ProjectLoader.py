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
Project Loader to read and write JSON
"""

import json
import logging

class ProjectLoader(object):
    def __init__(self):
        self._logger = logging.getLogger("blenderq")

    # Takes a list of dictionaries as input and writes them back to JSON file
    def writeProject(self, filename, filelist, hidden_ops):
        self._logger.info("Writing Project to file: %s" % filename)
        files_string = ''
        for elt in filelist:
            files_string += '{"filename": "%s", "ops": "%s"}, ' % (elt['filename'],
                                                                   elt['ops_box'].get())
        files_string = files_string[:-2]
        if hidden_ops is None:
            hidden_ops = ''
        json_string = '{"hidden_ops": "%s", "files": [%s]}' % (hidden_ops, files_string)
        with open(filename, 'w') as output_file:
            output_file.write(json_string)

    # Takes a list/tuple of filenames as input
    def loadProject(self, filename):
        self._logger.info("Loading Project from file: %s" % filename)
        return_map = None
        with open(filename, 'r') as json_file:
            return_map = json.load(json_file)
        return return_map
