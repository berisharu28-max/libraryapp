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
        padding: [30, 30, 30, 30]
        spacing: 20
        size_hint_y: None
        height: self.minimum_height
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}

        Label:
            text: "LIBREMANX"
            font_size: '32sp'
            bold: True

        Label:
            text: "Library Management System"
            font_size: '14sp'
            color: [0.6, 0.6, 0.6, 1]

        TextInput:
            id: username_input
            hint_text: "Username"
            multiline: False
            size_hint_y: None
            height: 45
            background_color: [0.1, 0.18, 0.3, 1]
            foreground_color: [1, 1, 1, 1]

        TextInput:
            id: password_input
            hint_text: "Password"
            password: True
            multiline: False
            size_hint_y: None
            height: 45
            background_color: [0.1, 0.18, 0.3, 1]
            foreground_color: [1, 1, 1, 1]

        Button:
            text: "LOGIN"
            bold: True
            font_size: '16sp'
            size_hint_y: None
            height: 50
            background_normal: ''
            background_color: [0.15, 0.27, 0.44, 1]
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
        padding: [15, 15, 15, 15]
        spacing: 15

        # Top Profile Bar
        BoxLayout:
            orientation: 'horizontal'
            size_hint_y: None
            height: 50
            Label:
                text: "LIBREMANX"
                font_size: '22sp'
                bold: True
                halign: 'left'
                valign: 'middle'
                text_size: self.size
            Label:
                text: "Profile"
                font_size: '14sp'
                size_hint_x: None
                width: 60
                valign: 'middle'
                text_size: self.size
            Label:
                text: "Alerts"
                font_size: '14sp'
                size_hint_x: None
                width: 60
                valign: 'middle'
                text_size: self.size

        # Dashboard Title
        Label:
            text: "DASHBOARD"
            font_size: '18sp'
            bold: True
            size_hint_y: None
            height: 25
            halign: 'left'
            valign: 'middle'
            text_size: self.size

        # Search Bar
        TextInput:
            hint_text: "Search books..."
            multiline: False
            size_hint_y: None
            height: 40
            background_color: [0.1, 0.18, 0.3, 1]
            foreground_color: [1, 1, 1, 1]

        # Stats Grid (3 Boxes)
        GridLayout:
            cols: 3
            spacing: 10
            size_hint_y: None
            height: 100

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
                    text: "Total Books"
                    font_size: '12sp'
                    color: [0.8, 0.8, 0.8, 1]

            BoxLayout:
                orientation: 'vertical'
                canvas.before:
                    Color:
                        rgba: 0.15, 0.27, 0.44, 1
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
                    color: [0.8, 0.8, 0.8, 1]

            BoxLayout:
                orientation: 'vertical'
                canvas.before:
                    Color:
                        rgba: 0.15, 0.27, 0.44, 1
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
                    color: [0.8, 0.8, 0.8, 1]

        # Menu Buttons List
        ScrollView:
            BoxLayout:
                orientation: 'vertical'
                spacing: 10
                size_hint_y: None
                height: self.minimum_height

                Button:
                    text: "Books Management"
                    background_normal: ''
                    background_color: [0.1, 0.18, 0.3, 1]
                    size_hint_y: None
                    height: 45
                    halign: 'left'
                    valign: 'middle'
                    text_size: self.size
                    padding: [15, 0]

                Button:
                    text: "Issue Book"
                    background_normal: ''
                    background_color: [0.1, 0.18, 0.3, 1]
                    size_hint_y: None
                    height: 45
                    halign: 'left'
                    valign: 'middle'
                    text_size: self.size
                    padding: [15, 0]

                Button:
                    text: "Issued Books"
                    background_normal: ''
                    background_color: [0.1, 0.18, 0.3, 1]
                    size_hint_y: None
                    height: 45
                    halign: 'left'
                    valign: 'middle'
                    text_size: self.size
                    padding: [15, 0]

                Button:
                    text: "Member History"
                    background_normal: ''
                    background_color: [0.1, 0.18, 0.3, 1]
                    size_hint_y: None
                    height: 45
                    halign: 'left'
                    valign: 'middle'
                    text_size: self.size
                    padding: [15, 0]

                Button:
                    text: "Logout"
                    background_normal: ''
                    background_color: [0.4, 0.15, 0.15, 1]
                    size_hint_y: None
                    height: 45
                    halign: 'left'
                    valign: 'middle'
                    text_size: self.size
                    padding: [15, 0]
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
