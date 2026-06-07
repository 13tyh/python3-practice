from importlib import import_module

target = import_module("exercises.basics.14_nested")


def test_nested_tasks() -> None:
    assert target.get_city({"profile": {"city": "Tokyo"}}) == "Tokyo"
    assert target.get_city({}) is None
    orders = [{"items": [{"amount": 100}, {"amount": 200}]}, {"items": [{"amount": 50}]}]
    assert target.total_order_amount(orders) == 350
    articles = [{"tags": ["python", "api"]}, {"tags": ["python", "db"]}]
    assert target.collect_tags(articles) == ["python", "api", "db"]
    users = [{"name": "Aki", "role": "admin"}, {"name": "Ren", "role": "member"}]
    assert target.group_names_by_role(users) == {"admin": ["Aki"], "member": ["Ren"]}

