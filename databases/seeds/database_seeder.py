"""Base Database Seeder Module."""

from orator.seeds import Seeder
from .user_table_seeder import UserTableSeeder
from .user_status_table_seeder import UserStatusTableSeeder
from .user_group_table_seeder import UserGroupTableSeeder
from .hit_status_table_seeder import HitStatusTableSeeder


class DatabaseSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        self.call(UserStatusTableSeeder)
        self.call(UserTableSeeder)
        self.call(UserGroupTableSeeder)
        self.call(HitStatusTableSeeder)
