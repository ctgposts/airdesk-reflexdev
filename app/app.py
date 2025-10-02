import reflex as rx
from app.states.auth_state import AuthState
from app.pages.login_page import login_page
from app.components.sidebar import sidebar
from app.pages.dashboard import dashboard_page


def index() -> rx.Component:
    return rx.el.div(
        sidebar(),
        rx.el.main(
            dashboard_page(),
            class_name="flex flex-col flex-1 gap-4 p-4 md:gap-8 md:p-6",
        ),
        class_name="grid min-h-screen w-full lg:grid-cols-[280px_1fr] font-['Inter'] bg-[#FBF7E9]",
    )


app = rx.App(
    theme=rx.theme(appearance="light", accent_color="amber"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap",
            rel="stylesheet",
        ),
        rx.el.link(rel="stylesheet", href="/animations.css"),
    ],
)
app.add_page(index, on_load=AuthState.check_login)
app.add_page(login_page, route="/login")