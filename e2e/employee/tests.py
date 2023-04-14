from django.test import TestCase
from django.urls import reverse
from .models import UserMaster,Candidate,Company


class UserMasterTestCase(TestCase):
    def setUp(self):
        self.user = UserMaster.objects.create(
            email='e2e@gmail.com',
            password='password',
            otp=123456,
            role='Candidate'
        )

    def test_user_master_fields(self):
        self.assertEqual(self.user.email, 'e2e@gmail.com')
        self.assertEqual(self.user.password, 'password')
        self.assertEqual(self.user.otp, 123456)
        self.assertEqual(self.user.role, 'Candidate')
        self.assertEqual(self.user.is_active, False)
        self.assertEqual(self.user.is_verified, False)

    def test_user_master_str(self):
        return self.user.email


class CandidateTestCase(TestCase):
    def setUp(self):
        self.user = UserMaster.objects.create(
            email='e2e@gmail.com',
            password='password',
            otp=123456,
            role='admin'
        )
        self.candidate = Candidate.objects.create(
            user_id=self.user,
            firstname='John',
            lastname='Doe',
            contact='1234567890',
            city='New York',
            address='123 Main Street',
            postalcode='12345',
            dob='2000-01-01',
            gender='Male',
            joblocation='New York',
            jobregion='Northeast',
            jobtype='Full-time',
            #profile_pic='test.jpg',
            #resume='test.pdf'
        )

    def test_candidate_fields(self):
        self.assertEqual(self.candidate.user_id, self.user)
        self.assertEqual(self.candidate.firstname, 'John')
        self.assertEqual(self.candidate.lastname, 'Doe')
        self.assertEqual(self.candidate.contact, '1234567890')
        self.assertEqual(self.candidate.city, 'New York')
        self.assertEqual(self.candidate.address, '123 Main Street')
        self.assertEqual(self.candidate.postalcode, '12345')
        self.assertEqual(self.candidate.dob, '2000-01-01')
        self.assertEqual(self.candidate.gender, 'Male')
        self.assertEqual(self.candidate.joblocation, 'New York')
        self.assertEqual(self.candidate.jobregion, 'Northeast')
        self.assertEqual(self.candidate.jobtype, 'Full-time')


    def test_candidate_str(self):
        return f'{self.candidate.firstname} {self.candidate.lastname}'


class CompanyTestCase(TestCase):
    def setUp(self):
        self.user_master = UserMaster.objects.create(
            email='e2e@gmail.com',
            password='password',
            otp=123456,
            role='admin'
        )
        self.company = Company.objects.create(
            user_id=self.user_master,
            firstname='Jane',
            lastname='Doe',
            company_name='Acme Inc.',
            state='New York',
            city='New York',
            contact='1234567890',
            address='123 Main Street',
            #logo_pic='test.jpg'
        )

    def test_company_fields(self):
        self.assertEqual(self.company.user_id, self.user_master)
        self.assertEqual(self.company.firstname, 'Jane')
        self.assertEqual(self.company.lastname, 'Doe')
        self.assertEqual(self.company.company_name, 'Acme Inc.')
        self.assertEqual(self.company.state, 'New York')
        self.assertEqual(self.company.city,'New York')
        self.assertEqual(self.company.contact, '1234567890')
        self.assertEqual(self.company.address, '123 Main Street')
        #self.assertEqual(self.company.logo_pic,'app/img/company/test.jpg')

    def test_company_str(self):
        return f'{self.company.firstname} {self.company.company_name}'


