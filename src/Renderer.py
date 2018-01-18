#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Renderer which actually calls blender to render files
"""

import logging

from subprocess import call

class BlenderRenderer(object):
    def __init__(self, blender_location):
        self._blender_location = blender_location

    def render_file(self, file_name, op_string):
        blender_command = 'cd ' + self._blender_location + ' && ./blender ' + op_string
        return call(blender_command, shell=True)
