"""Api and Utilities"""
import httplib2
import urllib


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

    def get(self, endpoint, url_data=None, parameters=None):
        """Returns the response and body for a get request
            endpoints = 'users'  # resource to access
            url_data = {}, ()  # Used to modularize endpoints, see __init__
            parameters = {}, ((),()) # URL parameters: google.com?q=a&f=b
        """
        return self.request_handler.request(
            self._url(endpoint, url_data, parameters),
            method=Api._method['get'],
        )

    def post(self, endpoint, data, url_data=None, parameters=None):
        """Returns the response and body for a post request
            endpoints = 'users'  # resource to access
            data = {'username': 'blah, 'password': blah}  # POST body
            url_data = {}, ()  # Used to modularize endpoints, see __init__
            parameters = {}, ((),()) # URL paramters, ex: google.com?q=a&f=b
        """
        return self.request_handler.request(
            self._url(endpoint, url_data, parameters),
            method=Api._method['post'],
            body=urllib.urlencode(data)
        )

    def put(self, endpoint, data, url_data=None, parameters=None):
        """Returns the response and body for a put request
            endpoints = 'users'  # resource to access
            data = {'username': 'blah, 'password': blah}  # PUT body
            url_data = {}, ()  # Used to modularize endpoints, see __init__
            parameters = {}, ((),()) # URL paramters, ex: google.com?q=a&f=b
        """
        return self.request_handler.request(
            self._url(endpoint, url_data, parameters),
            method=Api._method['put'],
            body=urllib.urlencode(data)

        )

    def delete(self, endpoint, data, url_data=None, parameters=None):
        """Returns the response and body for a delete request
            endpoints = 'users'  # resource to access
            data = {'username': 'blah, 'password': blah}  # DELETE body
            url_data = {}, ()  # Used to modularize endpoints, see __init__
            parameters = {}, ((),()) # URL paramters, ex: google.com?q=a&f=b
        """
        return self.request_handler.request(
            self._url(endpoint, url_data, parameters),
            method=Api._method['delete'],
            body=urllib.urlencode(data)
        )

    def head(self, endpoint, url_data=None, parameters=None):
        """Returns the response and body for a head request
            endpoints = 'users'  # resource to access
            url_data = {}, ()  # Used to modularize endpoints, see __init__
            parameters = {}, ((),()) # URL paramters, ex: google.com?q=a&f=b
        """
        return self.request_handler.request(
            self._url(endpoint, url_data, parameters),
            method=Api._method['head']
        )

    def _url(self, endpoint, url_data=None, parameters=None):
        """Generate URL on the modularized endpoints and url parameters"""
        try:
            url = '%s/%s' % (self.base_url, self.endpoints[endpoint])
        except KeyError:
            raise EndPointDoesNotExist(endpoint)
        if url_data:
            url = url % url_data
        if parameters:
            # url = url?key=value&key=value&key=value...
            url = '%s?%s' % (url, urllib.urlencode(parameters, True))
        return url

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

