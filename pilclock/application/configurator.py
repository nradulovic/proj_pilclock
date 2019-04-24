
import logging
import json

configurations = {}


class Configuration:
    def __init__(self, name, file, data):
        self.name = name
        self.file = file
        self.data = data
        self.template = None

    def set_template(self, template):
        self.template = template

    def get(self, key):
        try:
            return self.data[key]
        except KeyError:
            return self.template.data[key]


class Configurator:
    def __init__(self, name, file):
        self.name = name
        self.file = file

    def load(self):
        log = logging.getLogger(__name__)
        log.info('Loading configuration {}'.format(self.name))
        with open(self.file) as f:
            config = Configurator(self.name, self.file, json.load(f))
            configurations[self.name] = config
            return config
