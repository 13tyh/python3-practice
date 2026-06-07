from importlib import import_module

target = import_module("exercises.basics.29_dataclass_deep")


def test_dataclass_deep_tasks() -> None:
    address = target.Address("Tokyo", "100-0001")
    customer = target.Customer("c1", "Aki", address)
    assert target.customer_label(customer) == "c1:Aki@Tokyo"
    target.add_tag(customer, "vip")
    assert customer.tags == ["vip"]
    moved = target.move_customer(customer, target.Address("Osaka", "530-0001"))
    assert moved.address.city == "Osaka"
    assert customer.address.city == "Tokyo"

