import reflex as rx
from app.states.dashboard_state import DashboardState
from app.states.auth_state import AuthState


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
        class_name="p-6 fade-in-animation",
    )


def status_badge(status: rx.Var[str]) -> rx.Component:
    base_class = " text-xs font-medium me-2 px-2.5 py-0.5 rounded-full border w-fit"
    return rx.el.div(
        status,
        class_name=rx.match(
            status,
            ("Sold", "bg-green-100 text-green-800 border-green-200" + base_class),
            ("Available", "bg-blue-100 text-blue-800 border-blue-200" + base_class),
            ("Booked", "bg-orange-100 text-orange-800 border-orange-200" + base_class),
            ("Cancelled", "bg-red-100 text-red-800 border-red-200" + base_class),
            (
                "Purchased",
                "bg-purple-100 text-purple-800 border-purple-200" + base_class,
            ),
            "bg-gray-100 text-gray-800 border-gray-200" + base_class,
        ),
    )


def tickets_view() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h1(
                "Ticket Management", class_name="text-3xl font-bold text-stone-800"
            ),
            rx.el.button(
                rx.icon("plus", class_name="h-4 w-4 mr-2"),
                "Add New Ticket",
                class_name="inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50 bg-yellow-900/90 text-white shadow hover:bg-yellow-900 h-9 px-4 py-2",
            ),
            class_name="flex justify-between items-center mb-6",
        ),
        rx.el.div(
            rx.el.table(
                rx.el.thead(
                    rx.el.tr(
                        rx.el.th(
                            "PNR",
                            class_name="py-3 px-4 text-left text-sm font-semibold text-stone-700",
                        ),
                        rx.el.th(
                            "Customer",
                            class_name="py-3 px-4 text-left text-sm font-semibold text-stone-700",
                        ),
                        rx.el.th(
                            "Type",
                            class_name="py-3 px-4 text-left text-sm font-semibold text-stone-700",
                        ),
                        rx.el.th(
                            "Status",
                            class_name="py-3 px-4 text-left text-sm font-semibold text-stone-700",
                        ),
                        rx.el.th(
                            "Price",
                            class_name="py-3 px-4 text-right text-sm font-semibold text-stone-700",
                        ),
                        rx.el.th(
                            "Actions",
                            class_name="py-3 px-4 text-center text-sm font-semibold text-stone-700",
                        ),
                    ),
                    class_name="bg-stone-100/80",
                ),
                rx.el.tbody(
                    rx.foreach(
                        DashboardState.tickets,
                        lambda ticket: rx.el.tr(
                            rx.el.td(
                                ticket["pnr"],
                                class_name="py-3 px-4 font-mono text-sm text-stone-800",
                            ),
                            rx.el.td(
                                rx.cond(
                                    ticket["customer_name"] != "",
                                    ticket["customer_name"],
                                    rx.el.span(
                                        "N/A", class_name="text-stone-400 italic"
                                    ),
                                ),
                                class_name="py-3 px-4 text-sm text-stone-600",
                            ),
                            rx.el.td(
                                ticket["type"],
                                class_name="py-3 px-4 text-sm text-stone-600",
                            ),
                            rx.el.td(
                                status_badge(ticket["status"]), class_name="py-3 px-4"
                            ),
                            rx.el.td(
                                "$" + ticket["price"].to_string(),
                                class_name="py-3 px-4 text-right font-medium text-stone-800",
                            ),
                            rx.el.td(
                                rx.el.div(
                                    rx.el.button(
                                        rx.icon("eye", class_name="h-4 w-4"),
                                        class_name="p-2 rounded-md hover:bg-stone-200/50 text-stone-600 hover:text-stone-900 transition-colors",
                                    ),
                                    rx.el.button(
                                        rx.icon("pencil", class_name="h-4 w-4"),
                                        class_name="p-2 rounded-md hover:bg-stone-200/50 text-stone-600 hover:text-stone-900 transition-colors",
                                    ),
                                    rx.el.button(
                                        rx.icon("trash-2", class_name="h-4 w-4"),
                                        class_name="p-2 rounded-md hover:bg-red-100 text-red-600 hover:text-red-800 transition-colors",
                                    ),
                                    class_name="flex items-center justify-center gap-2",
                                ),
                                class_name="py-3 px-4",
                            ),
                            class_name="border-b border-stone-200/60 hover:bg-yellow-50/50 transition-colors",
                        ),
                    )
                ),
                class_name="w-full text-sm",
            ),
            class_name="rounded-xl shadow-md border border-stone-200/80 bg-white/60 overflow-hidden",
        ),
        class_name="p-6 fade-in-animation",
    )


