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
Renderer which actually calls blender to render files
"""

import logging

from subprocess import call, STDOUT

class BlenderRenderer(object):
    def __init__(self, blender_location):
        self._blender_location = blender_location
        self._logger = logging.getLogger("blenderq")

    def render_file(self, file_name, op_string):
        blender_command = '%s %s %s' % (self._blender_location, file_name, op_string)
        self._logger.info("Blender Command: %s" % blender_command)
        return call(blender_command, shell=True)
