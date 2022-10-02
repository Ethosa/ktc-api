# -*- coding: utf-8 -*-
from typing import List

from requests import Session
from pydantic import parse_obj_as
from .types import ActualVersion, Branch, Course, Timetable, Teachers, TeacherTimetable, News, Post


class KTCClient:
    """Provides working around KTC API
    """

    API_URL = 'http://mob.kansk-tc.ru'

    def __init__(self):
        self.session = Session()

    def actual_version(self) -> ActualVersion:
        return parse_obj_as(ActualVersion, self.session.get(
            f'{self.API_URL}/ktc-api/actual-version'
        ).json())

    def branches(self) -> List[Branch]:
        return parse_obj_as(List[Branch], self.session.get(
            f'{self.API_URL}/ktc-api/branches'
        ).json())

    def courses(self, branch_id: int = 1) -> List[Course]:
        return parse_obj_as(List[Course], self.session.get(
            f'{self.API_URL}/ktc-api/courses/{branch_id}'
        ).json())

    def news(self) -> News:
        return parse_obj_as(News, self.session.get(
            f'{self.API_URL}/ktc-api/news/'
        ).json())

    def news_by_id(self, nid: int) -> Post:
        return parse_obj_as(Post, self.session.get(
            f'{self.API_URL}/ktc-api/news/id{nid}'
        ).json())

    def teachers_list(self) -> Teachers:
        return parse_obj_as(Teachers, self.session.get(
            f'{self.API_URL}/ktc-api/teachers-list'
        ).json())

    def teacher_timetable(self, branch_id: int, teacher_id: int) -> TeacherTimetable:
        return parse_obj_as(TeacherTimetable, self.session.get(
            f'{self.API_URL}/ktc-api/teacher-timetable/{branch_id}/{teacher_id}'
        ).json())

    def timetable(self, group_id: int, week: int = 0) -> Timetable:
        return parse_obj_as(Timetable, self.session.get(
            f'{self.API_URL}/ktc-api/timetable/{group_id}/{week}'
        ).json())