def package_status_badge(status: rx.Var[bool]) -> rx.Component:
    base_class = " text-xs font-medium me-2 px-2.5 py-0.5 rounded-full border w-fit"
    return rx.cond(
        status,
        rx.el.div(
            "Active",
            class_name="bg-green-100 text-green-800 border-green-200" + base_class,
        ),
        rx.el.div(
            "Inactive",
            class_name="bg-gray-100 text-gray-800 border-gray-200" + base_class,
        ),
    )


def umrah_packages_view() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h1("Umrah Packages", class_name="text-3xl font-bold text-stone-800"),
            rx.el.button(
                rx.icon("plus", class_name="h-4 w-4 mr-2"),
                "Add New Package",
                class_name="inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50 bg-yellow-900/90 text-white shadow hover:bg-yellow-900 h-9 px-4 py-2",
            ),
            class_name="flex justify-between items-center mb-6",
        ),
        rx.el.div(
            rx.el.table(
                rx.el.thead(
                    rx.el.tr(
                        rx.el.th(
                            "Package Name",
                            class_name="py-3 px-4 text-left text-sm font-semibold text-stone-700",
                        ),
                        rx.el.th(
                            "Duration",
                            class_name="py-3 px-4 text-left text-sm font-semibold text-stone-700",
                        ),
                        rx.el.th(
                            "Price",
                            class_name="py-3 px-4 text-right text-sm font-semibold text-stone-700",
                        ),
                        rx.el.th(
                            "Status",
                            class_name="py-3 px-4 text-left text-sm font-semibold text-stone-700",
                        ),
                        rx.el.th(
                            "Actions",
                            class_name="py-3 px-4 text-center text-sm font-semibold text-stone-700",
                        ),
                    ),
                    class_name="bg-stone-100/80",
                ),
                rx.el.tbody(
                    rx.foreach(
                        DashboardState.umrah_packages,
                        lambda pkg: rx.el.tr(
                            rx.el.td(
                                pkg["name"],
                                class_name="py-3 px-4 font-medium text-stone-800",
                            ),
                            rx.el.td(
                                pkg["duration"].to_string() + " Days",
                                class_name="py-3 px-4 text-sm text-stone-600",
                            ),
                            rx.el.td(
                                "$" + pkg["price"].to_string(),
                                class_name="py-3 px-4 text-right font-medium text-stone-800",
                            ),
                            rx.el.td(
                                package_status_badge(pkg["is_active"]),
                                class_name="py-3 px-4",
                            ),
                            rx.el.td(
                                rx.el.div(
                                    rx.el.button(
                                        rx.icon("eye", class_name="h-4 w-4"),
                                        class_name="p-2 rounded-md hover:bg-stone-200/50 text-stone-600 hover:text-stone-900 transition-colors",
                                    ),
                                    rx.el.button(
                                        rx.icon("pencil", class_name="h-4 w-4"),
                                        class_name="p-2 rounded-md hover:bg-stone-200/50 text-stone-600 hover:text-stone-900 transition-colors",
                                    ),
                                    rx.el.button(
                                        rx.icon("trash-2", class_name="h-4 w-4"),
                                        class_name="p-2 rounded-md hover:bg-red-100 text-red-600 hover:text-red-800 transition-colors",
                                    ),
                                    class_name="flex items-center justify-center gap-2",
                                ),
                                class_name="py-3 px-4",
                            ),
                            class_name="border-b border-stone-200/60 hover:bg-yellow-50/50 transition-colors",
                        ),
                    )
                ),
                class_name="w-full text-sm",
            ),
            class_name="rounded-xl shadow-md border border-stone-200/80 bg-white/60 overflow-hidden",
        ),
        class_name="p-6 fade-in-animation",
    )


