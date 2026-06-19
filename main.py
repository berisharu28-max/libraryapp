import os
import sqlite3
from datetime import datetime, timedelta
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

class LoginScreen(Screen):
    def login(self):
        if self.ids.username.text.strip() == "admin" and self.ids.password.text.strip() == "1234":
            self.manager.current = "dashboard"
        else:
            self.ids.login_status.text = "Invalid Login"

class DashboardScreen(Screen):
    def on_enter(self):
        app = App.get_running_app()
        cursor = app.cursor

        cursor.execute("SELECT COUNT(*) FROM books")
        self.ids.total_books.text = str(cursor.fetchone()[0])

        cursor.execute("SELECT COUNT(*) FROM issued_books")
        self.ids.issued_books.text = str(cursor.fetchone()[0])

        cursor.execute("SELECT COALESCE(SUM(quantity),0) FROM books")
        self.ids.available_books.text = str(cursor.fetchone()[0])

class BookScreen(Screen):
    def add_book(self):
        app = App.get_running_app()
        cursor = app.cursor

        quantity_text = self.ids.book_quantity.text.strip()
        quantity = int(quantity_text) if quantity_text.isdigit() else 0

        cursor.execute(
            "INSERT INTO books(title,author,quantity) VALUES(?,?,?)",
            (self.ids.book_title.text.strip(), self.ids.book_author.text.strip(), quantity)
        )
        app.conn.commit()
        self.ids.book_status.text = "Book Added"

    def view_books(self):
        app = App.get_running_app()
        cursor = app.cursor

        cursor.execute("SELECT title,author,quantity FROM books")
        rows = cursor.fetchall()
        self.ids.book_status.text = "\n".join([f"{a} | {b} | Qty:{c}" for a,b,c in rows]) or "No Books"

class IssueScreen(Screen):
    def issue_book(self):
        app = App.get_running_app()
        cursor = app.cursor

        book = self.ids.issue_book_name.text.strip()
        cursor.execute("SELECT author, quantity FROM books WHERE title=?", (book,))
        row = cursor.fetchone()
        if not row:
            self.ids.issue_status.text = "Book Not Found"
            return

        if row[1] <= 0:
            self.ids.issue_status.text = "Book Not Available"
            return

        issue_date = datetime.now().strftime("%d-%m-%Y")
        return_date = (datetime.now() + timedelta(days=14)).strftime("%d-%m-%Y")

        cursor.execute(
            "INSERT INTO issued_books"
            "(student_name,father_name,student_class,roll_no,book_name,author_name,issue_date,return_date)"
            "VALUES (?,?,?,?,?,?,?,?)",
            (
                self.ids.student_name.text.strip(),
                self.ids.father_name.text.strip(),
                self.ids.student_class.text.strip(),
                self.ids.roll_no.text.strip(),
                book,
                row[0],
                issue_date,
                return_date
            )
        )
        cursor.execute("UPDATE books SET quantity=quantity-1 WHERE title=?", (book,))
        app.conn.commit()
        self.ids.issue_status.text = f"Issue: {issue_date}\nReturn: {return_date}"

class IssuedBooksScreen(Screen):
    def show_issued_books(self):
        app = App.get_running_app()
        cursor = app.cursor

        cursor.execute("SELECT student_name, book_name, issue_date, return_date FROM issued_books")
        rows = cursor.fetchall()
        self.ids.issued_label.text = "\n\n".join(
            [f"{a} | {b}\nIssue:{c}\nReturn:{d}" for a,b,c,d in rows]
        ) or "No Issued Books"

class WindowManager(ScreenManager):
    pass

class LibraryApp(App):
    db_filename = "library.db"

    def build(self):
        self.ensure_data_dir()
        self.connect_database()
        return Builder.load_file("library.kv")

    def ensure_data_dir(self):
        if not os.path.exists(self.user_data_dir):
            os.makedirs(self.user_data_dir, exist_ok=True)

    def connect_database(self):
        self.db_path = os.path.join(self.user_data_dir, self.db_filename)
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        self.init_database()

    def init_database(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS books(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author TEXT,
            quantity INTEGER
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS issued_books(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_name TEXT,
            father_name TEXT,
            student_class TEXT,
            roll_no TEXT,
            book_name TEXT,
            author_name TEXT,
            issue_date TEXT,
            return_date TEXT
        )
        """)
        self.conn.commit()

    def on_stop(self):
        if hasattr(self, "conn"):
            self.conn.commit()
            self.conn.close()

if __name__ == "__main__":
    LibraryApp().run()
