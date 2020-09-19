from pynput import keyboard

class MyListener(keyboard.Listener):
    def _init_(self):
        super(MyListener, self)._init_(self.on_press, self.on_release)
        self.key_pressed = None

    def on_press(self, key):
        self.key_pressed = key

    def on_release(self,key):
        self.key_pressed = None
