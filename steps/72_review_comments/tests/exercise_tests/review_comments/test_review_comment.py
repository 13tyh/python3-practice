from importlib import import_module

target = import_module("exercises.review_comments.01_review_comment")


def test_severity_from_label() -> None:
    assert target.severity_from_label("security") == "critical"
    assert target.severity_from_label("bug") == "high"
    assert target.severity_from_label("performance") == "medium"
    assert target.severity_from_label("style") == "low"


def test_make_review_comment() -> None:
    comment = target.make_review_comment(
        "app/router.py",
        12,
        "routerがDBへ直アクセス",
        "serviceへ移す",
    )

    assert "app/router.py:12" in comment
    assert "routerがDBへ直アクセス" in comment
    assert "serviceへ移す" in comment