def visa_status_badge(status: rx.Var[str]) -> rx.Component:
    base_class = " text-xs font-medium me-2 px-2.5 py-0.5 rounded-full border w-fit"
    return rx.el.div(
        status,
        class_name=rx.match(
            status,
            ("Approved", "bg-green-100 text-green-800 border-green-200" + base_class),
            ("In Process", "bg-blue-100 text-blue-800 border-blue-200" + base_class),
            ("Pending", "bg-orange-100 text-orange-800 border-orange-200" + base_class),
            ("Rejected", "bg-red-100 text-red-800 border-red-200" + base_class),
            "bg-gray-100 text-gray-800 border-gray-200" + base_class,
        ),
    )


def visa_mgmt_view() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h1("Visa Management", class_name="text-3xl font-bold text-stone-800"),
            rx.el.button(
                rx.icon("plus", class_name="h-4 w-4 mr-2"),
                "New Application",
                class_name="inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50 bg-yellow-900/90 text-white shadow hover:bg-yellow-900 h-9 px-4 py-2",
            ),
            class_name="flex justify-between items-center mb-6",
        ),
        rx.el.div(
            rx.el.table(
                rx.el.thead(
                    rx.el.tr(
                        rx.el.th(
                            "Customer",
                            class_name="py-3 px-4 text-left text-sm font-semibold text-stone-700",
                        ),
                        rx.el.th(
                            "Country",
                            class_name="py-3 px-4 text-left text-sm font-semibold text-stone-700",
                        ),
                        rx.el.th(
                            "Status",
                            class_name="py-3 px-4 text-left text-sm font-semibold text-stone-700",
                        ),
                        rx.el.th(
                            "Submitted",
                            class_name="py-3 px-4 text-left text-sm font-semibold text-stone-700",
                        ),
                        rx.el.th(
                            "Actions",
                            class_name="py-3 px-4 text-center text-sm font-semibold text-stone-700",
                        ),
                    ),
                    class_name="bg-stone-100/80",
                ),
                rx.el.tbody(
                    rx.foreach(
                        DashboardState.visa_applications,
                        lambda app: rx.el.tr(
                            rx.el.td(
                                app["customer_name"],
                                class_name="py-3 px-4 font-medium text-stone-800",
                            ),
                            rx.el.td(
                                app["country"],
                                class_name="py-3 px-4 text-sm text-stone-600",
                            ),
                            rx.el.td(
                                visa_status_badge(app["status"]), class_name="py-3 px-4"
                            ),
                            rx.el.td(
                                app["submission_date"],
                                class_name="py-3 px-4 text-sm text-stone-600",
                            ),
                            rx.el.td(
                                rx.el.div(
                                    rx.el.button(
                                        rx.icon("eye", class_name="h-4 w-4"),
                                        class_name="p-2 rounded-md hover:bg-stone-200/50 text-stone-600 hover:text-stone-900 transition-colors",
                                    ),
                                    rx.el.button(
                                        rx.icon("pencil", class_name="h-4 w-4"),
                                        class_name="p-2 rounded-md hover:bg-stone-200/50 text-stone-600 hover:text-stone-900 transition-colors",
                                    ),
                                    class_name="flex items-center justify-center gap-2",
                                ),
                                class_name="py-3 px-4",
                            ),
                            class_name="border-b border-stone-200/60 hover:bg-yellow-50/50 transition-colors",
                        ),
                    )
                ),
                class_name="w-full text-sm",
            ),
            class_name="rounded-xl shadow-md border border-stone-200/80 bg-white/60 overflow-hidden",
        ),
        class_name="p-6 fade-in-animation",
    )


