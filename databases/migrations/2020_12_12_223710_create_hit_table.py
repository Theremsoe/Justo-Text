from orator.migrations import Migration


class CreateHitTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("HIT") as table:
            table.big_increments("id")
            table.big_integer("user_id").unsigned()
            table.big_integer("assigned_by_id").unsigned()
            table.big_integer("hit_status_id").unsigned()
            table.big_integer("target_id").unsigned()
            table.datetime("stared_at")
            table.datetime("expires_at")
            table.timestamps()
            table.soft_deletes()
            table.foreign("user_id").references("id").on("USER")
            table.foreign("assigned_by_id").references("id").on("USER")
            table.foreign("hit_status_id").references("id").on("HIT_STATUS")
            table.foreign("target_id").references("id").on("TARGET")

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("HIT")
