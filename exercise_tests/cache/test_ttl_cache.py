from importlib import import_module

target = import_module("exercises.cache.01_ttl_cache")


def test_ttl_cache() -> None:
    assert target.build_cache_key("user", ["1", "profile"]) == "user:1:profile"
    cache = {}
    target.set_cached(cache, "k", "v", now=10, ttl=5)
    assert target.get_cached(cache, "k", now=12) == "v"
    assert target.get_cached(cache, "k", now=16) is None

