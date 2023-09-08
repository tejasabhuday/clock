import time
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.label import Label  # Corrected import statement
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout

Window.size = (400, 700)

class MyClock(Label):  # Class names should start with a capital letter
    def update(self, *args):
        t = time.gmtime()
        self.text = time.asctime(t)

class TimeApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        clock1 = MyClock()  # Updated class name
        Clock.schedule_interval(clock1.update, 1)
        layout.add_widget(clock1)
        layout.add_widget(Label(text='INDIA')) 

        clock2 = MyClock()  # Updated class name
        Clock.schedule_interval(clock2.update, 1)
        layout.add_widget(clock2)
        layout.add_widget(Label(text='LONDON'))  

        return layout

if __name__ == '__main__':
    root = TimeApp()
    root.run()
