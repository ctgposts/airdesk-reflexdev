import reflex as rx
from app.states.dashboard_state import DashboardState
from app.components.customer_form import customer_form
from app.components.delete_alert import delete_alert


def customers_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h1(
                "Customer Management", class_name="text-3xl font-bold text-stone-800"
            ),
            rx.el.button(
                rx.icon("plus", class_name="h-4 w-4 mr-2"),
                "Add New Customer",
                on_click=lambda: DashboardState.open_form(is_edit=False),
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
                                        rx.icon("pencil", class_name="h-4 w-4"),
                                        on_click=lambda: DashboardState.open_form(
                                            customer, is_edit=True
                                        ),
                                        class_name="p-2 rounded-md hover:bg-stone-200/50 text-stone-600 hover:text-stone-900 transition-colors",
                                    ),
                                    rx.el.button(
                                        rx.icon("trash-2", class_name="h-4 w-4"),
                                        on_click=lambda: DashboardState.open_delete_alert(
                                            "Customers", customer["id"]
                                        ),
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
        customer_form(),
        delete_alert(),
        class_name="fade-in-animation",
    )