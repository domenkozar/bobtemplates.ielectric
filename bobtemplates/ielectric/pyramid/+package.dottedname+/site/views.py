from pyramid.view import view_config


@view_config(route_name="home", renderer='index.jinja2')
def index(request):
    return {}
