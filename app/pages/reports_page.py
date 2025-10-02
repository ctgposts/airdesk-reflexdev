import reflex as rx
from app.states.dashboard_state import DashboardState


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


def reports_page() -> rx.Component:
    sales_data = [
        {"month": "Jan", "sales": 15000},
        {"month": "Feb", "sales": 18000},
        {"month": "Mar", "sales": 22000},
        {"month": "Apr", "sales": 19000},
        {"month": "May", "sales": 25000},
        {"month": "Jun", "sales": 28000},
    ]
    return rx.el.div(
        rx.el.h1("Reports & Analytics", class_name="text-3xl font-bold text-stone-800"),
        rx.el.p(
            "Key performance indicators for your travel agency.",
            class_name="text-stone-600 mt-2",
        ),
        rx.el.div(
            stat_card(
                "Total Sales",
                "$" + DashboardState.total_sales.to_string(),
                "dollar-sign",
                "green",
            ),
            stat_card(
                "Tickets Sold",
                DashboardState.tickets_sold.to_string(),
                "ticket",
                "blue",
            ),
            stat_card(
                "Active Packages",
                DashboardState.active_packages.to_string(),
                "package",
                "purple",
            ),
            stat_card(
                "Pending Visas",
                DashboardState.pending_visas.to_string(),
                "file-text",
                "orange",
            ),
            class_name="grid gap-4 md:grid-cols-2 lg:grid-cols-4 mt-6",
        ),
        rx.el.div(
            rx.el.h2(
                "Monthly Sales Overview",
                class_name="text-xl font-semibold text-stone-800 mb-4",
            ),
            rx.recharts.bar_chart(
                rx.recharts.cartesian_grid(stroke_dasharray="3 3"),
                rx.recharts.x_axis(data_key="month"),
                rx.recharts.y_axis(),
                rx.recharts.tooltip(),
                rx.recharts.legend(),
                rx.recharts.bar(data_key="sales", fill="#a16207"),
                data=sales_data,
                height=300,
            ),
            class_name="mt-8 p-6 rounded-xl shadow-md border border-stone-200/80 bg-white/60",
        ),
        class_name="fade-in-animation",
    )