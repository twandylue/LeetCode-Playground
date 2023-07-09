# ref: https://github.com/pytest-dev/pytest/issues/2393#issuecomment-452634365
def pytest_sessionfinish(session, exitstatus):
    if exitstatus == 5:  # no tests run
        session.exitstatus = 0  # Any arbitrary custom status you want to return
