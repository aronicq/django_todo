from django.test import TestCase
from django_todo_app.models import Tasks, AppUser
from django.urls import reverse
from rest_framework import status
# Create your tests here.


class UserTasksTestCase(TestCase):

    def setUp(self):
        user1 = AppUser.objects.create(email="newuser1@email.com", password="newpassword1")
        user2 = AppUser.objects.create(email="newuser2@email.com", password="newpassword2")

        Tasks.objects.create(title="task1_title", text="task1_text", is_completed=False, author=user1, completed_date="2020-10-10")
        Tasks.objects.create(title="task2_title", text="task2_text", is_completed=True, author=user2, completed_date="2020-09-10")        


    def test_author(self):
        task1 = Tasks.objects.get(title="task1_title")
        task2 = Tasks.objects.get(title="task2_title")
        self.assertEqual(task1.author, AppUser.objects.get(email="newuser1@email.com"))
        self.assertEqual(task2.author, AppUser.objects.get(email="newuser2@email.com"))


class GetTestCase(TestCase):

    def setUp(self):
        user1 = AppUser.objects.create(email="newuser1@email.com", password="newpassword1")
        user2 = AppUser.objects.create(email="newuser2@email.com", password="newpassword2")

        Tasks.objects.create(title="task1_title", text="task1_text", is_completed=False, author=user1, completed_date="2020-10-10")
        Tasks.objects.create(title="task2_title", text="task2_text", is_completed=True, author=user2, completed_date="2020-09-10")        

    def test_get(self):
        user1 = AppUser.objects.get(email="newuser1@email.com")
        user2 = AppUser.objects.get(email="newuser2@email.com")

        tasks_user1 = Tasks.objects.filter(author=user1)
        tasks_user2 = Tasks.objects.filter(author=user2)

        self.assertEqual(tasks_user1.first().title, "task1_title")
        self.assertEqual(tasks_user2.first().title, "task2_title")

        self.assertEqual(tasks_user1.count(), 1)
        self.assertEqual(len(tasks_user2), 1)