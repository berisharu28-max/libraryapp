import sqlite3
import os
import shutil
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.properties import StringProperty

# Global variable jo sahi database ka rasta yaad rakhega
DB_PATH = 'library.db'

KV = '''
ScreenManager:
    LoginScreen:
    DashboardScreen:
    BooksScreen:
    IssueScreen:
    IssuedBooksScreen:

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
        padding: 30
        spacing: 15
        size_hint: 1, None
        height: self.minimum_height
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        Label:
            text: "LIBREMANX"
            font_size: '36sp'
            bold: True
            size_hint_y: None
            height: 50
        Label:
            text: "Library Management System"
            font_size: '16sp'
            color: 0.7, 0.7, 0.7, 1
            size_hint_y: None
            height: 30
        Widget:
            size_hint_y: None
            height: 20
        TextInput:
            hint_text: "Username"
            multiline: False
            size_hint_y: None
            height: 48
        TextInput:
            hint_text: "Password"
            password: True
            multiline: False
            size_hint_y: None
            height: 48
        Button:
            text: "LOGIN"
            bold: True
            size_hint_y: None
            height: 50
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
        padding: [20, 40, 20, 20]
        spacing: 15
        Label:
            text: "Dashboard"
            font_size: '26sp'
            bold: True
            size_hint_y: None
            height: 40
        
        GridLayout:
            cols: 3
            spacing: 10
            size_hint_y: None
            height: 80
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: root.txt_total
                    bold: True
                    font_size: '20sp'
                Label:
                    text: "Total"
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: root.txt_issued
                    bold: True
                    font_size: '20sp'
                Label:
                    text: "Issued"
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: root.txt_available
                    bold: True
                    font_size: '20sp'
                Label:
                    text: "Available"
        
        Button:
            text: "Books Management"
            size_hint_y: None
            height: 50
            on_release: root.manager.current = 'books'
        Button:
            text: "Issue Book"
            size_hint_y: None
            height: 50
            on_release: root.manager.current = 'issue'
        Button:
            text: "Issued Books"
            size_hint_y: None
            height: 50
            on_release: root.manager.current = 'issued'
        Button:
            text: "Logout"
            size_hint_y: None
            height: 50
            on_release: root.manager.current = 'login'
        Widget:
            size_hint_y: 1

<BooksScreen>:
    name: 'books'
    BoxLayout:
        orientation: 'vertical'
        padding: 20
        Label:
            text: "Books Management Screen"
        Button:
            text: "Back to Dashboard"
            size_hint_y: None
            height: 50
            on_release: root.manager.current = 'dashboard'

<IssueScreen>:
    name: 'issue'
    BoxLayout:
        orientation: 'vertical'
        padding: 20
        Label:
            text: "Issue Book Screen"
        Button:
            text: "Back to Dashboard"
            size_hint_y: None
            height: 50
            on_release: root.manager.current = 'dashboard'

<IssuedBooksScreen>:
    name: 'issued'
    BoxLayout:
        orientation: 'vertical'
        padding: 20
        Label:
            text: "Issued Books Screen"
        Button:
            text: "Back to Dashboard"
            size_hint_y: None
            height: 50
            on_release: root.manager.current = 'dashboard'
'''

class LoginScreen(Screen):
    pass

class DashboardScreen(Screen):
    txt_total = StringProperty("0")
    txt_issued = StringProperty("0")
    txt_available = StringProperty("0")

    def on_pre_enter(self):
        global DB_PATH
        try:
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()
            
            cursor.execute("SELECT SUM(quantity) FROM books")
            res_total = cursor.fetchone()[0]
            total = int(res_total) if res_total is not None else 0
            
            cursor.execute("SELECT COUNT(*) FROM issued_books")
            issued = cursor.fetchone()[0]
            issued = int(issued) if issued is not None else 0
            
            available = total - issued
            if available < 0: available = 0
            
            self.txt_total = str(total)
            self.txt_issued = str(issued)
            self.txt_available = str(available)
            
            conn.close()
        except Exception as e:
            self.txt_total = "0"
            self.txt_issued = "0"
            self.txt_available = "0"

class BooksScreen(Screen):
    pass

class IssueScreen(Screen):
    pass

class IssuedBooksScreen(Screen):
    pass

class LibraryApp(App):
    def build(self):
        self.init_database()
        return Builder.load_string(KV)
        
    def init_database(self):
        global DB_PATH
        try:
            # Android par safe writeable directory dhoondhna
            user_dir = self.user_data_dir
            DB_PATH = os.path.join(user_dir, 'library.db')
            
            # Agar safe folder me pehle se file nahi h, toh APK waali copy kar dein
            if not os.path.exists(DB_PATH):
                bundled_db = os.path.join(os.path.dirname(__file__), 'library.db')
                if os.path.exists(bundled_db):
                    shutil.copy(bundled_db, DB_PATH)
        except Exception as e:
            DB_PATH = 'library.db' # PC par testing ke liye fallback
            
        # Tables create karne ka safe kaam
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                author TEXT,
                quantity INTEGER
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS issued_books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_name TEXT,
                father_name TEXT,
                student_class TEXT,
                roll_no TEXT,
                book_name TEXT,
                author_name TEXT
            )
        ''')
        conn.commit()
        conn.close()

if __name__ == '__main__':
    LibraryApp().run()
