from django.test import TestCase
from django.apps import apps

#Imports for app testing
from .apps import JobsConfig

#Imports for views testing
from .models import Job, JobFileUpload, JobComment

# Create your tests here.
# Testing the app for the blog section
class TestJobConfig(TestCase):

    def test_jobs_app(self):
        self.assertEqual("jobs", JobsConfig.name)
        self.assertEqual("jobs", apps.get_app_config("jobs").name)

#Testing the views
class TestJobViews(TestCase):

    def test_job_home_page(self):
        jobs_home = self.client.get("/jobs/")
        self.assertEqual(jobs_home.status_code, 200)
        self.assertTemplateUsed(jobs_home, "jobs/home.html")