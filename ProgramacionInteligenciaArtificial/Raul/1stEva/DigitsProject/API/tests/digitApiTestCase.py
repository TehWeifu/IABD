import io
import json
import unittest
import os

from ..app import app


class FlaskApiTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_health_check(self):
        response = self.app.get('/hc')
        payload = json.loads(response.data.decode('utf-8'))

        self.assertEqual(response.status_code, 200)
        self.assertIn('date', payload)
        self.assertIn('uptime', payload)

    def test_predict_without_image(self):
        response = self.app.post('/predict')
        data = json.loads(response.data.decode('utf-8'))

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['msg'], "The image (parameter 'digit') is missing.")

    def test_predict_with_invalid_extension(self):
        # This test needs a mock image with an invalid extension
        response = self.app.post('/predict', data={'digit': (io.BytesIO(b"fake_image_data"), 'test.txt')})
        data = json.loads(response.data.decode('utf-8'))

        self.assertEqual(response.status_code, 415)
        self.assertIn("the image must have a", data['msg'].lower())

    def test_upload_file(self):
        file_path = 'API/tests/datasetDigits/0.png'
        self.assertTrue(os.path.exists(file_path))

        with open(file_path, 'rb') as file:
            data = {
                'digit': (file, os.path.basename(file_path))
            }
            response = self.app.post('/predict', data=data, content_type='multipart/form-data')
            payload = json.loads(response.data.decode('utf-8'))

            self.assertEqual(response.status_code, 200)

            self.assertIn('digit', payload)
            self.assertIn('score', payload)


if __name__ == '__main__':
    unittest.main()
