import tkinter as tk
from tkinter import messagebox
import hashlib
import json


class LoginPage(tk.Frame):
    def __init__(self, parent, login_callback, register_callback):
        tk.Frame.__init__(self, parent)
        self.login_callback = login_callback
        self.register_callback = register_callback

        self.username_label = tk.Label(self, text="Username")
        self.username_label.pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        self.password_label = tk.Label(self, text="Password")
        self.password_label.pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        self.remember_me_var = tk.IntVar()
        self.remember_me_checkbox = tk.Checkbutton(self, text="Remember me", variable=self.remember_me_var)
        self.remember_me_checkbox.pack()

        self.login_button = tk.Button(self, text="Login", command=self.login)
        self.login_button.pack()

        self.register_button = tk.Button(self, text="Register", command=self.register)
        self.register_button.pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        if self.remember_me_var.get():
            with open("login_info.json", "w") as f:
                login_info = {"username": username, "password": hashed_password}
                json.dump(login_info, f)

        login_successful = self.login_callback(username, hashed_password)

        if login_successful:
            messagebox.showinfo("Login Successful", "You have successfully logged in!")
        else:
            messagebox.showerror("Login Failed", "Incorrect username or password")

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        with open("login_info.json", "w") as f:
            login_info = {"username": username, "password": hashed_password}
            json.dump(login_info, f)

        self.register_callback()

        messagebox.showinfo("Registration Successful", "You have successfully registered!")


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        try:
            with open("login_info.json", "r") as f:
                login_info = json.load(f)
                self.username = login_info["username"]
                self.hashed_password = login_info["password"]
        except:
            self.username = None
            self.hashed_password = None

        self.geometry("300x200")

        self.title("Login")

        self.login_page = LoginPage(self, self.handle_login, self.handle_register)
        self.login_page.pack()

    def handle_login(self, username, hashed_password):
        if self.username is None or self.hashed_password is None:
            # First-time login
            self.username = username
            self.hashed_password = hashed_password
            return True
        elif self.username == username and self.hashed_password == hashed_password:
            # Successful login
            return True
        else:
            # Incorrect login information
            return False

    def handle_register(self):
        self.username = None
        self.hashed_password = None
        self.login_page.username_entry.delete(0, tk.END)
        self.login_page.password_entry.delete(0, tk.END)
        messagebox.showinfo("Registration Successful", "You have successfully registered! Please log in.")


if __name__ == "__main__":
    app = App()
    app.mainloop()
import tkinter as tk
from tkinter import messagebox
import hashlib
import json


class LoginPage(tk.Frame):
    def __init__(self, parent, login_callback, register_callback):
        tk.Frame.__init__(self, parent)
        self.login_callback = login_callback
        self.register_callback = register_callback

        self.username_label = tk.Label(self, text="Username")
        self.username_label.pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        self.password_label = tk.Label(self, text="Password")
        self.password_label.pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        self.remember_me_var = tk.IntVar()
        self.remember_me_checkbox = tk.Checkbutton(self, text="Remember me", variable=self.remember_me_var)
        self.remember_me_checkbox.pack()

        self.login_button = tk.Button(self, text="Login", command=self.login)
        self.login_button.pack()

        self.register_button = tk.Button(self, text="Register", command=self.register)
        self.register_button.pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        if self.remember_me_var.get():
            with open("login_info.json", "w") as f:
                login_info = {"username": username, "password": hashed_password}
                json.dump(login_info, f)

        login_successful = self.login_callback(username, hashed_password)

        if login_successful:
            messagebox.showinfo("Login Successful", "You have successfully logged in!")
        else:
            messagebox.showerror("Login Failed", "Incorrect username or password")

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        with open("login_info.json", "w") as f:
            login_info = {"username": username, "password": hashed_password}
            json.dump(login_info, f)

        self.register_callback()

        messagebox.showinfo("Registration Successful", "You have successfully registered!")


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        try:
            with open("login_info.json", "r") as f:
                login_info = json.load(f)
                self.username = login_info["username"]
                self.hashed_password = login_info["password"]
        except:
            self.username = None
            self.hashed_password = None

        self.geometry("300x200")

        self.title("Login")

        self.login_page = LoginPage(self, self.handle_login, self.handle_register)
        self.login_page.pack()

    def handle_login(self, username, hashed_password):
        if self.username is None or self.hashed_password is None:
            # First-time login
            self.username = username
            self.hashed_password = hashed_password
            return True
        elif self.username == username and self.hashed_password == hashed_password:
            # Successful login
            return True
        else:
            # Incorrect login information
            return False

    def handle_register(self):
        self.username = None
        self.hashed_password = None
        self.login_page.username_entry.delete(0, tk.END)
        self.login_page.password_entry.delete(0, tk.END)
        messagebox.showinfo("Registration Successful", "You have successfully registered! Please log in.")


if __name__ == "__main__":
    app = App()
    app.mainloop()
