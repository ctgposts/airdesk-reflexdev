import reflex as rx
from app.states.dashboard_state import DashboardState


def form_field(label: str, input_component: rx.Component) -> rx.Component:
    return rx.el.div(
        rx.el.label(label, class_name="block text-sm font-medium text-stone-700 mb-1"),
        input_component,
        class_name="mb-4",
    )


def booking_form() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.content(
            rx.dialog.title(
                rx.cond(DashboardState.is_edit_mode, "Edit Booking", "New Booking")
            ),
            rx.el.form(
                rx.el.div(
                    form_field(
                        "Ticket PNR",
                        rx.el.select(
                            rx.foreach(
                                DashboardState.tickets,
                                lambda ticket: rx.el.option(
                                    f"{ticket['pnr']} - {ticket['details']}",
                                    value=ticket["pnr"],
                                ),
                            ),
                            name="ticket_pnr",
                            default_value=DashboardState.current_item["ticket_pnr"],
                            class_name="w-full rounded-lg border-stone-300",
                        ),
                    ),
                    form_field(
                        "Customer Name",
                        rx.el.select(
                            rx.foreach(
                                DashboardState.customers,
                                lambda customer: rx.el.option(
                                    customer["name"], value=customer["name"]
                                ),
                            ),
                            name="customer_name",
                            default_value=DashboardState.current_item["customer_name"],
                            class_name="w-full rounded-lg border-stone-300",
                        ),
                    ),
                    class_name="grid grid-cols-2 gap-4",
                ),
                rx.el.div(
                    form_field(
                        "Booking Date",
                        rx.el.input(
                            name="booking_date",
                            type="date",
                            default_value=DashboardState.current_item["booking_date"],
                            class_name="w-full rounded-lg border-stone-300",
                        ),
                    ),
                    form_field(
                        "Status",
                        rx.el.select(
                            rx.el.option("Confirmed", value="Confirmed"),
                            rx.el.option("Pending", value="Pending"),
                            rx.el.option("Cancelled", value="Cancelled"),
                            name="status",
                            default_value=DashboardState.current_item["status"],
                            class_name="w-full rounded-lg border-stone-300",
                        ),
                    ),
                    class_name="grid grid-cols-2 gap-4",
                ),
                rx.el.div(
                    rx.el.button(
                        "Cancel",
                        type="button",
                        on_click=DashboardState.close_form,
                        class_name="px-4 py-2 rounded-md bg-gray-200 text-gray-800 hover:bg-gray-300",
                    ),
                    rx.el.button(
                        "Save",
                        type="submit",
                        class_name="px-4 py-2 rounded-md bg-yellow-900/90 text-white hover:bg-yellow-900",
                    ),
                    class_name="flex justify-end gap-4 mt-4",
                ),
                on_submit=DashboardState.save_item,
            ),
        ),
        open=DashboardState.show_form & (DashboardState.active_view == "Bookings"),
    )