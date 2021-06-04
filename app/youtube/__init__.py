BASE_ROUTE = "youtube"


def register_routes(api, app, root="api"):
    from .search.controller import api as Video_api

    api.add_namespace(Video_api, path=f"/{root}/{BASE_ROUTE}/Video")