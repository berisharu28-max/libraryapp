from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

KV = '''
ScreenManager:
    LoginScreen:
    DashboardScreen:

<LoginScreen>:
    name: 'login'
    canvas.before:
        Color:
            rgba: 0.06, 0.12, 0.21, 1
        Rectangle:
            pos: self.pos
            size: self.size

    BoxLayout:
        orientation: 'vertical'
        padding: 40
        spacing: 15
        size_hint_y: None
        height: self.minimum_height
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}

        Label:
            text: "LIBREMANX"
            font_size: '36sp'
            bold: True
            color: 1, 1, 1, 1

        Label:
            text: "Library Management System"
            font_size: '16sp'
            color: 0.7, 0.7, 0.7, 1

        Widget:
            size_hint_y: None
            height: 10

        TextInput:
            hint_text: "Username"
            multiline: False
            size_hint_y: None
            height: 48
            background_color: 0.1, 0.18, 0.3, 1
            foreground_color: 1, 1, 1, 1
            cursor_color: 1, 1, 1, 1

        TextInput:
            hint_text: "Password"
            password: True
            multiline: False
            size_hint_y: None
            height: 48
            background_color: 0.1, 0.18, 0.3, 1
            foreground_color: 1, 1, 1, 1
            cursor_color: 1, 1, 1, 1

        Widget:
            size_hint_y: None
            height: 10

        Button:
            text: "LOGIN"
            bold: True
            font_size: '16sp'
            size_hint_y: None
            height: 50
            background_normal: ''
            background_color: 0.15, 0.27, 0.44, 1
            on_release: root.manager.current = 'dashboard'

<DashboardScreen>:
    name: 'dashboard'
    canvas.before:
        Color:
            rgba: 0.06, 0.12, 0.21, 1
        Rectangle:
            pos: self.pos
            size: self.size

    BoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 15

        # Header Title
        Label:
            text: "Dashboard"
            font_size: '24sp'
            bold: True
            size_hint_y: None
            height: 40
            halign: 'left'
            valign: 'middle'
            text_size: self.size

        # Stats Grid
        GridLayout:
            cols: 3
            spacing: 10
            size_hint_y: None
            height: 80

            BoxLayout:
                orientation: 'vertical'
                canvas.before:
                    Color:
                        rgba: 0.15, 0.27, 0.44, 1
                    Rectangle:
                        pos: self.pos
                        size: self.size
                Label:
                    text: "1,245"
                    bold: True
                    font_size: '18sp'
                Label:
                    text: "Total"
                    font_size: '12sp'
                    color: 0.8, 0.8, 0.8, 1

            BoxLayout:
                orientation: 'vertical'
                canvas.before:
                    Color:
                        rgba: 0.17, 0.61, 0.34, 1
                    Rectangle:
                        pos: self.pos
                        size: self.size
                Label:
                    text: "112"
                    bold: True
                    font_size: '18sp'
                Label:
                    text: "Issued"
                    font_size: '12sp'
                    color: 0.9, 0.9, 0.9, 1

            BoxLayout:
                orientation: 'vertical'
                canvas.before:
                    Color:
                        rgba: 0.84, 0.44, 0.17, 1
                    Rectangle:
                        pos: self.pos
                        size: self.size
                Label:
                    text: "1,133"
                    bold: True
                    font_size: '18sp'
                Label:
                    text: "Available"
                    font_size: '12sp'
                    color: 0.9, 0.9, 0.9, 1

        Widget:
            size_hint_y: None
            height: 10

        # Action Menu Buttons
        ScrollView:
            BoxLayout:
                orientation: 'vertical'
                spacing: 12
                size_hint_y: None
                height: self.minimum_height

                Button:
                    text: "Books Management"
                    background_normal: ''
                    background_color: 0.1, 0.18, 0.3, 1
                    size_hint_y: None
                    height: 50
                    font_size: '15sp'

                Button:
                    text: "Issue Book"
                    background_normal: ''
                    background_color: 0.1, 0.18, 0.3, 1
                    size_hint_y: None
                    height: 50
                    font_size: '15sp'

                Button:
                    text: "Issued Books"
                    background_normal: ''
                    background_color: 0.1, 0.18, 0.3, 1
                    size_hint_y: None
                    height: 50
                    font_size: '15sp'

                Button:
                    text: "Logout"
                    background_normal: ''
                    background_color: 0.58, 0.22, 0.22, 1
                    size_hint_y: None
                    height: 50
                    font_size: '15sp'
                    bold: True
                    on_release: root.manager.current = 'login'
'''

class LoginScreen(Screen):
    pass

class DashboardScreen(Screen):
    pass

class LibraryApp(App):
    def build(self):
        return Builder.load_string(KV)

if __name__ == '__main__':
    LibraryApp().run()
