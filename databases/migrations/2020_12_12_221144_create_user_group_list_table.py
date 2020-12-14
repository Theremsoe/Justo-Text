from orator.migrations import Migration


class CreateUserGroupListTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("USER_GROUP_LIST") as table:
            table.integer("user_id").unsigned()
            table.integer("user_group_id").unsigned()
            table.timestamps()
            table.foreign("user_id").references("id").on("USER")
            table.foreign("user_group_id").references("id").on("USER_GROUP")

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("USER_GROUP_LIST")
