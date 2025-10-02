import reflex as rx
from typing import TypedDict, Literal

TicketStatus = Literal["Purchased", "Available", "Booked", "Sold", "Cancelled"]
TicketType = Literal["Package", "Non-Package"]
VisaStatus = Literal["Pending", "Approved", "Rejected", "In Process"]


class Ticket(TypedDict):
    id: int
    pnr: str
    type: TicketType
    status: TicketStatus
    customer_name: str
    details: str
    price: float
    purchase_date: str


class UmrahPackage(TypedDict):
    id: int
    name: str
    duration: int
    price: float
    inclusions: str
    is_active: bool


class Customer(TypedDict):
    id: int
    name: str
    email: str
    phone: str
    address: str


class VisaApplication(TypedDict):
    id: int
    customer_name: str
    country: str
    status: VisaStatus
    submission_date: str


class DashboardState(rx.State):
    active_view: str = "Dashboard"
    tickets: list[Ticket] = [
        {
            "id": 1,
            "pnr": "LUXE-786A",
            "type": "Package",
            "status": "Sold",
            "customer_name": "John Doe",
            "details": "Jeddah - Madinah, 14 days",
            "price": 2500.0,
            "purchase_date": "2024-05-10",
        },
        {
            "id": 2,
            "pnr": "LUXE-991B",
            "type": "Non-Package",
            "status": "Available",
            "customer_name": "",
            "details": "Dubai, One-way",
            "price": 450.0,
            "purchase_date": "2024-05-15",
        },
        {
            "id": 3,
            "pnr": "LUXE-452C",
            "type": "Package",
            "status": "Booked",
            "customer_name": "Jane Smith",
            "details": "Makkah - Madinah, 10 days",
            "price": 1800.0,
            "purchase_date": "2024-05-20",
        },
        {
            "id": 4,
            "pnr": "LUXE-333D",
            "type": "Non-Package",
            "status": "Cancelled",
            "customer_name": "Peter Jones",
            "details": "Istanbul, Round-trip",
            "price": 750.0,
            "purchase_date": "2024-04-22",
        },
    ]
    umrah_packages: list[UmrahPackage] = [
        {
            "id": 1,
            "name": "14-Day Executive Umrah",
            "duration": 14,
            "price": 2500.0,
            "inclusions": "5-star hotels, VIP transport, Guided Ziyarat",
            "is_active": True,
        },
        {
            "id": 2,
            "name": "10-Day Economy Umrah",
            "duration": 10,
            "price": 1500.0,
            "inclusions": "4-star hotels, Standard transport",
            "is_active": True,
        },
        {
            "id": 3,
            "name": "Ramadan Special",
            "duration": 20,
            "price": 3500.0,
            "inclusions": "Close to Haram hotels, Iftar/Suhoor",
            "is_active": False,
        },
    ]
    customers: list[Customer] = [
        {
            "id": 1,
            "name": "John Doe",
            "email": "john.doe@email.com",
            "phone": "123-456-7890",
            "address": "123 Main St, Anytown",
        },
        {
            "id": 2,
            "name": "Jane Smith",
            "email": "jane.smith@email.com",
            "phone": "987-654-3210",
            "address": "456 Oak Ave, Othertown",
        },
    ]
    visa_applications: list[VisaApplication] = [
        {
            "id": 1,
            "customer_name": "John Doe",
            "country": "Saudi Arabia",
            "status": "Approved",
            "submission_date": "2024-05-01",
        },
        {
            "id": 2,
            "customer_name": "Jane Smith",
            "country": "Saudi Arabia",
            "status": "In Process",
            "submission_date": "2024-05-18",
        },
    ]

    @rx.event
    def set_active_view(self, view: str):
        self.active_view = view

    @rx.var
    def total_sales(self) -> float:
        return sum((t["price"] for t in self.tickets if t["status"] == "Sold"))

    @rx.var
    def tickets_sold(self) -> int:
        return sum((1 for t in self.tickets if t["status"] == "Sold"))

    @rx.var
    def active_packages(self) -> int:
        return sum((1 for pkg in self.umrah_packages if pkg["is_active"]))

    @rx.var
    def pending_visas(self) -> int:
        return sum(
            (
                1
                for visa in self.visa_applications
                if visa["status"] in ["Pending", "In Process"]
            )
        )

    @rx.var
    def total_tickets(self) -> int:
        return len(self.tickets)

    @rx.var
    def available_tickets(self) -> int:
        return sum((1 for t in self.tickets if t["status"] == "Available"))

    @rx.var
    def booked_tickets(self) -> int:
        return sum((1 for t in self.tickets if t["status"] == "Booked"))

    @rx.var
    def total_customers(self) -> int:
        return len(self.customers)