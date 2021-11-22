import requests.exceptions

from cenzopapa.exceptions import NotAuthorized


def check_authorization(decorated):
    def wrapper(api, *args, **kwargs):
        try:
            return decorated(api, *args, **kwargs)
        except requests.exceptions.RequestException as e:
            print(api.__dict__)
            raise

    return wrapper

