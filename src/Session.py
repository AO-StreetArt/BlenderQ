#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Session to hold configuration values
"""

import ConfigParser
import logging

class Session(object):
    def __init__(self):
        self.param_list = {}
        self.configure()

    def teardown(self):
        self.param_list.clear()

    def __len__(self):
        return len(self.param_list)

    def __getitem__(self, key):
        return self.param_list[key]

    def __setitem__(self, key, value):
        self.param_list[key] = value

    def __delitem__(self, key):
        del self.param_list[key]

    def __iter__(self):
        return self.param_list.__iter__()

    def configure(self):

        print("Pulling Core Config Data")

        # Read the config file, with a set of defaults
        config = ConfigParser.SafeConfigParser({
            'blender.default_ops': '--render-output //test_ --render-format PNG --render-frame 1',
            'blender.hidden_ops': '--engine CYCLES --use-extension 1',
            'logging.file': 'bq.log',
            'logging.level': 'Debug',
        })
        config.read('config.ini')

        # Parse the standard config variables out of the file
        self.param_list['blender_location'] = config.get('Blender', 'blender.location')
        self.param_list['default_ops'] = config.get('Blender', 'blender.default_ops')
        self.param_list['hidden_ops'] = config.get('Blender', 'blender.hidden_ops')
        self.param_list['log_file'] = config.get('Logging', 'logging.file')
        self.param_list['log_level'] = config.get('Logging', 'logging.level')

        #Set up the file logging config
        if self.param_list['log_level'] == 'Debug':
            logging.basicConfig(filename=self.param_list['log_file'], level=logging.DEBUG)
        elif self.param_list['log_level'] == 'Info':
            logging.basicConfig(filename=self.param_list['log_file'], level=logging.INFO)
        elif self.param_list['log_level'] == 'Warning':
            logging.basicConfig(filename=self.param_list['log_file'], level=logging.WARNING)
        elif self.param_list['log_level'] == 'Error':
            logging.basicConfig(filename=self.param_list['log_file'], level=logging.ERROR)
        else:
            print("Log level not set to one of the given options, defaulting to debug level")
        logging.basicConfig(filename=self.param_list['log_file'], level=logging.DEBUG)
