import json

class ListMixin:
    def list(self, page=None):
        url = self.generate_url(page=page)
        return self.session.get(url)


class CreateMixin:
    def create(self, data):
        url = self.generate_url()
        return self.session.put(url, data=json.dumps(data))


class RetrieveMixin:
    def retrieve(self, pk):
        url = self.generate_url(obj_pk=pk)
        return self.session.get(url)


class UpdateMixin:
    def update(self, pk, updated_data):
        url = self.generate_url(obj_pk=pk)
        return self.session.post(url, data=json.dumps(updated_data))


class DeleteMixin:
    def delete(self, pk):
        url = self.generate_url(obj_pk=pk)
        return self.session.delete(url)