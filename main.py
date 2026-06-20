from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

KV = '''
ScreenManager:
    LoginScreen:
    DashboardScreen:

<LoginScreen>:
    name: 'login'
    md_bg_color: 0.06, 0.12, 0.21, 1

    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(24)
        spacing: dp(24)
        adaptive_height: True
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}

        MDLabel:
            text: "LIBREMANX"
            font_style: "H4"
            halign: "center"
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            bold: True

        MDLabel:
            text: "Library Management System"
            font_style: "Subtitle1"
            halign: "center"
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 0.6

        MDTextField:
            id: username
            hint_text: "Username"
            icon_left: "account"

        MDTextField:
            id: password
            hint_text: "Password"
            password: True
            icon_left: "key"

        MDRaisedButton:
            text: "LOGIN"
            md_bg_color: 0.15, 0.27, 0.44, 1
            size_hint_x: 1
            height: dp(48)
            on_release: root.manager.current = 'dashboard'

<DashboardScreen>:
    name: 'dashboard'
    md_bg_color: 0.06, 0.12, 0.21, 1

    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(16)
        spacing: dp(16)

        # Top Profile Bar
        MDBoxLayout:
            size_hint_y: None
            height: dp(56)
            spacing: dp(10)
            
            MDLabel:
                text: "LIBREMANX"
                font_style: "H5"
                bold: True
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1

            MDIconButton:
                icon: "account-circle"
                theme_text_color: "Custom"
                text_color: 0.7, 0.8, 1, 1
                
            MDIconButton:
                icon: "bell-outline"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1

        # Dashboard Title
        MDLabel:
            text: "DASHBOARD"
            font_style: "H6"
            bold: True
            size_hint_y: None
            height: dp(30)
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1

        # Search Bar
        MDTextField:
            hint_text: "Search"
            icon_left: "magnify"
            size_hint_y: None
            height: dp(44)

        # Cards Row
        MDGridLayout:
            cols: 3
            spacing: dp(8)
            size_hint_y: None
            height: dp(130)

            # Total Books Card
            MDCard:
                orientation: 'vertical'
                padding: dp(8)
                spacing: dp(4)
                md_bg_color: 0.88, 0.93, 1, 1
                radius: [12, 12, 12, 12]

                MDIcon:
                    icon: "bookshelf"
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: 0.1, 0.3, 0.6, 1
                MDLabel:
                    text: "1,245"
                    halign: "center"
                    bold: True
                    font_style: "Subtitle1"
                    theme_text_color: "Custom"
                    text_color: 0.1, 0.2, 0.4, 1
                MDLabel:
                    text: "Total Books"
                    halign: "center"
                    font_style: "Caption"
                    theme_text_color: "Custom"
                    text_color: 0.3, 0.4, 0.5, 1

            # Issued Books Card
            MDCard:
                orientation: 'vertical'
                padding: dp(8)
                spacing: dp(4)
                md_bg_color: 0.88, 0.96, 0.9, 1
                radius: [12, 12, 12, 12]

                MDIcon:
                    icon: "book-arrow-up"
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: 0.1, 0.5, 0.2, 1
                MDLabel:
                    text: "112"
                    halign: "center"
                    bold: True
                    font_style: "Subtitle1"
                    theme_text_color: "Custom"
                    text_color: 0.1, 0.4, 0.2, 1
                MDLabel:
                    text: "Issued Books"
                    halign: "center"
                    font_style: "Caption"
                    theme_text_color: "Custom"
                    text_color: 0.2, 0.4, 0.3, 1

            # Available Books Card
            MDCard:
                orientation: 'vertical'
                padding: dp(8)
                spacing: dp(4)
                md_bg_color: 1, 0.93, 0.85, 1
                radius: [12, 12, 12, 12]

                MDIcon:
                    icon: "book-check"
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: 0.7, 0.4, 0.1, 1
                MDLabel:
                    text: "1,133"
                    halign: "center"
                    bold: True
                    font_style: "Subtitle1"
                    theme_text_color: "Custom"
                    text_color: 0.5, 0.3, 0.1, 1
                MDLabel:
                    text: "Available"
                    halign: "center"
                    font_style: "Caption"
                    theme_text_color: "Custom"
                    text_color: 0.5, 0.4, 0.3, 1

        # Menu List Section
        MDScrollView:
            MDBoxLayout:
                orientation: 'vertical'
                spacing: dp(12)
                adaptive_height: True

                # Books Management
                MDBoxLayout:
                    size_hint_y: None
                    height: dp(50)
                    spacing: dp(12)
                    MDIcon:
                        icon: "notebook-cog"
                        theme_text_color: "Custom"
                        text_color: 1, 1, 1, 1
                        size_hint_x: None
                        width: dp(24)
                    MDLabel:
                        text: "Books Management"
                        theme_text_color: "Custom"
                        text_color: 1, 1, 1, 1
                    MDIcon:
                        icon: "chevron-right"
                        theme_text_color: "Custom"
                        text_color: 1, 1, 1, 0.4
                        size_hint_x: None
                        width: dp(24)

                # Issue Book
                MDBoxLayout:
                    size_hint_y: None
                    height: dp(50)
                    spacing: dp(12)
                    MDIcon:
                        icon: "book-plus"
                        theme_icon_color: "Custom"
                        icon_color: [1, 1, 1, 1]
                        size_hint_x: None
                        width: dp(24)
                    MDLabel:
                        text: "Issue Book"
                        theme_text_color: "Custom"
                        text_color: 1, 1, 1, 1

                # Issued Books List
                MDBoxLayout:
                    size_hint_y: None
                    height: dp(50)
                    spacing: dp(12)
                    MDIcon:
                        icon: "book-multiple"
                        theme_text_color: "Custom"
                        text_color: 1, 1, 1, 1
                        size_hint_x: None
                        width: dp(24)
                    MDLabel:
                        text: "Issued Books"
                        theme_text_color: "Custom"
                        text_color: 1, 1, 1, 1

                # Member History
                MDBoxLayout:
                    size_hint_y: None
                    height: dp(50)
                    spacing: dp(12)
                    MDIcon:
                        icon: "card-account-details"
                        theme_text_color: "Custom"
                        text_color: 1, 1, 1, 1
                        size_hint_x: None
                        width: dp(24)
                    MDLabel:
                        text: "Member History"
                        theme_text_color: "Custom"
                        text_color: 1, 1, 1, 1

                # Logout
                MDBoxLayout:
                    size_hint_y: None
                    height: dp(50)
                    spacing: dp(12)
                    MDIcon:
                        icon: "logout"
                        theme_text_color: "Custom"
                        text_color: 0.9, 0.3, 0.3, 1
                        size_hint_x: None
                        width: dp(24)
                    MDLabel:
                        text: "Logout"
                        theme_text_color: "Custom"
                        text_color: 0.9, 0.3, 0.3, 1
                        bold: True
'''

class LoginScreen(Screen):
    pass

class DashboardScreen(Screen):
    pass

class LibraryApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_string(KV)

if __name__ == '__main__':
    LibraryApp().run()
