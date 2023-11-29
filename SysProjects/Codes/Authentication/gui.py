import tkinter as tk
from tkinter.font import Font

from add_record import Submit


class Gui(tk.Tk):
    def __init__(
        self,
        screenName: str | None = None,
        baseName: str | None = None,
        className: str = "Tk",
        useTk: bool = True,
        sync: bool = False,
        use: str | None = None,
    ) -> None:
        super().__init__("Login Page", baseName, className, useTk, sync, use)
        hide_show = tk.PhotoImage(file="D:\Python_env\python_projects\Projects\Codes\Authentication\hide_button.png")
        logo_icon = tk.PhotoImage(file="D:\Python_env\python_projects\Projects\Codes\Authentication\icon.png")
        image = hide_show.subsample(7, 7)
        self.iconphoto(True, logo_icon)
        self.title(screenName)
        self.geometry(
            f"500x245+{self.winfo_screenwidth()//2-250}+{self.winfo_screenheight()//2-245}"
        )
        self.resizable(False, False)
        pane_1: tk.PanedWindow = tk.PanedWindow(
            self, orient="horizontal", borderwidth=1, height=100, width=200
        )
        pane_2: tk.PanedWindow = tk.PanedWindow(
            self, orient="horizontal", borderwidth=1, height=100, width=200
        )
        pane_3: tk.PanedWindow = tk.PanedWindow(
            self, orient="horizontal", borderwidth=1, height=100, width=200
        )
        pane_1.pack(anchor="n")
        pane_2.pack(anchor="center")
        pane_3.pack(anchor="s")
        error_font = Font(family="Calibri", slant="italic", size=18, underline=True)

        def sign_up():
            if self.sign_up__btn["text"] == "Sign in":
                self.signin_frame["text"] = "Sign in..."
                self.sign_up__btn["text"] = "Sign up"
                self.enteranc_btn["text"] = "Sign in"
            else:
                self.signin_frame["text"] = "Sign up..."
                self.sign_up__btn["text"] = "Sign in"
                self.enteranc_btn["text"] = "Sign up"

        def enter():
            username = self.username_ent.get()
            password = self.password_ent.get()
            print(username)
            print(password)
            user = "app(username, password)"
            if self.signin_frame["text"] == "Sign in...":  # sign in
                if Submit.sign_in(username, password) == 1:
                    # self.check_label_['font'] = _error_font
                    self.check_label_["fg"] = "green"
                    self.check_label_["text"] = "Logged in"
                else:
                    self.check_label_["font"] = error_font
                    self.check_label_["fg"] = "red"
                    self.check_label_["text"] = "username or password incorrect!"
            else:  # sign up
                try:
                    assert Submit.sign_up(username, password) == 1
                except:
                    self.check_label_["font"] = error_font
                    self.check_label_["fg"] = "red"
                    self.check_label_["text"] = "Username Exists. try sign in instead"
                else:
                    self.check_label_["fg"] = "blue"
                    self.check_label_["text"] = "Successfuly Signed up"

        def show(sh):
            if sh == "*":
                self.password_ent["show"] = ""
            else:
                self.password_ent["show"] = "*"

        self.signin_frame: tk.LabelFrame = tk.LabelFrame(
            pane_2,
            text="Sign in...",
            width=60,
            height=50,
            font="Calibri 25",
            padx=10,
            pady=10,
        )
        self.check_label_: tk.Label = tk.Label(
            pane_1,
            text="Enter username and password",
            font="Calibri 18",
            justify="center",
            pady=8,
        )
        self.username_lbl: tk.Label = tk.Label(
            self.signin_frame, text="User name:", font="Arial 10", padx=10, pady=10
        )
        self.password_lbl: tk.Label = tk.Label(
            self.signin_frame, text="Password: ", font="Arial 10", padx=10, pady=10
        )
        self.spacer_e_lbl: tk.Label = tk.Label(self.signin_frame, width=2)
        self.username_ent: tk.Entry = tk.Entry(
            self.signin_frame, width=30, borderwidth=5, font="simsun 16"
        )
        self.password_ent: tk.Entry = tk.Entry(
            self.signin_frame, width=30, borderwidth=5, font="simsun 16", show="*"
        )
        self.enteranc_btn: tk.Button = tk.Button(
            self.signin_frame, text="Sign in", width=6, padx=10, pady=10, command=enter
        )
        self.show_hid_btn: tk.Button = tk.Button(
            self.signin_frame,
            image=image,
            borderwidth=0,
            width=11,
            height=11,
            padx=20,
            command=lambda: show(self.password_ent["show"]),
        )
        self.sign_up__btn: tk.Button = tk.Button(
            self.signin_frame, text="Sign up", relief="flat", fg="blue", command=sign_up
        )
        self.sign_up__lbl: tk.Label = tk.Label(
            self.signin_frame, text="dont have\naccount?", font="Calibri 9", fg="black"
        )

        ### Griding
        self.signin_frame.grid(column=0, row=0)
        self.check_label_.grid(column=0, row=0)
        self.username_lbl.grid(column=0, row=0)
        self.password_lbl.grid(column=0, row=1)
        self.spacer_e_lbl.grid(column=1, row=0, rowspan=2)
        self.username_ent.grid(column=2, row=0)
        self.password_ent.grid(column=2, row=1)
        self.enteranc_btn.grid(column=2, row=2, sticky="E")
        self.show_hid_btn.grid(column=3, row=1)
        self.sign_up__btn.grid(column=2, row=2, sticky="W")
        self.sign_up__lbl.grid(column=0, row=2)

        self.mainloop()


# login_page = Gui('Login_Test')
