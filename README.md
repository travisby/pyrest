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

Style/Commiting Guide
====================
- Commit early, commit often.
- PEP8
- At the top of any scope, initialize and define any methods you will use inside it.  For objects, use None.  For primitives, use the most empty value (False, 0, '', etc.)
    - Two spaces, and then a comment to describe what it does
    - BEWARE, dictionaries (and most likely many others collections!) are objects, and do not get re-instantiated between object instantiation.  Make sure in __init__() you re-set them.
- Run linters
    - pep8
    - pylint
    - pyflakes
    - pychecker
- Code Coverage
    - Use coverage to test our code!  100% coverage is a nice rule of thumb.
        - coverage run --omit=tests.py --branch tests.py

Licensing
=========
The code in this repository is underneath the GPLv3 license

