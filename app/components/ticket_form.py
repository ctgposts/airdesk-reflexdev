import reflex as rx
from app.states.dashboard_state import DashboardState, TicketStatus, TicketType


def form_field(label: str, input_component: rx.Component) -> rx.Component:
    return rx.el.div(
        rx.el.label(label, class_name="block text-sm font-medium text-stone-700 mb-1"),
        input_component,
        class_name="mb-4",
    )


def ticket_form() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.content(
            rx.dialog.title(
                rx.cond(DashboardState.is_edit_mode, "Edit Ticket", "Add New Ticket")
            ),
            rx.el.form(
                form_field(
                    "Details",
                    rx.el.input(
                        name="details",
                        default_value=DashboardState.current_item["details"],
                        class_name="w-full rounded-lg border-stone-300",
                    ),
                ),
                rx.el.div(
                    form_field(
                        "Price",
                        rx.el.input(
                            name="price",
                            type="number",
                            default_value=DashboardState.current_item[
                                "price"
                            ].to_string(),
                            class_name="w-full rounded-lg border-stone-300",
                        ),
                    ),
                    form_field(
                        "Purchase Date",
                        rx.el.input(
                            name="purchase_date",
                            type="date",
                            default_value=DashboardState.current_item["purchase_date"],
                            class_name="w-full rounded-lg border-stone-300",
                        ),
                    ),
                    class_name="grid grid-cols-2 gap-4",
                ),
                rx.el.div(
                    form_field(
                        "Ticket Type",
                        rx.el.select(
                            rx.foreach(
                                TicketType.__args__,
                                lambda type_option: rx.el.option(
                                    type_option, value=type_option
                                ),
                            ),
                            name="type",
                            default_value=DashboardState.current_item["type"],
                            class_name="w-full rounded-lg border-stone-300",
                        ),
                    ),
                    form_field(
                        "Status",
                        rx.el.select(
                            rx.foreach(
                                TicketStatus.__args__,
                                lambda status_option: rx.el.option(
                                    status_option, value=status_option
                                ),
                            ),
                            name="status",
                            default_value=DashboardState.current_item["status"],
                            class_name="w-full rounded-lg border-stone-300",
                        ),
                    ),
                    class_name="grid grid-cols-2 gap-4",
                ),
                form_field(
                    "Customer Name (optional)",
                    rx.el.input(
                        name="customer_name",
                        default_value=DashboardState.current_item["customer_name"],
                        class_name="w-full rounded-lg border-stone-300",
                    ),
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
        open=DashboardState.show_form & (DashboardState.active_view == "Tickets"),
    )