from orator.migrations import Migration


class CreateUsersTable(Migration):
    def up(self):
        """Run the migrations."""
        with self.schema.create("USER") as table:
            table.big_increments("id")
            table.big_integer("user_status_id").unsigned()
            table.string("name")
            table.string("last_name").nullable()
            table.string("email").unique()
            table.string("username").unique()
            table.string("password")
            table.timestamps()
            table.soft_deletes()
            table.foreign("user_status_id").references("id").on("USER_STATUS")

    def down(self):
        """Revert the migrations."""
        self.schema.drop("USER")
