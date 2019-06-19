
import os
from .application import runner
from .application import logger
from .application import configurator
from . import identity
from time import sleep


class Main(runner.Runner):
    def on_entry(self):
        print('Starting {}...'.format(identity.NAME))
        print('Provided by {} ({})'.format(identity.PROVIDER,
              identity.DATE))

    def main(self):
        log = logger.setup(identity.ROOT)
        config_file = os.getenv('{}_CONFIG_FILE'.format(
                identity.NAME.upper()),
                'pilclock/application/default_config.py')
        log.info('Using "{}" configuration file'.format(config_file))
        try:
            configurator.Configurator(identity.NAME, config_file).load()
        except FileNotFoundError as e:
            log.warn('Failed to load configuration "{}" ({})'.format(
                    e.filename, e.strerror))
        while True:
            sleep(1)

    def on_exit(self):
        print('Exiting...')
