from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.config import Config
from kivy.core.audio import SoundLoader
from datetime import timedelta, datetime
import time
from kivy.uix.popup import Popup
from kivy.uix.label import Label
import math
Config.set('graphics', 'resizable', True)
kv = """
Screen:
    canvas.before:
        Color:
            rgba: 0, 3, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size
    MDLabel:
        text: 'Sanitizer Alarm'
        pos_hint: {'center_x': 0.75, 'center_y': 0.95}
        bold:True
        italic:True
        font_style: 'H5'
    MDLabel:
        text: "Please type in the frequency you want the alarm to ring in minutes."
        pos_hint: {'center_x': 0.5, 'center_y': 0.75}
        bold:False
    MDLabel:
        text: "Please type the ending hour and minute in the end hour and end minute(24 hour format used)."
        pos_hint: {'center_x': 0.5, 'center_y': 0.85}
        bold:False
    MDRaisedButton:
        text: 'Start'
        pos_hint: {'center_x': 0.5, 'center_y': 0.25}
        size_hint_x: None
        on_press:
            app.onButtonPress()
    MDTextField:
        id: frequency
        hint_text: 'Alarm Frequency'
        bold:True
        helper_text_mode: "on_focus" 
        pos_hint: {'center_x': 0.5, 'center_y': 0.35}
        size_hint_x: None
        width: 320
        required: True
    MDTextField:
        id: minute
        hint_text: 'End Minute'
        bold:True
        helper_text_mode: "on_focus" 
        pos_hint: {'center_x': 0.5, 'center_y': 0.45}
        size_hint_x: None
        width: 300
        required: True
    MDTextField:
        id: hour
        hint_text: 'End Hour'
        bold:True
        helper_text_mode: "on_focus" 
        pos_hint: {'center_x': 0.5, 'center_y': 0.55}
        size_hint_x: None
        width: 300
        required: True
"""
sound = SoundLoader.load('bye.wav')
sound1 = SoundLoader.load('pls_use_sanitizer.wav')
class Main(MDApp):
    def alarm(self, frequency, end_time):
        now1 = datetime.now()
        def __datetime(date_str):
            return datetime.strptime(date_str, '%H:%M:%S')
        start = now1
        end = __datetime(end_time)
        start1 = str(start)
        delta = end - start
        seconds = delta.seconds
        hours = seconds // 3600
        minutes = (seconds // 60) % 60
        main = f'{hours}:{minutes}'
        main2 = datetime.strptime(main, '%H:%M')
        minutes2 = hours * 60
        minutes3 = minutes2 + minutes
        mnia = minutes3 / frequency
        mnia2 = math.modf(mnia)
        mnia3 = int(mnia2[1])
        x1 = 0
        print(end_time)
        for x in range(0, mnia3):
            time.sleep(1)
            x1 += frequency
            start2 = start + timedelta(minutes=x1)
            now_plus = format(start2, "%H:%M:%S")
            while True:
                time.sleep(1)
                current_time = datetime.now()
                now = current_time.strftime("%H:%M:%S")
                if now == now_plus:
                    sound1.play()
                    break
        end_1 = end + timedelta(minutes=1)
        print(end_1)
        while True:
            time.sleep(1)
            current_time = datetime.now()
            now = current_time.strftime("%H:%M:%S")
            end_2 = end_1 .strftime("%H:%M:%S")
            if now == end_2:
                sound.play()
                break
    def onButtonPress(self):
        label = Label(text='Alarm Started !!')
        popup = Popup(title='Alarm Started !!',content=label,size_hint=(None, None), size=(600, 600))
        popup.bind(on_dismiss=self.actual_time)
        popup.open()
    def actual_time(self,instance=0):
        hour = self.root.ids.hour.text
        minute = self.root.ids.minute.text
        end_time = (f'{hour}:{minute}:00')
        frequency = int(self.root.ids.frequency.text)
        self.alarm(frequency,end_time)
    def build(self):
        return Builder.load_string(kv)
Main().run()
