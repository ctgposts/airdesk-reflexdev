import reflex as rx
from app.states.auth_state import AuthState
from app.states.dashboard_state import DashboardState


def sidebar_item(name: str, icon: str, url: str) -> rx.Component:
    return rx.el.a(
        rx.icon(tag=icon, class_name="h-5 w-5"),
        rx.text(name, class_name="truncate"),
        on_click=lambda: DashboardState.set_active_view(name),
        class_name=rx.cond(
            DashboardState.active_view == name,
            "flex items-center gap-3 rounded-lg px-3 py-2 bg-yellow-200/50 text-yellow-900 transition-all hover:text-yellow-950 cursor-pointer",
            "flex items-center gap-3 rounded-lg px-3 py-2 text-stone-600 transition-all hover:text-stone-900 hover:bg-stone-200/50 cursor-pointer",
        ),
        width="100%",
    )


def role_based_sidebar_items() -> rx.Component:
    admin_links = [
        ("Tickets", "ticket"),
        ("Umrah Packages", "package"),
        ("Visa Mgmt", "file-text"),
        ("Customers", "users"),
        ("Reports", "bar-chart-2"),
    ]
    manager_links = [
        ("Tickets", "ticket"),
        ("Customers", "users"),
        ("Reports", "bar-chart-2"),
    ]
    staff_links = [
        ("Tickets", "ticket"),
        ("Visa Mgmt", "file-text"),
        ("Customers", "users"),
    ]
    return rx.match(
        AuthState.current_user_role,
        (
            "Admin",
            rx.fragment(
                rx.foreach(
                    admin_links,
                    lambda link: sidebar_item(
                        link[0], link[1], f"/{link[0].lower().replace(' ', '-')}"
                    ),
                )
            ),
        ),
        (
            "Manager",
            rx.fragment(
                rx.foreach(
                    manager_links,
                    lambda link: sidebar_item(
                        link[0], link[1], f"/{link[0].lower().replace(' ', '-')}"
                    ),
                )
            ),
        ),
        (
            "Staff",
            rx.fragment(
                rx.foreach(
                    staff_links,
                    lambda link: sidebar_item(
                        link[0], link[1], f"/{link[0].lower().replace(' ', '-')}"
                    ),
                )
            ),
        ),
        rx.text("Loading..."),
    )


def sidebar() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.icon(tag="gem", class_name="h-8 w-8 text-yellow-900"),
                    rx.el.span(
                        "Luxe Travel", class_name="text-xl font-bold text-stone-800"
                    ),
                    class_name="flex items-center gap-2 font-semibold",
                ),
                class_name="flex h-16 items-center border-b px-6",
            ),
            rx.el.div(
                rx.el.nav(
                    sidebar_item("Dashboard", "layout-dashboard", "/"),
                    role_based_sidebar_items(),
                    class_name="grid items-start gap-1 px-4 text-sm font-medium",
                ),
                class_name="flex-1 overflow-auto py-2",
            ),
            rx.el.div(
                rx.cond(
                    AuthState.current_user,
                    rx.el.div(
                        rx.image(
                            src=AuthState.current_user["avatar"],
                            class_name="h-10 w-10 rounded-full border-2 border-yellow-300",
                        ),
                        rx.el.div(
                            rx.text(
                                AuthState.current_user["name"],
                                class_name="font-semibold text-stone-800",
                            ),
                            rx.text(
                                AuthState.current_user["role"],
                                class_name="text-xs text-stone-500",
                            ),
                            class_name="flex-1 truncate",
                        ),
                        rx.el.button(
                            rx.icon("log-out", class_name="h-5 w-5"),
                            on_click=AuthState.logout,
                            class_name="p-2 rounded-md hover:bg-stone-200/50 text-stone-600 hover:text-stone-900 transition-colors",
                        ),
                        class_name="flex items-center gap-3 p-4",
                    ),
                    rx.el.div(class_name="p-4"),
                ),
                class_name="mt-auto border-t",
            ),
            class_name="flex h-full max-h-screen flex-col gap-2",
        ),
        class_name="hidden border-r bg-cream-100/40 lg:block slide-in-left-animation",
        width="280px",
    )