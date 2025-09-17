import pytest

# python -m pytest  --project=terminal --locale=en
def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://httpbin.org/",
        help="This is request url"
    )
    parser.addoption(
        "--locale",
        action="store",
        default="en",
        help="Locale to run tests in (e.g. en, ru).",
    )
    parser.addoption(
        "--project",
        action="append",
        default=[],
    )

@pytest.fixture(scope="session")
def locale(pytestconfig):
    return pytestconfig.getoption("--locale") or os.getenv("LOCALE")


@pytest.fixture(scope="session")
def project(pytestconfig):
    project_option = pytestconfig.getoption("--project")
    return (project_option[0] if project_option else None) or os.getenv("PROJECT")


@pytest.fixture
def base_url(request):
    print(request.config.getoption("--url"))