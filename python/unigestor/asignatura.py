from enum import Enum


class ETemporizacionAsignatura(Enum):
    ANUAL = 0
    CUATRI1 = 1
    CUATRI2 = 2
    NO_SE_INDICA = 3


class Asignatura:
    id: int
    nombre: str
    creditos: int
    temporizacion: ETemporizacionAsignatura

    def __init__(self, id: int, nombre: str, creditos: int, temporizacion: ETemporizacionAsignatura) -> None:
        if not creditos >= 1:
            raise ValueError(f"Una asignatura debe ser de al menos un crédito. Se ha proporcionado '{creditos}' como valor.")
        if not creditos == int(creditos):
            raise ValueError(f"Se espera un número entero como valor de créditos de una asignatura. Se ha proporcionado '{creditos}' como valor.")
        self.id = id
        self.nombre = nombre
        self.creditos = creditos
        self.temporizacion = temporizacion
