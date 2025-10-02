import reflex as rx
from app.components.login_form import login_form


def login_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            class_name="absolute top-0 left-0 w-full h-full bg-gradient-to-br from-yellow-50 to-amber-200 opacity-50 z-0"
        ),
        rx.el.div(
            class_name="absolute top-1/4 left-1/4 w-96 h-96 bg-purple-200 rounded-full mix-blend-multiply filter blur-xl opacity-20 animate-blob"
        ),
        rx.el.div(
            class_name="absolute bottom-1/4 right-1/4 w-96 h-96 bg-yellow-200 rounded-full mix-blend-multiply filter blur-xl opacity-20 animate-blob animation-delay-2000"
        ),
        rx.el.div(login_form(), class_name="relative z-10"),
        class_name="relative flex min-h-screen flex-col justify-center items-center px-6 py-12 lg:px-8 bg-[#FBF7E9]",
    )