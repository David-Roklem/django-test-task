from django.test import Client


class TestViews:

    def test_index_get(self):
        c = Client()
        response_get = c.get('')
        assert response_get.status_code == 200

    def test_index_post(self):
        c = Client()
        response_post = c.post('')
        assert response_post.status_code == 200
