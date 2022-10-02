from unittest import main, TestCase

from src import KTCClient


class ClientTestCase(TestCase):
    client = KTCClient()

    def test_actual_version(self):
        response = self.client.actual_version()
        print(response.actual_version)
        print(response.description)

    def test_branches(self):
        response = self.client.branches()
        for branch in response:
            print(f'[{branch.id}] {branch.title}')

    def test_courses(self):
        response = self.client.courses()
        for course in response:
            print(course)

    def test_news(self):
        response = self.client.news()
        for post in response.announce + response.news:
            print(post)

    def test_news_by_id(self):
        response = self.client.news_by_id(2604)
        print(response.title)

    def test_teachers_list(self):
        response = self.client.teachers_list()
        for teacher in response.teachers:
            print(teacher)

    def test_teacher_timetable(self):
        response = self.client.teacher_timetable(1, 2388)
        for lesson in response.week[0].lessons:
            print(lesson)

    def test_timetable(self):
        response = self.client.timetable(264)
        print(response.week_number)
        print(response.days)


if __name__ == '__main__':
    main(verbosity=2)
