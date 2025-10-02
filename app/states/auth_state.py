import reflex as rx
from typing import TypedDict, Literal

UserRole = Literal["Admin", "Manager", "Staff"]


class User(TypedDict):
    password: str
    role: UserRole
    name: str
    avatar: str


class AuthState(rx.State):
    users: dict[str, User] = {
        "admin@luxe.travel": {
            "password": "password123",
            "role": "Admin",
            "name": "Alexandre Dupont",
            "avatar": "https://api.dicebear.com/9.x/initials/svg?seed=Alexandre%20Dupont",
        },
        "manager@luxe.travel": {
            "password": "password123",
            "role": "Manager",
            "name": "Isabella Rossi",
            "avatar": "https://api.dicebear.com/9.x/initials/svg?seed=Isabella%20Rossi",
        },
        "staff@luxe.travel": {
            "password": "password123",
            "role": "Staff",
            "name": "Chen Wei",
            "avatar": "https://api.dicebear.com/9.x/initials/svg?seed=Chen%20Wei",
        },
    }
    is_authenticated: bool = False
    current_user_email: str = ""
    error_message: str = ""

    @rx.var
    def current_user(self) -> User | None:
        if self.is_authenticated and self.current_user_email:
            return self.users.get(self.current_user_email)
        return None

    @rx.var
    def current_user_role(self) -> UserRole | None:
        user = self.current_user
        if user:
            return user["role"]
        return None

    @rx.event
    def login(self, form_data: dict):
        email = form_data["email"].lower()
        password = form_data["password"]
        user = self.users.get(email)
        if user and user["password"] == password:
            self.is_authenticated = True
            self.current_user_email = email
            self.error_message = ""
            return rx.redirect("/")
        else:
            self.error_message = "Invalid credentials. Please try again."
            return

    @rx.event
    def logout(self):
        self.is_authenticated = False
        self.current_user_email = ""
        self.error_message = ""
        return rx.redirect("/login")

    @rx.event
    def check_login(self):
        if not self.is_authenticated:
            return rx.redirect("/login")