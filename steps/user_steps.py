import requests


class UserSteps():
    def get_all_users(self, url, users):
        response = requests.get(url + users)

        return response

    def get_user_data(self, url, user, id):
        response = requests.get(url + user + id)

        return response

    def delete_user(self, url, user, id):
        response = requests.delete(url + user + id)

        return response
