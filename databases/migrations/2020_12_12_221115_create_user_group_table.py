from orator.migrations import Migration


class CreateUserGroupTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("USER_GROUP") as table:
            table.big_increments("id")
            table.string("slug").unique()
            table.string("name")
            table.text("details").nullable()
            table.timestamps()
            table.soft_deletes()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("USER_GROUP")
