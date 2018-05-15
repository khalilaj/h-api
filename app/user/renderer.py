import json
from ..core.renderer import HudumaRenderer


class AccountRenderer(HudumaRenderer):
    object_name = 'user'

    def render(self, data, media_type=None, renderer_context=None):

        if 'errors' in data:
            return super(AccountRenderer, self).render(data)

        token = data['token'] if 'token' in data else None

        if token is not None and isinstance(token, bytes):
            data['token'] = token.decode('utf-8')

        return json.dumps({self.object_name:data})
