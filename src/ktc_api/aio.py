# -*- coding: utf-8 -*-
from typing import List

from aiohttp import ClientSession
from pydantic import parse_obj_as
from .types import ActualVersion, Branch, Course, Timetable, Teachers, TeacherTimetable, News, Post, Grade


class AKTCClient:
    """Provides working around KTC API
    """

    API_URL = 'http://mob.kansk-tc.ru'

    def __init__(self):
        self.session = ClientSession()

    async def close(self):
        await self.session.close()

    async def actual_version(self) -> ActualVersion:
        response = await self.session.get(f'{self.API_URL}/ktc-api/actual-version')
        return parse_obj_as(ActualVersion, await response.json())

    async def branches(self) -> List[Branch]:
        response = await self.session.get(f'{self.API_URL}/ktc-api/branches')
        return parse_obj_as(List[Branch], await response.json())

    async def courses(self, branch_id: int = 1) -> List[Course]:
        response = await self.session.get(f'{self.API_URL}/ktc-api/courses/{branch_id}')
        return parse_obj_as(List[Course], await response.json())

    async def news(self) -> News:
        response = await self.session.get(f'{self.API_URL}/ktc-api/news/')
        return parse_obj_as(News, await response.json())

    async def news_by_id(self, nid: int) -> Post:
        response = await self.session.get(f'{self.API_URL}/ktc-api/news/id{nid}')
        return parse_obj_as(Post, await response.json())

    async def teachers_list(self) -> Teachers:
        response = await self.session.get(f'{self.API_URL}/ktc-api/teachers-list')
        return parse_obj_as(Teachers, await response.json())

    async def teacher_timetable(self, branch_id: int, teacher_id: int) -> TeacherTimetable:
        response = await self.session.get(f'{self.API_URL}/ktc-api/teacher-timetable/{branch_id}/{teacher_id}')
        return parse_obj_as(TeacherTimetable, await response.json())

    async def timetable(self, group_id: int, week: int = 0) -> Timetable:
        response = await self.session.get(f'{self.API_URL}/ktc-api/timetable/{group_id}/{week}')
        return parse_obj_as(Timetable, await response.json())

    async def grades(self, username: str, password: str) -> List[Grade]:
        response = await self.session.get(
            f'{self.API_URL}/ktc-api/pro/grades',
            params={
                'username': username,
                'password': password
            }
        )
        return parse_obj_as(List[Grade], await response.json())
