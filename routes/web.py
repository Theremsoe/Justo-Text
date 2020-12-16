"""Web Routes."""

from masonite.routes import Get, Post, Patch, Delete, RouteGroup

ROUTES = [
    RouteGroup(
        [
            RouteGroup(
                [
                    RouteGroup(
                        [
                            Get("/", "ListController@index").name("list"),
                            Get("/@id:int", "ReadController@index").name("read"),
                            Post("/", "CreateController@index").name("create"),
                            Patch("/@id:int", "UpdateController@index").name("update"),
                            Delete("/@id:int", "DeleteController@index").name("delete"),
                        ],
                        namespace="user",
                        name="user.",
                        prefix="user",
                    ),
                    RouteGroup(
                        [
                            Get("/", "ListController@index").name("list"),
                            Get("/@id:int", "ReadController@index").name("read"),
                        ],
                        namespace="userGroup",
                        name="user-group.",
                        prefix="user-group",
                    ),
                    RouteGroup(
                        [
                            Get("/", "ListController@index").name("list"),
                            Get("/@id:int", "ReadController@index").name("read"),
                        ],
                        namespace="userStatus",
                        name="user-status.",
                        prefix="user-status",
                    ),
                    RouteGroup(
                        [
                            Get("/", "ListController@index").name("list"),
                            Get("/@id:int", "ReadController@index").name("read"),
                            Post("/", "CreateController@index").name("create"),
                            Patch("/@id:int", "UpdateController@index").name("update"),
                            Delete("/@id:int", "DeleteController@index").name("delete"),
                        ],
                        namespace="target",
                        name="target.",
                        prefix="target",
                    ),
                    RouteGroup(
                        [
                            Get("/", "ListController@index").name("list"),
                            Get("/@id:int", "ReadController@index").name("read"),
                        ],
                        namespace="hitStatus",
                        name="hit-status.",
                        prefix="hit-status",
                    ),
                    RouteGroup(
                        [
                            Get("/", "ListController@index").name("list"),
                            Get("/@id:int", "ReadController@index").name("read"),
                            Post("/", "CreateController@index").name("create"),
                            Patch("/@id:int", "UpdateController@index").name("update"),
                            Delete("/@id:int", "DeleteController@index").name("delete"),
                        ],
                        namespace="hit",
                        name="hit.",
                        prefix="hit",
                    ),
                ],
                middleware=["auth"],
            ),
            RouteGroup(
                [Post("/", "IssueController@index").name("issue")],
                namespace="authentication",
                name="auth.",
                prefix="auth",
            ),
        ],
        namespace="api.v1",
        name="api.v1.",
        prefix="/api/v1/",
        add_methods=["OPTIONS"],
    ),
    Get("/", "WelcomeController@show").name("welcome"),
]
