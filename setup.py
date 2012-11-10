"""
Used for Distribution

    This file is part of pyrest.

    pyrest is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, version 3 of the License.

    pyrest is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with pyrest.  If not, see <http://www.gnu.org/licenses/>.
"""

from distutils.core import setup

setup(
    name='pyrest',
    version='0.5.0',
    author='Travis Beatty',
    author_email='travisby@gmail.com',
    maintainer='Travis Beatty',
    maintainer_email='travisby@gmail.com',
    url='http://github.com/travisby/pyrest',
    description='Small RESTFul API Wrapper for python',
    long_description=(
        """
        RESTFul API Wrapper to sit between your API Resources
        and your own package API Wrapper
        """
    ),
    download_url='http://github.com/travisby/pyrest/archive/v0.5.0.zip',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP'
    ],
    py_modules=['api'],
)
