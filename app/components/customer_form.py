import reflex as rx
from app.states.dashboard_state import DashboardState


def form_field(label: str, input_component: rx.Component) -> rx.Component:
    return rx.el.div(
        rx.el.label(label, class_name="block text-sm font-medium text-stone-700 mb-1"),
        input_component,
        class_name="mb-4",
    )


def customer_form() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.content(
            rx.dialog.title(
                rx.cond(
                    DashboardState.is_edit_mode, "Edit Customer", "Add New Customer"
                )
            ),
            rx.el.form(
                form_field(
                    "Full Name",
                    rx.el.input(
                        name="name",
                        default_value=DashboardState.current_item["name"],
                        class_name="w-full rounded-lg border-stone-300",
                    ),
                ),
                form_field(
                    "Address",
                    rx.el.input(
                        name="address",
                        default_value=DashboardState.current_item["address"],
                        class_name="w-full rounded-lg border-stone-300",
                    ),
                ),
                rx.el.div(
                    form_field(
                        "Email",
                        rx.el.input(
                            name="email",
                            type="email",
                            default_value=DashboardState.current_item["email"],
                            class_name="w-full rounded-lg border-stone-300",
                        ),
                    ),
                    form_field(
                        "Phone",
                        rx.el.input(
                            name="phone",
                            type="tel",
                            default_value=DashboardState.current_item["phone"],
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
        open=DashboardState.show_form & (DashboardState.active_view == "Customers"),
    )