def customers_view() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h1(
                "Customer Management", class_name="text-3xl font-bold text-stone-800"
            ),
            rx.el.button(
                rx.icon("plus", class_name="h-4 w-4 mr-2"),
                "Add New Customer",
                class_name="inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50 bg-yellow-900/90 text-white shadow hover:bg-yellow-900 h-9 px-4 py-2",
            ),
            class_name="flex justify-between items-center mb-6",
        ),
        rx.el.div(
            rx.el.table(
                rx.el.thead(
                    rx.el.tr(
                        rx.el.th(
                            "Customer",
                            class_name="py-3 px-4 text-left text-sm font-semibold text-stone-700",
                        ),
                        rx.el.th(
                            "Contact",
                            class_name="py-3 px-4 text-left text-sm font-semibold text-stone-700",
                        ),
                        rx.el.th(
                            "Address",
                            class_name="py-3 px-4 text-left text-sm font-semibold text-stone-700",
                        ),
                        rx.el.th(
                            "Actions",
                            class_name="py-3 px-4 text-center text-sm font-semibold text-stone-700",
                        ),
                    ),
                    class_name="bg-stone-100/80",
                ),
                rx.el.tbody(
                    rx.foreach(
                        DashboardState.customers,
                        lambda customer: rx.el.tr(
                            rx.el.td(
                                rx.el.div(
                                    rx.image(
                                        src=f"https://api.dicebear.com/9.x/initials/svg?seed={customer['name']}",
                                        class_name="h-10 w-10 rounded-full border-2 border-yellow-200",
                                    ),
                                    rx.el.div(
                                        rx.text(
                                            customer["name"],
                                            class_name="font-medium text-stone-800",
                                        ),
                                        rx.text(
                                            customer["email"],
                                            class_name="text-xs text-stone-500",
                                        ),
                                    ),
                                    class_name="flex items-center gap-3",
                                ),
                                class_name="py-3 px-4",
                            ),
                            rx.el.td(
                                customer["phone"],
                                class_name="py-3 px-4 text-sm text-stone-600",
                            ),
                            rx.el.td(
                                customer["address"],
                                class_name="py-3 px-4 text-sm text-stone-600",
                            ),
                            rx.el.td(
                                rx.el.div(
                                    rx.el.button(
                                        rx.icon("eye", class_name="h-4 w-4"),
                                        class_name="p-2 rounded-md hover:bg-stone-200/50 text-stone-600 hover:text-stone-900 transition-colors",
                                    ),
                                    rx.el.button(
                                        rx.icon("pencil", class_name="h-4 w-4"),
                                        class_name="p-2 rounded-md hover:bg-stone-200/50 text-stone-600 hover:text-stone-900 transition-colors",
                                    ),
                                    rx.el.button(
                                        rx.icon("trash-2", class_name="h-4 w-4"),
                                        class_name="p-2 rounded-md hover:bg-red-100 text-red-600 hover:text-red-800 transition-colors",
                                    ),
                                    class_name="flex items-center justify-center gap-2",
                                ),
                                class_name="py-3 px-4",
                            ),
                            class_name="border-b border-stone-200/60 hover:bg-yellow-50/50 transition-colors",
                        ),
                    )
                ),
                class_name="w-full text-sm",
            ),
            class_name="rounded-xl shadow-md border border-stone-200/80 bg-white/60 overflow-hidden",
        ),
        class_name="p-6 fade-in-animation",
    )


def reports_view() -> rx.Component:
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
        class_name="p-6 fade-in-animation",
    )


def dashboard_page() -> rx.Component:
    return rx.el.div(
        rx.match(
            DashboardState.active_view,
            ("Dashboard", dashboard_view()),
            ("Tickets", tickets_view()),
            ("Umrah Packages", umrah_packages_view()),
            ("Visa Mgmt", visa_mgmt_view()),
            ("Customers", customers_view()),
            ("Reports", reports_view()),
            dashboard_view(),
        ),
        class_name="flex-1 p-4 sm:px-6 sm:py-0",
    )