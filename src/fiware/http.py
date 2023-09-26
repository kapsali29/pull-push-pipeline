import abc

import requests


class AbstractClient(abc.ABC):
    """Abstract operations of HTTP client"""

    def __init__(self):
        pass

    def list(self, url, headers, **kwargs):
        """Fetch the list of entities"""
        pass

    def get(self, url, headers, **kwargs):
        """Fetch a list of entities or an entity"""
        pass

    def post(self, url, headers, payload, **kwargs):
        """Insert an entity"""
        pass

    def put(self, url, headers, payload, **kwargs):
        """Update partially an entity"""
        pass


class Client(AbstractClient):
    """The HTTP Client class

    Attributes:
        verify_ssl_cert (bool): True to verify the SSL cert. False otherwise.

    Methods:
        list(url, headers): get a list of entities
        get(url, headers): fetch an entity
        post(url, headers, payload): insert an entity
        delete(url, headers): delete an entity
    """

    def __init__(self, verify_ssl_cert=False):
        self.verify_ssl_cert = verify_ssl_cert
        super(Client, self).__init__()

    def list(self, url, headers=None, **kwargs):
        """Fetch a list of entities (a collection).

        Args:
            url (str): the endpoint of the web service
            headers (dict): the required HTTP headers, e.g., Accept: application/json
            kwargs (dict, optional): Additional arguments will be passed to the request.

        Returns:
            obj: a requests object
        """
        query_params = kwargs.get('query_params', None)
        response = requests.get(url, headers=headers, params=query_params,
                                verify=self.verify_ssl_cert)
        return response

    def get(self, url, headers=None, **kwargs):
        """Fetch an entity.

        Args:
            url (str): the endpoint of the web service
            headers (dict): the required HTTP headers, e.g., Accept: application/json
            kwargs (dict, optional): Additional arguments will be passed to the request.

        Returns:
            obj: a requests object
        """
        query_params = kwargs.get('query_params', None)
        response = requests.get(url, headers=headers, params=query_params,
                                verify=self.verify_ssl_cert)
        return response

    def post(self, url, headers=None, payload=None, **kwargs):
        """Insert an entity.

        Args:
            url (str): the endpoint of the web service
            headers (dict): the required HTTP headers, e.g., Accept: application/json
            payload (dict): data that will be encoded as JSON and passed in the request
            kwargs (dict, optional): Additional arguments will be passed to the request.

        Returns:
            obj: a requests object
        """
        query_params = kwargs.get('query_params', None)
        response = requests.post(url, data=payload, headers=headers, params=query_params,
                                 verify=self.verify_ssl_cert)
        return response

    def delete(self, url, headers=None, **kwargs):
        """Delete an entity.

        Args:
            url (str): the endpoint of the web service
            headers (dict): the required HTTP headers, e.g., Accept: application/json
            kwargs (dict, optional): Additional arguments will be passed to the request.

        Returns:
            obj: a requests object
        """
        query_params = kwargs.get('query_params', None)
        response = requests.delete(url=url, headers=headers, params=query_params,
                                   verify=self.verify_ssl_cert)
        return response
