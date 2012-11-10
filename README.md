pyrest
======

pyrest is a small RESTFul API Wrapper for python.  It allows you to rapidly
develop your own API Wrapper for your specific application, without worrying
about the HTTP Requests on their own.

Code Examples
-------------
This would be a basic GET request
````
from pyrest.api import Api


stack = Api('http://api.stackexchange.com/2.1')  # Notice no trailing / !
stack.update_endpoints(
    {
        'ans': 'answers'
    }
)

print(
    stack.get(
        endpoint = 'ans',
        parameters = (('site', 'stackoverflow'), ('order', 'desc'))
    )
)
````

Here we show off some of our fancy url modularization:
````
stack = Api('http://api.stackexchange.com/2.1')  # Notice no trailing / !
stack.update_endpoints(
    {
        'comments': 'posts/%(id)s/comments'
    }
)
print(
    stack.get(
        endpoint = 'comments',
        parameters = (('site', 'stackoverflow'), ('order', 'desc')),
        url_data = {'id': '11867143'}
    )
)
````