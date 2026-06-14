from importlib import import_module

domain = import_module("exercises.domain_modeling.01_domain_model")


def test_can_add_user_requires_active_and_available_seat() -> None:
    sub = domain.Subscription("city-001", "standard", 3, True)

    assert domain.can_add_user(sub, 2) is True
    assert domain.can_add_user(sub, 3) is False
    assert domain.can_add_user(domain.Subscription("city-001", "standard", 3, False), 1) is False


def test_seats_by_municipality_only_counts_active_contracts() -> None:
    subscriptions = [
        domain.Subscription("city-001", "standard", 3, True),
        domain.Subscription("city-001", "trial", 2, False),
        domain.Subscription("city-002", "pro", 10, True),
    ]

    assert domain.seats_by_municipality(subscriptions) == {"city-001": 3, "city-002": 10}
