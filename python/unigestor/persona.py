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
    creditos_completados: int

    def __init__(self, nombre: str, nif: str, direccion: str, grado: str, ano_entrada: int, sexo: ESexo = ESexo.OTRO, creditos_completados: int = 0) -> None:
        Persona.__init__(self, nombre, nif, direccion, sexo)  # También se podría utilizar super()
        self.grado = grado
        self.ano_entrada = ano_entrada
        self.creditos_completados = creditos_completados

    def asignatura_aprobada(self, asignatura: Asignatura) -> None:
        if asignatura not in self.asignaturas:
            raise ValueError(f"El estudiante no tiene la asignatura que se intenta aprobar. Asignatura: {asignatura.id}.")
        self.quitar_asignatura(asignatura)
        self.creditos_completados += asignatura.creditos
