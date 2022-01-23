from pytest_bdd import given, scenario, then, when


@scenario("features/dummy.feature", "Dummy test")
def dummy_scenario():
    return True


@given("write given statement here")
def dummy_given():
    return True


@when("write when statment here")
def dummy_when():
    return True


@then("write then statement here")
def dummy_then():
    assert True
