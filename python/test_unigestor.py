import pytest
from unigestor import *


def test_asignatura_inicializada_correctamente():
    id = 31416
    nombre = "pi"
    creditos = 6
    temporizacion = ETemporizacionAsignatura.CUATRI1
    asignatura = Asignatura(id, nombre, creditos, temporizacion)
    assert id == asignatura.id
    assert nombre == asignatura.nombre
    assert creditos == asignatura.creditos
    assert temporizacion == asignatura.temporizacion


def test_asignatura_creditos_incorrectos():
    id = 31416
    nombre = "pi"
    creditos = 0
    temporizacion = ETemporizacionAsignatura.CUATRI1
    with pytest.raises(ValueError):
        _ = Asignatura(id, nombre, creditos, temporizacion)
        _ = Asignatura(id, nombre, creditos + 0.5, temporizacion)
    with pytest.raises(TypeError):
        _ = Asignatura(id, nombre, creditos + 1.5, temporizacion)


def test_departamento_inicializado_correctamente():
    id_dep = EDEPARTAMENTO_ID.DIIC
    departamento = Departamento(id_dep)
    assert departamento.id == id_dep
