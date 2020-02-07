import hubspot.codegen.auth.oauth as oauth
import hubspot.codegen.auth.oauth.exceptions as exceptions


class Discovery:
    def default_api(self):
        configuration = oauth.Configuration()

        return oauth.DefaultApi(oauth.ApiClient(configuration))

    def exceptions(self):
        return exceptions
