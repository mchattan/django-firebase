from django.test import TestCase, Client
from django.contrib.auth.models import User
import json
from mixer.backend.django import mixer
from hypothesis import given, settings, strategies as st
import pytest
from django.core.exceptions import ValidationError
from rest_framework.reverse import reverse
from pytest_django.asserts import assertTemplateUsed
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse_lazy
import datetime as dt


pytestmark = pytest.mark.django_db

# path("firebase-test/", firebase_test_page, name="firebase_test_page"),
# path("firebase-config/", firebase_config, name="firebase_config"),
# path('register-web-push/', register_web_push, name='register_web_push'),


class TestModels(TestCase):

    def setUp(self):
        self._client = Client()
        User.objects.create(username='test_user', password='asd123!!', email='chattenm@gmail.com')
        user = User.objects.filter(username='test_user').first()
        self._client.force_login(user)


    def test_true(self):
        # TEST INSTALLATIONS
        assert True

    def test_false(self):
        assert False