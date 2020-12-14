"""User Table Seeder.

You can run this seeder in order to generate users.

    - Each time it is ran it will generate 50 random users.
    - All users have the password of 'secret'.
    - You can run the seeder by running: craft seed:run.
"""

from orator.seeds import Seeder

from app.models.User import User
from app.models.UserStatus import UserStatus
from config.factories import factory


class UserTableSeeder(Seeder):
    def run(self):
        """
        Run the database seeds.
        """
        status: UserStatus = UserStatus.where("slug", "active").first_or_fail()

        status.users().save_many(
            [
                User(
                    name="John",
                    last_name="Cairncross",
                    username="root",
                    email="hitman_root@secret.com",
                    password="secret",
                ),
                User(
                    name="Bruce",
                    last_name="Lockhart",
                    username="bruce_lockhart",
                    email="hitman_a.1@secret.com",
                    password="secret",
                ),
                User(
                    name="Kim",
                    last_name="Philby",
                    username="kim_philby",
                    email="hitman_b.1@secret.com",
                    password="secret",
                ),
                User(
                    name="Donald",
                    last_name="Maclean",
                    username="donald_maclean",
                    email="hitman_a@secret.com",
                    password="secret",
                ),
                User(
                    name="Guy",
                    last_name="Burgess",
                    username="guy_burgess",
                    email="hitman_b@secret.com",
                    password="secret",
                ),
            ]
        )
