# class Vi:
class Vi(object):
    def __init__(self, keymap):
        self.keymap = keymap
        self.emacs = keymap.defineWindowKeymap()
        self.emacs.is_marked = False

    def delete_char(self):
        self.keymap.InputKeyCommand('Delete')()

    def kill_word(self, repeat=1):
        self.emacs.is_marked = True

        def move_end_of_region():
            for i in range(repeat):
                self.forward_word()

        self.mark(move_end_of_region)()
        self.delay(self.kill_region)()

    def kill_region(self):
        self.keymap.InputKeyCommand("C-x")()

    def mark(self, func):
        def _func():
            if self.emacs.is_marked:
                # D-Shift だと、M-< や M-> 押下時に、D-Shift が解除されてしまう。その対策。
                self.keymap.InputKeyCommand("D-LShift", "D-RShift")()
                self.delay(func)()
                self.keymap.InputKeyCommand("U-LShift", "U-RShift")()
            else:
                func()

        return _func

    def delay(self, func, sec=0.01):
        def _func():
            time.sleep(sec)  # delay
            func()
            time.sleep(sec)  # delay

        return _func

    def forward_word(self):
        self.keymap.InputKeyCommand("C-Right")()
