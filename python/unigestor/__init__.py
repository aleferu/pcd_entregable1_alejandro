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

    def crear_estudiante(self, nombre: str, nif: str, direccion: str, grado: str, ano_entrada: int, sexo: ESexo = ESexo.OTRO) -> None:
        # No hay persona con el mismo nif
        self.nif_ya_usado_raises(nif)
        self.personas.append(Estudiante(nombre, nif, direccion, grado, ano_entrada, sexo))

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

    def asignar_profesor_departamento(self, profesor: Profesor, departamento: Departamento) -> None:
        if profesor not in self.personas or departamento not in self.departamentos:
            raise ValueError("Solo se puede trabajar con objetos creados por el objeto de UniGestor.")
        profesor.asignar_departamento(departamento)
        departamento.anadir_profesor(profesor)

    def asignar_investigador_departamento(self, investigador: Investigador, departamento: Departamento, area: str) -> None:
        if area not in departamento.areas:
            raise ValueError(f"El área de investigación {area} no es un área del departamento {departamento.id}.")
        self.asignar_profesor_departamento(investigador, departamento)
        investigador.asignar_area_investigacion(area)

    def asignar_director_departamento(self, titular: Titular, departamento: Departamento) -> None:
        if titular.departamento != departamento:
            raise ValueError(f"El titular {titular.nif} no está en el departamento {departamento.id}, por lo que no puede ser el director.")
        departamento.establecer_director(titular)

    def asignar_asignatura_persona(self, asignatura: Asignatura, persona: Persona) -> None:
        persona.anadir_asignatura(asignatura)

    def asignar_area_investigacion(self, area: str, investigador: Investigador) -> None:
        if area not in investigador.departamento.areas:
            pass
        # TODO: Creo que hay que cambiar como funcionan los departamentos y los profesores para que no haya opcionales.

    def nif_ya_usado(self, nif: str) -> bool:
        for persona in self.personas:
            if persona.nif == nif:
                return True
        return False

    def nif_ya_usado_raises(self, nif: str) -> None:
        if self.nif_ya_usado(nif):
            raise ValueError("No puede haber dos personas con el mismo NIF.")
