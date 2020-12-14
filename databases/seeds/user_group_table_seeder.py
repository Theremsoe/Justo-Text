from orator.seeds import Seeder
from app.models.UserGroup import UserGroup
from app.models.User import User


class UserGroupTableSeeder(Seeder):
    def run(self):
        """
        Run the database seeds.
        """
        rootGroup: UserGroup = UserGroup.create(
            slug="root", name="root", details="root user", level=1
        )
        rootGroup.users().attach(User.where("username", "root").first_or_fail())

        adminGroup: UserGroup = UserGroup.create(
            slug="admin", name="admin", details="admin user", level=2
        )

        adminGroup.users().save_many(
            [
                User.where("username", "donald_maclean").first_or_fail(),
                User.where("username", "guy_burgess").first_or_fail(),
            ]
        )

        staffGroup: UserGroup = UserGroup.create(
            slug="staff", name="staff", details="staff user", level=50
        )

        staffGroup.users().save_many(
            [
                User.where("username", "bruce_lockhart").first_or_fail(),
                User.where("username", "kim_philby").first_or_fail(),
            ]
        )
