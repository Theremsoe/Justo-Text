from orator.seeds import Seeder
from app.models.UserStatus import UserStatus


class UserStatusTableSeeder(Seeder):
    def run(self):
        """
        Run the database seeds.
        """
        UserStatus.create(slug="active", name="Active", details="Operative hitman")
        UserStatus.create(
            slug="suspended",
            name="Suspended",
            details="Suspended hitmen (violations agree, murders, double agents, traitor)",
        )
        UserStatus.create(
            slug="retirement",
            name="Retirement",
            details="Retirement agents",
        )
