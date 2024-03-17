from .asignatura import Asignatura, ETemporizacionAsignatura
from .persona import Persona, Estudiante, ESexo
from .profesor import Departamento, EDepartamentoId, Profesor, Asociado, Titular, Investigador

del asignatura, persona, profesor  # Para no poder acceder a los submódulos


class SistemaGestor:
    personas: list[Persona]
    departamentos: list[Departamento]
    asignaturas: list[Asignatura]

    def __init__(self):
        self.personas = list()
        self.departamentos = list()
        self.asignaturas = list()

    def crear_departamento(self, id: EDepartamentoId) -> None:
        # No hay apartamento con el mismo id
        for dep in self.departamentos:
            if dep.id == id:
                raise ValueError("No se puede tener dos apartamentos con el mismo id.")
        self.departamentos.append(Departamento(id))

    def crear_estudiante(self, nombre: str, nif: str, direccion: str, grado: str, ano_entrada: int, sexo: ESexo = ESexo.OTRO, creditos_completados: int = 0) -> None:
        # No hay persona con el mismo nif
        self.nif_ya_usado_raises(nif)
        self.personas.append(Estudiante(nombre, nif, direccion, grado, ano_entrada, sexo, creditos_completados))

    def crear_asociado(self, nombre: str, nif: str, direccion: str, sexo: ESexo = ESexo.OTRO, otro_trabajo: str = "Desconocido") -> None:
        self.nif_ya_usado_raises(nif)
        self.personas.append(Asociado(nombre, nif, direccion, sexo, otro_trabajo))

    def crear_titular(self, nombre: str, nif: str, direccion: str, sexo: ESexo = ESexo.OTRO) -> None:
        self.nif_ya_usado_raises(nif)
        self.personas.append(Titular(nombre, nif, direccion, sexo))

    def crear_investigador(self, nombre: str, nif: str, direccion: str, sexo: ESexo = ESexo.OTRO, area_investigacion: str = "") -> None:
        self.nif_ya_usado_raises(nif)
        self.personas.append(Investigador(nombre, nif, direccion, sexo, area_investigacion))

    def crear_asignatura(self, id: int, nombre: str, creditos: int, temporizacion: ETemporizacionAsignatura) -> None:
        for asignatura in self.asignaturas:
            if asignatura.id == id:
                raise ValueError("No se puede tener dos asignaturas con el mismo id.")
        self.asignaturas.append(Asignatura(id, nombre, creditos, temporizacion))

    def nif_ya_usado(self, nif: str) -> bool:
        for persona in self.personas:
            if persona.nif == nif:
                return True
        return False

    def nif_ya_usado_raises(self, nif: str) -> None:
        if self.nif_ya_usado(nif):
            raise ValueError("No puede haber dos personas con el mismo NIF.")
