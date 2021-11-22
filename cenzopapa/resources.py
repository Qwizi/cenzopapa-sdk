from enum import Enum

from cenzopapa.decorators import check_authorization
from cenzopapa.exceptions import NotAuthorized
from cenzopapa.mixins import ListMixin, CreateMixin, RetrieveMixin
from cenzopapa.resource_client import ResourceClient


class ImageAction(str, Enum):
    FAVORITE = "favorite"
    UNVAFORITE = "unfavorite"
    LIKE = "like"
    UNLIKE = 'unlike'
    RANDOM = 'random'


class ImageResource(
    ResourceClient,
    RetrieveMixin,
    ListMixin,

):
    endpoint = "/images/"

    def random(self):
        url = self.generate_url(action=ImageAction.RANDOM.value)
        return self.session.get(url)

    def __action_mixin(self, pk, action):
        url = self.generate_url(pk=pk, action=action)
        print(url)
        response = self.session.post(url)
        response.raise_for_status()
        return response

    @check_authorization
    def favorite(self, pk):
        return self.__action_mixin(pk=pk, action=ImageAction.FAVORITE.value)

    def unfavorite(self, pk):
        return self.__action_mixin(pk=pk, action=ImageAction.UNVAFORITE.value)

    def like(self, image_pk):
        return self.__action_mixin(pk=image_pk, action=ImageAction.LIKE.value)

    def unlike(self, image_pk):
        return self.__action_mixin(pk=image_pk, action=ImageAction.UNLIKE.value)


class JWTResource(ResourceClient):
    endpoint = "/auth/jwt"

    def create(self, data):
        url = f"{self.generate_url()}/create"
        return self.session.post(url, data)

    def refresh(self, refresh_token):
        url = f"{self.generate_url()}/refresh"
        return self.session.post(url, {"refresh": refresh_token})
