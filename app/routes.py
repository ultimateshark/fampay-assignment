
def register_routes(api, app, root="api"):
    from app.youtube import register_routes as attach_youtube
    attach_youtube(api, app)