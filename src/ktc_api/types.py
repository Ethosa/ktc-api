# -*- coding: utf-8 -*-
from typing import List

from pydantic import BaseModel


class ActualVersion(BaseModel):
    actual_version: List[int]  # android app actual version
    description: str  # update description


class Branch(BaseModel):
    title: str  # branch title
    id: int  # branch ID


class Group(BaseModel):
    id: int  # group ID
    title: str  # group title


class Course(BaseModel):
    course: int  # course number
    groups: List[Group]  # course groups


class Lesson(BaseModel):
    time: List[str]
    title: str
    teacher: str
    classroom: str


class Day(BaseModel):
    title: str
    lessons: List[Lesson]


class Timetable(BaseModel):
    week_number: int
    days: List[Day]


class Teacher(BaseModel):
    id: int
    name: str


class Teachers(BaseModel):
    teachers: List[Teacher]


class TeacherLesson(BaseModel):
    number: str
    classroom: str
    group: str
    title: str


class TeacherDay(BaseModel):
    title: str
    lessons: List[TeacherLesson]


class TeacherTimetable(BaseModel):
    teacher: str
    title: str
    week: List[TeacherDay]


class Post(BaseModel):
    id: int
    title: str
    image: str
    date: str
    body: str
    likes: List[str]


class News(BaseModel):
    announce: List[Post]
    news: List[Post]


class OneGrade(BaseModel):
    title: str
    grade: int


class Grade(BaseModel):
    title: str
    grades: List[OneGrade]  # all grades
    final_grade: str
    skipped: str  # skipped hours
