import unittest
from unittest.mock import Mock, patch
from externalcalls.externalcalls import get_response, sum_and_post, post_current_datetime, post_current_datetime


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
        with unittest.mock.patch("externalcalls.externalcalls.requests.post", mock_post):
            resultado = sum_and_post(2, 3)

        # Verificamos que la función se comporte como esperamos
        self.assertEqual(resultado, {"resultado": "datos simulados"})


class TestPostCurrentDatetime(unittest.TestCase):
    def setUp(self):
        # setUP se ejecuta antes de cada test y nos permite preparar el entorno
        # añadiendo atributos que utilizaremos de manera repetida en los tests
        self.mock_response_value = {"resultado": "datos simulados"}
    
    # Otra manera de crear mocks es usando el decorador 'patch'
    # Podemos mockear más de una función o clase a la vez
    @patch("externalcalls.externalcalls.requests.post")
    @patch("externalcalls.externalcalls.datetime")
    def test_post_current_datetime(self, mock_datetime, mock_post):
        # Creamos un mock para la función 'requests.post'
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = self.mock_response_value

        # Creamos un mock para la clase 'datetime', que siempre devuelva el timestamp 0.0
        mock_datetime.now.return_value.timestamp.return_value = 0.0

        # Usamos el mock en lugar de 'requests.post' durante la prueba
        resultado = post_current_datetime()

        # Verificamos que la función se comporte como esperamos
        self.assertEqual(resultado, {"resultado": "datos simulados", "datetime": 0.0})
