# Implementación en Python

Se utiliza la utilidad de los paquetes en Python. El paquete se llama `unigestor`, y toda la implementación se encuentra en ese directorio.

### Tests

El fichero de tests `test_unigestor.py` sirve para ir comprobando que todo funciona como se pretende que funcione.

Para comprobar el correcto funcionamiento de todo lo incluido en `test_unigestor.py` se ha utilizado la herramienta [pytest](https://docs.pytest.org/en/8.0.x/ 'pytest website'). Una vez instalada se puede ejecutar el comando `pytest` en el mismo directorio en el que se encuentra este README (si no funciona se puede utilizar la utilidad de ejecutar módulos en python `python -m pytest`). Si se ejecuta desde otro directorio se puede añadir la ruta al directorio como argumento del comando. Si se quiere más información se puede utilizar la flag `-v` para obtener más información.

Se facilita un script para ejecutar los tests, fichero `ejecutar-tests.sh`.
