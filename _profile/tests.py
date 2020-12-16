from datetime import datetime

from django.test import TestCase, Client
from rest_framework.test import APIClient

from .models import Layout, Resume, Profile, Skills, Testimonial, Service
from users.models import ContactUser, ContactAdmin
from django.contrib.auth import get_user_model
from blog.models import Post

User = get_user_model()


class PortfolioCase(TestCase):
    def setUp(self):
        """ this is the database so right now the files i create here
         are the once that are in the database"""
        print(datetime.now())
        self.user = User.objects.create_user(username='admin', password='thankgod12',email='begintjay@mgial.com')
        self.userB = User.objects.create_user(username='coderjay', password='thankgod12')
        Testimonial.objects.create(user=self.user, client_name='client_name', image='',
                                   detail='detail', url='https://www.google.com')
        Skills.objects.create(description='my skill ', user=self.user, percent=14, icon='')
        Resume.objects.create(name='my resume name', detail='my resume name', start_date=datetime.now(),
                              end_date=datetime.now(), user=self.user)
        Post.objects.create(user=self.user, title='my title',
                            description='my description', image='', category='EN', slug='slug', view_count=12,
                            published_date=datetime.now())
        Service.objects.create(user=self.user,
                               name='the name',
                               image='', description='this is the description')

        # self.currentCount = Tweet.objects.all().count()

    # logging in with this client
    def get_client(self):
        client = Client()
        client.login(username=self.user.username, password="thankgod12")
        return client

    def test_portfolio_user_created(self):
        self.assertEqual(self.user.username, 'admin')

    def test_profile_user_exist(self):
        profile = Profile.objects.filter(user=self.user).first()
        print(profile)
        self.assertEqual(self.user.profile, profile)

    def test_layout_user_exist(self):
        layout = Layout.objects.filter(user=self.user).first()
        print(layout)
        self.assertEqual(self.user.layout, layout)

    def test_resume_created(self):
        resume = Resume.objects.create(name='my resume name', detail='my resume name', start_date=datetime.now(),
                                       end_date=datetime.now(), user=self.user)
        self.assertEqual(resume.id, 2)
        self.assertEqual(resume.user, self.user)

    def test_skill_created(self):
        skill = Skills.objects.create(description='my skill ', user=self.user, percent=14, icon='')
        self.assertEqual(skill.id, 2)
        self.assertEqual(skill.user, self.user)

    def test_service_created(self):
        service = Service.objects.create(user=self.user,
                                         name='the name',
                                         image='', description='this is the description')
        self.assertEqual(service.id, 2)
        self.assertNotEqual(service.user, 2)
        self.assertEqual(service.user, self.user)

    def test_profile_detail_view(self):
        client = self.get_client()
        _response = client.get("/profile_no_user/")
        print('the _response ', _response.status_code)
        self.assertEqual(_response.status_code, 302)
        self.assertNotEqual(_response.url, 'http://www.localhost:8000/profile/profileUpdate/')

    def test_contact_user(self):
        client = self.get_client()
        print('the client',client)
        response = client.post('user/contactUser/', {'contact_name': 'demilade',
                                                                               'contact_email': 'demilade@gmail.com',
                                                                               'contact_subject': 'the subject',
                                                                               'contact_message':'the message',
                                                                               'to_email':'begintjay@mgial.com'
                                                                               })
        print('the response for client',response)




