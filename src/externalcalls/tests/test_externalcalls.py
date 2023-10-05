import unittest
from unittest.mock import Mock
from externalcalls.externalcalls import get_response, sum_and_post


class TestObtenerDatosDeServicioWeb(unittest.TestCase):
    def test_get_response_success(self):
        # Creamos un mock para la función 'requests.get'
        mock_get = Mock()
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"resultado": "datos simulados"}

        # Usamos el mock en lugar de 'requests.get' durante la prueba
        with unittest.mock.patch("requests.get", mock_get):
            resultado = get_response()

        # Verificamos que la función se comporte como esperamos
        self.assertEqual(resultado, {"resultado": "datos simulados"})

    def test_get_response_error(self):
        # Creamos un mock para la función 'requests.get'
        mock_get = Mock()
        mock_get.return_value.status_code = 404

        # Usamos el mock en lugar de 'requests.get' durante la prueba
        with unittest.mock.patch("requests.get", mock_get):
            resultado = get_response()

        # Verificamos que la función se comporte como esperamos
        self.assertEqual(resultado, None)


class TestSumAndPost(unittest.TestCase):
    def test_sum_and_post(self):
        # Creamos un mock para la función 'requests.post'
        mock_post = Mock()
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {"resultado": "datos simulados"}

        # Usamos el mock en lugar de 'requests.post' durante la prueba
        with unittest.mock.patch("requests.post", mock_post):
            resultado = sum_and_post(2, 3)

        # Verificamos que la función se comporte como esperamos
        self.assertEqual(resultado, {"resultado": "datos simulados"})
