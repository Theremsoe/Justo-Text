from orator.migrations import Migration


class CreateTargetTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("TARGET") as table:
            table.big_increments("id")
            table.string("name")
            table.string("last_name").nullable()
            table.string("aka").nullable()
            table.date("born_date").nullable()
            table.timestamps()
            table.soft_deletes()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("TARGET")
