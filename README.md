
# Unit Testing en Python

## Introducción

El unit testing, o pruebas unitarias, es una práctica esencial en el desarrollo de software que permite verificar que las partes individuales de un programa funcionan como se espera. En Python, puedes realizar pruebas unitarias utilizando el módulo `unittest`, que proporciona un marco de trabajo sólido para escribir y ejecutar pruebas de manera efectiva.

**¿Por qué realizar pruebas unitarias?**

Las pruebas unitarias tienen varios beneficios clave:

1. **Detectar errores temprano:** Identificar problemas en una etapa temprana del desarrollo, cuando son más fáciles y económicos de corregir.

2. **Mantener la calidad del código:** Garantizar que el código existente siga funcionando correctamente a medida que se hacen cambios y mejoras.

3. **Facilitar la colaboración:** Las pruebas unitarias pueden ser compartidas con otros miembros del equipo, lo que facilita la colaboración y la revisión de código.

4. **Documentación viva:** Las pruebas unitarias sirven como documentación en tiempo real sobre cómo se espera que funcione cada parte del código.

**Escribir Pruebas Unitarias en Python**

Para escribir pruebas unitarias en Python, sigue estos pasos:

1. **Importa el módulo `unittest`:** Asegúrate de importar `unittest` al principio de tu archivo de prueba.

   ```python
   import unittest
   ```

2. **Crea una clase de prueba:** Define una clase que herede de `unittest.TestCase`. Cada método en esta clase será una prueba individual.

   ```python
   class MiPrueba(unittest.TestCase):
   ```

3. **Escribe pruebas:** Dentro de la clase, define métodos que comiencen con "test_" y utilicen las aserciones proporcionadas por `unittest` para verificar el comportamiento esperado de tu código.

   ```python
   def test_sum(self):
       resultado = sum(2, 3)
       self.assertEqual(resultado, 5)
   ```

4. **Ejecuta las pruebas:** Puedes ejecutar tus pruebas utilizando el módulo `unittest` desde la línea de comandos o mediante herramientas de desarrollo integradas.

    Para correr todas las pruebas en un directorio, puedes usar el siguiente comando:

    ```bash
    coverage run -m --source=. pytest
    ```

    Para correr las pruebas solo para un archivo en específico, puedes usar el siguiente comando:

    ```bash
    coverage run -m --source=. pytest ./path/to/test_file.py
    ```

5. **Interpreta los resultados:** Después de la ejecución, podrás ver si tus pruebas han pasado o han fallado. Si fallan, podrás investigar y corregir el código correspondiente. Adicionalmente, puedes generar un reporte de cobertura de código con el siguiente comando:

    ```bash 
    coverage report -m
    ```

**Ejemplo Completo**

```python
import unittest

def sum(a, b):
    return a + b

class TestSum(unittest.TestCase):
    def test_sum(self):
        resultado = sum(2, 3)
        self.assertEqual(resultado, 5)

```

Esta es una introducción básica al unit testing en Python. A medida que avances en tu desarrollo de software, te encontrarás escribiendo pruebas unitarias más complejas y utilizando características adicionales de `unittest` para abordar diferentes escenarios de prueba.


## Mocks

En las pruebas unitarias, a menudo necesitas simular o "falsificar" ciertas partes de tu código para aislar la funcionalidad que deseas probar. Los objetos que cumplen esta función se llaman "mocks". Los mocks son especialmente útiles cuando necesitas controlar el comportamiento de dependencias externas, como bases de datos, servicios web o módulos que aún no están implementados.

Python proporciona una biblioteca llamada `unittest.mock` (disponible en Python 3.3 y versiones posteriores) que facilita la creación de mocks para tus pruebas unitarias.

**¿Por qué usar Mocks?**

1. **Control de dependencias:** Los mocks te permiten controlar y predecir el comportamiento de las dependencias externas, lo que hace que tus pruebas sean más predecibles y confiables.

2. **Aislamiento de pruebas:** Al aislar las partes de tu código que deseas probar, puedes centrarte en la lógica específica que estás evaluando, sin preocuparte por el comportamiento de las dependencias.

3. **Rendimiento y eficiencia:** Evita la necesidad de interactuar con sistemas externos reales, lo que puede ser costoso en términos de tiempo y recursos en pruebas unitarias.

**Ejemplo de Uso de Mocks**

A continuación, se muestra un ejemplo de cómo usar `unittest.mock` para crear un mock y simular el comportamiento de una dependencia en una prueba unitaria:

Supongamos que tienes una función `get_response` que hace una solicitud a un servicio web y procesa los datos. Quieres probar la función sin depender de la disponibilidad real del servicio web. Aquí es donde entra en juego el uso de mocks:

```python
import unittest
from unittest.mock import Mock

# Función que obtiene datos de un servicio web y los procesa
def get_response():
    response = requests.get("https://example.com/api/data")
    if response.status_code == 200:
        return response.json()
    else:
        return None

class TestObtenerDatosDeServicioWeb(unittest.TestCase):
    def test_get_response_success(self):
        # Creamos un mock para la función 'requests.get'
        mock_get = Mock()
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"resultado": "datos simulados"}

        # Usamos el mock en lugar de 'requests.get' durante la prueba
        with unittest.mock.patch('requests.get', mock_get):
            resultado = get_response()

        # Verificamos que la función se comporte como esperamos
        self.assertEqual(resultado, {"resultado": "datos simulados"})

```

En este ejemplo, hemos creado un mock para `requests.get` utilizando `unittest.mock.patch`. Esto nos permite controlar el comportamiento de la llamada a `requests.get` dentro de la función `get_response` y asegurarnos de que retorne los datos simulados que especificamos en el mock. Esto nos permite probar la función sin depender de un servicio web real.

Los mocks son una herramienta poderosa en las pruebas unitarias de Python, y te permiten escribir pruebas más efectivas y robustas al controlar el comportamiento de las dependencias externas.


## Ejemplo de implementación

En este repositorio encontrarás un ejemplo de implementación de pruebas unitarias en Python. El repositorio tiene la siguiente estructura:

```
.
├── README.md
├── src
│   ├── mathfuncs
│   │   ├── tests
│   │   │   ├── __init__.py
│   │   │   └── test_sum.py
│   │   ├── __init__.py
│   │   └── sum.py
│   │
│   └── externalcalls
│       ├── tests
│       │   ├── __init__.py
│       │   └── test_externalcalls.py
│       ├── __init__.py
│       └── externalcalls.py
│
├── Pipfile
└── requirements.txt

```

En la carpeta `src` se encuentran dos carpetas, `mathfuncs` y `externalcalls`. En la primera se encuentra un ejemplo de pruebas unitarias para una función que realiza una suma. En la segunda se encuentran dos ejemplos de pruebas unitarias para funciones que realizan una llamada a un servicio externo y la segunda tiene la particularidad de que importa una función de la primera carpeta.



Referencias:

- [Unit Testing in Python](https://realpython.com/python-testing/)
- [unittest — Unit testing framework](https://docs.python.org/3/library/unittest.html)
- [Python Unit Testing Tutorial](https://www.youtube.com/watch?v=6tNS--WetLI)
- [Python Mocking 101: Fake It Before You Make It](https://www.toptal.com/python/an-introduction-to-mocking-in-python)
- [unittest.mock — mock object library](https://docs.python.org/3/library/unittest.mock.html)