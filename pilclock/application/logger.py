
import logging


def setup(name=None):
    logger = logging.getLogger(name)
    formatter = logging.Formatter(
            '%(asctime)s %(name)s %(levelname)s: %(message)s')

    _handler = logging.StreamHandler()
    _handler.setFormatter(formatter)

    logger.addHandler(_handler)
    logger.setLevel(logging.INFO)

    return logger


def reconfigure(config):
    pass
