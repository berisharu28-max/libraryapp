from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window

# Laptop par check karne ke liye size (Phone par auto-fit ho jayega)
Window.size = (360, 640)

KV = '''
ScreenManager:
    LoginScreen:
    DashboardScreen:

# Custom Button Design for Menu
<MenuListButton@Button>:
    background_color: 0, 0, 0, 0
    background_normal: ''
    font_size: '16sp'
    halign: 'left'
    valign: 'middle'
    text_size: self.size
    padding_x: dp(20)
    canvas.before:
        Color:
            rgba: 0.1, 0.18, 0.3, 1
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [8]

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
        padding: dp(24)
        spacing: dp(20)
        size_hint_y: None
        height: self.minimum_height
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}

        Label:
            text: "LIBREMANX"
            font_size: '32sp'
            bold: True
            color: 1, 1, 1, 1

        Label:
            text: "Library Management System"
            font_size: '14sp'
            color: 1, 1, 1, 0.6

        TextInput:
            hint_text: "Username"
            multiline: False
            size_hint_y: None
            height: dp(46)
            background_color: 0.1, 0.18, 0.3, 1
            foreground_color: 1, 1, 1, 1
            hint_text_color: 1, 1, 1, 0.4
            padding: [dp(12), dp(12), dp(12), dp(12)]

        TextInput:
            hint_text: "Password"
            password: True
            multiline: False
            size_hint_y: None
            height: dp(46)
            background_color: 0.1, 0.18, 0.3, 1
            foreground_color: 1, 1, 1, 1
            hint_text_color: 1, 1, 1, 0.4
            padding: [dp(12), dp(12), dp(12), dp(12)]

        Button:
            text: "LOGIN"
            bold: True
            font_size: '16sp'
            size_hint_y: None
            height: dp(50)
            background_color: 0, 0, 0, 0
            background_normal: ''
            on_release: root.manager.current = 'dashboard'
            canvas.before:
                Color:
                    rgba: 0.15, 0.27, 0.44, 1
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [8]

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
        padding: dp(16)
        spacing: dp(16)

        # Top Profile Bar
        BoxLayout:
            size_hint_y: None
            height: dp(56)
            Label:
                text: "LIBREMANX"
                font_size: '24sp'
                bold: True
                halign: 'left'
                text_size: self.size
            Label:
                text: "👤"
                font_size: '22sp'
                size_hint_x: None
                width: dp(40)
            Label:
                text: "🔔"
                font_size: '22sp'
                size_hint_x: None
                width: dp(40)

        # Dashboard Title
        Label:
            text: "DASHBOARD"
            font_size: '18sp'
            bold: True
            size_hint_y: None
            height: dp(24)
            halign: 'left'
            text_size: self.size

        # Search Bar
        TextInput:
            hint_text: "🔍  Search books..."
            multiline: False
            size_hint_y: None
            height: dp(42)
            background_color: 0.1, 0.18, 0.3, 1
            foreground_color: 1, 1, 1, 1
            hint_text_color: 1, 1, 1, 0.4
            padding: [dp(12), dp(12), dp(12), dp(12)]

        # Cards Row (Grid Layout)
        GridLayout:
            cols: 3
            spacing: dp(8)
            size_hint_y: None
            height: dp(120)

            # Total Books Card
            BoxLayout:
                orientation: 'vertical'
                padding: dp(8)
                canvas.before:
                    Color:
                        rgba: 0.88, 0.93, 1, 1
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [10]
                Label:
                    text: "📚"
                    font_size: '24sp'
                Label:
                    text: "1,245"
                    bold: True
                    color: 0.1, 0.2, 0.4, 1
                    font_size: '16sp'
                Label:
                    text: "Total Books"
                    color: 0.3, 0.4, 0.5, 1
                    font_size: '11sp'

            # Issued Books Card
            BoxLayout:
                orientation: 'vertical'
                padding: dp(8)
                canvas.before:
                    Color:
                        rgba: 0.88, 0.96, 0.9, 1
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [10]
                Label:
                    text: "📤"
                    font_size: '24sp'
                Label:
                    text: "112"
                    bold: True
                    color: 0.1, 0.4, 0.2, 1
                    font_size: '16sp'
                Label:
                    text: "Issued"
                    color: 0.2, 0.4, 0.3, 1
                    font_size: '11sp'

            # Available Books Card
            BoxLayout:
                orientation: 'vertical'
                padding: dp(8)
                canvas.before:
                    Color:
                        rgba: 1, 0.93, 0.85, 1
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [10]
                Label:
                    text: "✅"
                    font_size: '24sp'
                Label:
                    text: "1,133"
                    bold: True
                    color: 0.5, 0.3, 0.1, 1
                    font_size: '16sp'
                Label:
                    text: "Available"
                    color: 0.5, 0.4, 0.3, 1
                    font_size: '11sp'

        # Menu List Section
        ScrollView:
            BoxLayout:
                orientation: 'vertical'
                spacing: dp(10)
                size_hint_y: None
                height: self.minimum_height

                MenuListButton:
                    text: "⚙️      Books Management"
                    size_hint_y: None
                    height: dp(50)

                MenuListButton:
                    text: "➕      Issue Book"
                    size_hint_y: None
                    height: dp(50)

                MenuListButton:
                    text: "📋      Issued Books"
                    size_hint_y: None
                    height: dp(50)

                MenuListButton:
                    text: "👤      Member History"
                    size_hint_y: None
                    height: dp(50)
                
                # Logout Button
                Button:
                    text: "🚪      Logout"
                    font_size: '16sp'
                    bold: True
                    color: 0.9, 0.3, 0.3, 1
                    halign: 'left'
                    valign: 'middle'
                    text_size: self.size
                    padding_x: dp(20)
                    background_color: 0, 0, 0, 0
                    background_normal: ''
                    size_hint_y: None
                    height: dp(50)
                    on_release: root.manager.current = 'login'
                    canvas.before:
                        Color:
                            rgba: 0.18, 0.1, 0.15, 1
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [8]
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
