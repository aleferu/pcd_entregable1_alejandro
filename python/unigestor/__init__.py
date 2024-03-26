from .asignatura import Asignatura, ETemporizacionAsignatura
from .persona import Persona, Estudiante, ESexo
from .profesor import Departamento, EDepartamentoId, Profesor, Asociado, Titular

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

    def crear_asociado(self, nombre: str, nif: str, direccion: str, departamento: Departamento, sexo: ESexo = ESexo.OTRO, otro_trabajo: str = "Desconocido") -> None:
        self.nif_ya_usado_raises(nif)
        self.personas.append(Asociado(nombre, nif, direccion, departamento, sexo, otro_trabajo))

    def crear_titular(self, nombre: str, nif: str, direccion: str, departamento: Departamento, sexo: ESexo = ESexo.OTRO, area_investigacion: str = "") -> None:
        self.nif_ya_usado_raises(nif)
        if area_investigacion != "":
            SistemaGestor.assert_area_en_departamento(area_investigacion, departamento)
        self.personas.append(Titular(nombre, nif, direccion, departamento, sexo, area_investigacion))

    def crear_asignatura(self, id: int, nombre: str, creditos: int, temporizacion: ETemporizacionAsignatura) -> None:
        for asignatura in self.asignaturas:
            if asignatura.id == id:
                raise ValueError("No se puede tener dos asignaturas con el mismo id.")
        self.asignaturas.append(Asignatura(id, nombre, creditos, temporizacion))

    def asignar_profesor_departamento(self, profesor: Profesor, departamento: Departamento, area_investigacion: str = "") -> None:
        if isinstance(profesor, Titular):
            if area_investigacion != "":
                SistemaGestor.assert_area_en_departamento(area_investigacion, departamento)
            profesor.asignar_area_investigacion(area_investigacion)
        profesor.asignar_departamento(departamento)
        departamento.anadir_profesor(profesor)

    def asignar_director_departamento(self, titular: Titular, departamento: Departamento) -> None:
        if titular.departamento != departamento:
            raise ValueError(f"El titular {titular.nif} no está en el departamento {departamento.id}, por lo que no puede ser el director.")
        departamento.establecer_director(titular)

    def asignar_asignatura_persona(self, asignatura: Asignatura, persona: Persona) -> None:
        persona.anadir_asignatura(asignatura)

    def asignar_area_investigacion(self, area: str, titular: Titular) -> None:
        SistemaGestor.assert_area_en_departamento(area, titular.departamento)
        titular.asignar_area_investigacion(area)

    def estudiante_asignatura_aprobada(self, estudiante: Estudiante, asignatura: Asignatura) -> None:
        estudiante.asignatura_aprobada(asignatura)

    def creditos_completados_estudiante(self, estudiante: Estudiante) -> int:
        return estudiante.creditos_completados()

    def asociado_titular(self, asociado: Asociado, area_investigacion: str) -> None:
        SistemaGestor.assert_area_en_departamento(area_investigacion, asociado.departamento)
        self.personas.remove(asociado)
        self.personas.append(Titular(asociado.nombre, asociado.nif, asociado.direccion, asociado.departamento, asociado.sexo, area_investigacion))

    def nueva_area_investigacion(self, area_investigacion: str, departamento: Departamento):
        departamento.crear_area_investigacion(area_investigacion)

    def get_creditos_en_activo(self, persona: Persona) -> int:
        return persona.get_creditos_en_activo()

    def eliminar_asignatura_persona(self, asignatura: Asignatura, persona: Persona) -> None:
        persona.quitar_asignatura(asignatura)

    def eliminar_asignatura(self, asignatura: Asignatura) -> None:
        self.asignaturas.remove(asignatura)
        for persona in self.personas:
            self.eliminar_asignatura_persona(asignatura, persona)

    def eliminar_area_investigacion(self, area_investigacion: str, departamento: Departamento) -> None:
        departamento.eliminar_area_investigacion(area_investigacion)

    def eliminar_persona(self, persona: Persona):
        self.personas.remove(persona)

    def eliminar_departamento(self, departamento: Departamento) -> None:
        for persona in self.personas:
            if isinstance(persona, Profesor) and persona.departamento is departamento:
                raise ValueError("No se puede eliminar un departamento que tiene profesores asociados.")
        self.departamentos.remove(departamento)

    def cambiar_departamento(self, profesor: Profesor, departamento: Departamento) -> None:
        old_dep = profesor.departamento
        old_dep.eliminar_profesor(profesor)
        profesor.asignar_departamento(departamento)
        departamento.anadir_profesor(profesor)

    @staticmethod
    def assert_area_en_departamento(area: str, departamento: Departamento):
        if area not in departamento.areas:
            raise ValueError(f"El área de investigación '{area}' no pertenece al departamento {departamento.id}.")

    def nif_ya_usado(self, nif: str) -> bool:
        for persona in self.personas:
            if persona.nif == nif:
                return True
        return False

    def nif_ya_usado_raises(self, nif: str) -> None:
        if self.nif_ya_usado(nif):
            raise ValueError("No puede haber dos personas con el mismo NIF.")
