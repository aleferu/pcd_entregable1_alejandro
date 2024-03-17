from abc import ABCMeta
from enum import Enum
from typing import Optional
from .persona import Persona, ESexo
from .asignatura import Asignatura


class EDepartamentoId(Enum):
    DIIC = 1
    DITEC = 2
    DIS = 3


class Departamento:
    id: EDepartamentoId
    miembros: set["Profesor"]
    director: Optional["Profesor"]
    areas: set[str]

    def __init__(self, id: EDepartamentoId) -> None:
        self.id = id
        self.miembros = set()
        self.director = None
        self.areas = set()

    def anadir_profesor(self, profesor: "Profesor") -> None:
        self.miembros.add(profesor)

    def eliminar_profesor(self, profesor: "Profesor") -> None:
        self.miembros.remove(profesor)

    def establecer_director(self, titular: "Titular") -> None:
        if not isinstance(titular, Titular):
            raise TypeError("Un profesor debe de ser titular para poder ejercer de director de departamento.")
        self.director = titular

    def crear_area_investigacion(self, area: str) -> None:
        self.areas.add(area)

    def eliminar_area_investigacion(self, area: str) -> None:
        self.areas.remove(area)


class Profesor(Persona, metaclass=ABCMeta):
    creditos_maximos: int
    departamento: Optional[Departamento]

    def __init__(self, nombre: str, nif: str, direccion: str, sexo: ESexo = ESexo.OTRO) -> None:
        Persona.__init__(self, nombre, nif, direccion, sexo)  # También se podría utilizar super()
        self.departamento = None

    def anadir_asignatura(self, asignatura: Asignatura) -> None:
        if self.get_creditos_en_activo() + asignatura.creditos > self.creditos_maximos:
            raise ValueError("Se ha intentado asignar una asignatura a un profesor, pero eso sobrepasaría los créditos máximos asociados a su título.")
        Persona.anadir_asignatura(self, asignatura)

    def asignar_departamento(self, departamento: Departamento) -> None:
        self.departamento = departamento


class Asociado(Profesor):
    creditos_maximos: int = 6
    otro_trabajo: str

    def __init__(self, nombre: str, nif: str, direccion: str, sexo: ESexo = ESexo.OTRO, otro_trabajo: str = "Desconocido") -> None:
        Profesor.__init__(self, nombre, nif, direccion, sexo)  # También se podría utilizar super()
        self.otro_trabajo = otro_trabajo


class Titular(Profesor):
    creditos_maximos: int = 12

    def __init__(self, nombre: str, nif: str, direccion: str, sexo: ESexo = ESexo.OTRO) -> None:
        Profesor.__init__(self, nombre, nif, direccion, sexo)  # También se podría utilizar super()


class Investigador(Titular):
    area_investigacion: str

    def __init__(self, nombre: str, nif: str, direccion: str, sexo: ESexo = ESexo.OTRO, area_investigacion: str = "") -> None:
        Titular.__init__(self, nombre, nif, direccion, sexo)  # También se podría utilizar super()
        self.area_investigacion = area_investigacion

    def asignar_area_investigacion(self, area_investigacion: str) -> None:
        self.area_investigacion = area_investigacion
