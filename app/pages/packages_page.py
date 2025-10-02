import reflex as rx
from app.states.dashboard_state import DashboardState
from app.components.package_form import package_form
from app.components.delete_alert import delete_alert


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


def packages_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h1("Umrah Packages", class_name="text-3xl font-bold text-stone-800"),
            rx.el.button(
                rx.icon("plus", class_name="h-4 w-4 mr-2"),
                "Add New Package",
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
                                        rx.icon("pencil", class_name="h-4 w-4"),
                                        on_click=lambda: DashboardState.open_form(
                                            pkg, is_edit=True
                                        ),
                                        class_name="p-2 rounded-md hover:bg-stone-200/50 text-stone-600 hover:text-stone-900 transition-colors",
                                    ),
                                    rx.el.button(
                                        rx.icon("trash-2", class_name="h-4 w-4"),
                                        on_click=lambda: DashboardState.open_delete_alert(
                                            "Umrah Packages", pkg["id"]
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
        package_form(),
        delete_alert(),
        class_name="fade-in-animation",
    )