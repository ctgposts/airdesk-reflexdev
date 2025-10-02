import reflex as rx
from app.states.auth_state import AuthState


def login_form() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(tag="gem", class_name="mx-auto h-12 w-auto text-yellow-500"),
            rx.el.h2(
                "Luxe Travel Access",
                class_name="mt-6 text-center text-2xl font-bold tracking-tight text-stone-800",
            ),
            class_name="sm:mx-auto sm:w-full sm:max-w-md",
        ),
        rx.el.div(
            rx.el.form(
                rx.el.div(
                    rx.el.label(
                        "Email address",
                        class_name="block text-sm font-semibold leading-6 text-stone-700",
                    ),
                    rx.el.div(
                        rx.el.input(
                            type="email",
                            name="email",
                            placeholder="user@luxe.travel",
                            required=True,
                            class_name="w-full rounded-lg border-0 bg-white/50 p-3 text-stone-800 shadow-sm ring-1 ring-inset ring-stone-300 placeholder:text-stone-400 focus:ring-2 focus:ring-inset focus:ring-yellow-500 transition-shadow duration-300",
                        ),
                        class_name="mt-2",
                    ),
                    class_name="space-y-1",
                ),
                rx.el.div(
                    rx.el.label(
                        "Password",
                        class_name="block text-sm font-semibold leading-6 text-stone-700",
                    ),
                    rx.el.div(
                        rx.el.input(
                            type="password",
                            name="password",
                            placeholder="••••••••",
                            required=True,
                            class_name="w-full rounded-lg border-0 bg-white/50 p-3 text-stone-800 shadow-sm ring-1 ring-inset ring-stone-300 placeholder:text-stone-400 focus:ring-2 focus:ring-inset focus:ring-yellow-500 transition-shadow duration-300",
                        ),
                        class_name="mt-2",
                    ),
                    class_name="space-y-1",
                ),
                rx.cond(
                    AuthState.error_message != "",
                    rx.el.div(
                        rx.icon("flag_triangle_right", class_name="h-4 w-4 mr-2"),
                        rx.text(AuthState.error_message),
                        class_name="flex items-center text-sm text-red-600 bg-red-100 p-2 rounded-md mt-4",
                    ),
                    None,
                ),
                rx.el.div(
                    rx.el.button(
                        "Sign in",
                        type="submit",
                        class_name="flex w-full justify-center rounded-lg bg-yellow-900/90 px-4 py-3 text-sm font-semibold leading-6 text-white shadow-md hover:bg-yellow-900 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-yellow-600 transition-all duration-300 glow-on-hover",
                    ),
                    class_name="pt-6",
                ),
                on_submit=AuthState.login,
            ),
            class_name="bg-cream-100/10 backdrop-blur-md p-8 sm:p-10 rounded-2xl shadow-2xl border border-white/20 mt-10",
        ),
        class_name="sm:mx-auto sm:w-full sm:max-w-md",
    )