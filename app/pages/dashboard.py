import reflex as rx
from app.states.dashboard_state import DashboardState
from app.states.auth_state import AuthState
from app.pages.tickets_page import tickets_page
from app.pages.packages_page import packages_page
from app.pages.visa_page import visa_page
from app.pages.customers_page import customers_page
from app.pages.reports_page import reports_page
from app.pages.bookings_page import bookings_page


def stat_card(title: str, value: rx.Var[str], icon: str, color: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(tag=icon, class_name="h-6 w-6"),
            class_name=f"p-3 rounded-full bg-{color}-100 text-{color}-600",
        ),
        rx.el.div(
            rx.text(title, class_name="text-sm font-medium text-stone-500"),
            rx.text(value, class_name="text-2xl font-bold text-stone-800"),
            class_name="flex-1",
        ),
        class_name="flex items-center gap-4 p-4 rounded-xl shadow-sm border border-stone-200/80 bg-white/60 float-animation",
    )


def dashboard_view() -> rx.Component:
    return rx.el.div(
        rx.el.h1(
            "Welcome, ",
            rx.el.span(
                AuthState.current_user["name"], class_name="text-yellow-900 font-bold"
            ),
            "!",
            class_name="text-3xl font-semibold text-stone-800",
        ),
        rx.el.p(
            "Here's a quick overview of your agency's activities.",
            class_name="text-stone-600 mt-2",
        ),
        rx.el.div(
            stat_card(
                "Total Tickets",
                DashboardState.total_tickets.to_string(),
                "ticket",
                "blue",
            ),
            stat_card(
                "Available Tickets",
                DashboardState.available_tickets.to_string(),
                "square_check",
                "green",
            ),
            stat_card(
                "Booked Tickets",
                DashboardState.booked_tickets.to_string(),
                "calendar",
                "orange",
            ),
            stat_card(
                "Total Customers",
                DashboardState.total_customers.to_string(),
                "users",
                "purple",
            ),
            class_name="grid gap-4 md:grid-cols-2 lg:grid-cols-4 mt-6",
        ),
        class_name="fade-in-animation",
    )


def dashboard_page() -> rx.Component:
    return rx.el.div(
        rx.match(
            DashboardState.active_view,
            ("Dashboard", dashboard_view()),
            ("Tickets", tickets_page()),
            ("Bookings", bookings_page()),
            ("Umrah Packages", packages_page()),
            ("Visa Mgmt", visa_page()),
            ("Customers", customers_page()),
            ("Reports", reports_page()),
            dashboard_view(),
        )
    )