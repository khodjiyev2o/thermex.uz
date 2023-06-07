import environ
from drf_yasg.generators import OpenAPISchemaGenerator


env = environ.Env()
DJANGO_SETTINGS_MODULE = env.str("DJANGO_SETTINGS_MODULE")


class BothHttpAndHttpsSchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        schema.schemes = ["http", "https"]
        if DJANGO_SETTINGS_MODULE == "config.settings.prod":
            schema.schemes = ["https", "http"]
        return schema
