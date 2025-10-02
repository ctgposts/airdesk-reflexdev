import reflex as rx
from app.states.dashboard_state import DashboardState


def delete_alert() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(rx.el.div()),
        rx.dialog.content(
            rx.dialog.title("Confirm Deletion"),
            rx.dialog.description(
                "Are you sure you want to delete this item? This action cannot be undone."
            ),
            rx.el.div(
                rx.dialog.close(
                    rx.el.button(
                        "Cancel",
                        on_click=DashboardState.close_delete_alert,
                        class_name="px-4 py-2 rounded-md bg-gray-200 text-gray-800 hover:bg-gray-300",
                        margin_top="1rem",
                        margin_right="1rem",
                    )
                ),
                rx.dialog.close(
                    rx.el.button(
                        "Delete",
                        on_click=DashboardState.confirm_delete,
                        class_name="px-4 py-2 rounded-md bg-red-500 text-white hover:bg-red-600",
                    )
                ),
                class_name="flex justify-end mt-4",
            ),
            style={"max_width": "450px"},
        ),
        open=DashboardState.show_delete_alert,
    )