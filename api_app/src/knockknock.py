import falcon


class Ping(object):
    def __init__(self):
        pass

    def on_get(self, req, resp):
        resp.content_type = falcon.MEDIA_TEXT
        resp.text = "Who's there?"

        resp.status = falcon.HTTP_200
