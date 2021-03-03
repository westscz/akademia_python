"""
Article: https://akademiapython.pl/czytanie-tracebackow-czy-to-pieklo-kiedys-sie-konczy/
"""

from dataclasses import dataclass, field, replace
from uuid import uuid4
from typing import List


class CourseNotFoundError(Exception):
    ...


@dataclass
class Module:
    name: str
    uuid: str = field(default_factory=lambda: str(uuid4()))

    def __repr__(self):
        return f"Module(uuid={self.uuid}, name={self.name})"


@dataclass
class Course:
    name: str
    uuid: str = field(default_factory=lambda: str(uuid4()))
    items: List[Module] = field(default_factory=list)

    def __repr__(self):
        return f"Course(uuid={self.uuid}, name={self.name}, items={self.items})"


class CourseRepository:
    def __init__(self):
        self._store: dict = {}

    def create(self, name: str) -> Course:
        course = Course(name)
        self._store[course.uuid] = course
        return course

    def get(self, course_id: str) -> Course:
        course = self._store.get(course_id, None)
        if course is not None:
            return course
        raise CourseNotFoundError(f"Course for uuid={course_id} is not found")

    def save(self, course: Course) -> Course:
        self._store[course.uuid] = course
        return course


class ModuleRepository:
    def __init__(self):
        self._store = {}

    def create(self, name):
        module = Module(name)
        self._store[module.uuid] = module
        return module

    def get(self, module_id):
        return self._store[module_id]


class CourseLogic:
    def __init__(
        self, course_repository: CourseRepository, module_repository: ModuleRepository
    ):
        self._courses = course_repository
        self._modules = module_repository

    def create(self, name):
        return self._courses.create(name)

    def get(self, course_id):
        return self._courses.get(course_id)

    def create_module(self, course_id, name):
        course = self._courses.get(course_id)
        module = self._modules.create(name)
        course = replace(course, items=course.items + [module])
        self._courses.save(course)


if __name__ == "__main__":
    cl = CourseLogic(CourseRepository(), ModuleRepository())
    course = cl.create("Python Basics")
    cl.create_module(course.uuid, "For Loop")
    cl.create_module(course.uuid, "For Else Loop")
    course = cl.get(course.uuid)
    print(course)
    cl.get("52e506a4-1117-4b96-9658-434122abbb26")
