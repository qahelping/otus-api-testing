import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://httpbin.org/",
        help="This is request url"
    )

@pytest.fixture
def base_url(request):
    print(request.config.getoption("--url"))