
import sys
from builtins import NotImplementedError


class Runner:
    def main(self):
        raise NotImplementedError('Main function is not defined')

    def run(self):
        sys.exit(self.main())
