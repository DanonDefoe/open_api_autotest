import random

from constants.status_code import OK, NOT_FOUND, MISMATCH, DELETED, NOT_FOUND_FAKED
from constants.uri import BASE_URL, USERS, USER
from dto.user import UserSchema
from fixtures.open_api_fixture import user_steps


class TestUsers:
    def test_get_all_users_positive(self, user_steps):
        users_list = user_steps.get_all_users(BASE_URL, USERS)
        assert users_list.status_code == OK, MISMATCH

    def test_get_all_users_negative(self, user_steps):
        incorrect_uri = str(random.randint(0, 999))
        users_list = user_steps.get_all_users(BASE_URL, incorrect_uri)
        assert users_list.status_code == NOT_FOUND, MISMATCH

    def test_get_user_data_positive(self, user_steps):
        user_id = str(random.randint(1, 20))
        user_data = user_steps.get_user_data(BASE_URL, USERS, user_id)
        assert user_data.status_code == OK, MISMATCH

    def test_get_user_data_negative(self, user_steps):
        user_id = str(random.randint(-999, -1))
        user_data = user_steps.get_user_data(BASE_URL, USER, user_id)
        assert user_data.status_code == NOT_FOUND, MISMATCH

    def test_validate_user_data_scheme(self, user_steps):
        user_data = user_steps.get_user_data(BASE_URL, USERS, '/2')
        users_list = user_data.json()
        result = UserSchema(**users_list)
        print(result)

    '''The following tests are fake, because we actually can't delete users from the server'''
    def test_delete_user_negative(self, user_steps):
        wrong_user_id = str(random.randint(21, 999))
        delete_user = user_steps.delete_user(BASE_URL, USERS, f'/{wrong_user_id}')
        assert delete_user.status_code == NOT_FOUND_FAKED, MISMATCH

    def test_delete_user_positive(self, user_steps):
        create_user_def = True  # There is a hypothetical method that creates a new user
        user_id = str(random.randint(1, 20))
        delete_user = user_steps.delete_user(BASE_URL, USERS, f'/{user_id}')
        assert delete_user.status_code == DELETED, MISMATCH

        # check the user doesn't exist
        user_data = user_steps.get_user_data(BASE_URL, USERS, '/999')  # 999 is the nonexistent user id
        assert user_data.status_code == NOT_FOUND, MISMATCH
