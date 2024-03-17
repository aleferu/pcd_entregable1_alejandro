from enum import Enum
from abc import ABCMeta
from .asignatura import Asignatura


class ESexo(Enum):
    VARON = 1
    MUJER = 2
    OTRO = 3
    NO_CONTESTA = 4


class Persona(metaclass=ABCMeta):
    nombre: str
    nif: str
    direccion: str
    sexo: ESexo
    asignaturas: set[Asignatura]
    id_asignaturas_completadas: set[int]

    def __init__(self, nombre: str, nif: str, direccion: str, sexo: ESexo = ESexo.NO_CONTESTA) -> None:
        self.nombre = nombre
        self.nif = nif
        self.direccion = direccion
        self.sexo = sexo
        self.asignaturas = set()

    def get_creditos_en_activo(self) -> int:
        return sum([a.creditos for a in self.asignaturas])

    def anadir_asignatura(self, asignatura: Asignatura) -> None:
        self.asignaturas.add(asignatura)

    def quitar_asignatura(self, asignatura: Asignatura) -> None:
        self.asignaturas.remove(asignatura)


class Estudiante(Persona):
    grado: str
    ano_entrada: int
    asignaturas_completadas: list[Asignatura]

    def __init__(self, nombre: str, nif: str, direccion: str, grado: str, ano_entrada: int, sexo: ESexo = ESexo.OTRO) -> None:
        Persona.__init__(self, nombre, nif, direccion, sexo)  # También se podría utilizar super()
        self.grado = grado
        self.ano_entrada = ano_entrada
        self.asignaturas_completadas = list()

    def anadir_asignatura_completada(self, asignatura: Asignatura):
        self.asignaturas_completadas.append(asignatura)

    def asignatura_aprobada(self, asignatura: Asignatura) -> None:
        if asignatura not in self.asignaturas:
            raise ValueError(f"El estudiante no tiene la asignatura que se intenta aprobar. Asignatura: {asignatura.id}.")
        self.quitar_asignatura(asignatura)
        self.anadir_asignatura_completada(asignatura)

    def creditos_completados(self) -> int:
        return sum([a.creditos for a in self.asignaturas_completadas])
