import pytest

from steps.user_steps import UserSteps


@pytest.fixture(scope="session")
def user_steps():
    return UserSteps()
