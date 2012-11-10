"""Api and Utilities"""
import httplib2


class Api():
    """Api Object"""

    base_url = ''  # Prefixed before every URL.  EX: api.website.url/v2
    endpoints = None  # Dictionary holding all the options
    request_handler = None  # httplib2-esque

    # This is how we handle our different types of requests...
    _method = {
        'get': 'GET',
        'post': 'POST',
        'put': 'PUT',
        'delete': 'DELETE',
        'head': 'HEAD'
    }

    def __init__(self, base_url, username='', password='', oauth_client=None):
        """Grabs everything we need to connect to a REST API
            base_url: 'http://google.com'  -- no trailing slashes
            username = 'travisby@gmail.com'
            password = 'helloworld'
            oauth_client = oauth2.client()
        """
        self.base_url = base_url
        self.endpoints = {}
        if oauth_client:
            self.request_handler = oauth_client
        else:
            self.request_handler = Api._httplib2_init(username, password)

    def update_endpoints(self, endpoints):
        """"
        Adds to the endpoints collection
            endpoints = {
                'get_users': 'users',
                'classes': 'crazyURL/withExtraStuff',
                'get_user': 'user/%(id)s'  # requires url_data
                'get_me': 'user/3'  # Don't be afraid to hard code!
            }
        """
        self.endpoints.update(endpoints)

    def clear_endpoints(self):
        """Clears all stored endpoints"""
        self.endpoints = {}

    @staticmethod
    def _httplib2_init(username, password):
        """Used to instantiate a regular HTTP request object"""
        obj = httplib2.Http()
        if username and password:
            obj.add_credentials(username, password)
        return obj


class EndPointDoesNotExist(Exception):
    """Raised when the endpoint could not be found"""
    pass

