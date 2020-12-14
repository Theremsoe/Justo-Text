from orator.seeds import Seeder
from app.models.HitStatus import HitStatus


class HitStatusTableSeeder(Seeder):
    def run(self):
        """
        Run the database seeds.
        """
        HitStatus.create(slug="open", name="Open", details="Work in progress")
        HitStatus.create(
            slug="wait", name="Wait", details="Work waiting (paused by some order)"
        )
        HitStatus.create(
            slug="closed", name="Closed", details="Work Closed (by not rejected)"
        )
        HitStatus.create(
            slug="successful", name="Successful", details="Work successful"
        )
        HitStatus.create(slug="rejected", name="Rejected", details="Work Rejected")
        HitStatus.create(
            slug="fail", name="Failed", details="Work Fialed. Target(s) lives"
        )
