
import os


class Runner:
    def main(self):
        raise NotImplementedError('Main function is not implemented.')

    def on_exit(self):
        pass

    def on_entry(self):
        pass

    def on_signal(self, signal):
        raise SystemExit

    def _signal_handler(self, signal, frame):
        self.on_signal(signal)

    def run(self):
        self.on_entry()

        try:
            self.main()
        except (KeyboardInterrupt, SystemExit):
            pass
        finally:
            try:
                self.on_exit()
            except KeyboardInterrupt:
                print('Interrupted while exiting...')
                os._exit(0)
            except SystemExit:
                print('Double exiting request...')
                os._exit(0)
