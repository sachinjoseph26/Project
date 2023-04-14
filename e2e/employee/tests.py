
from django.test import TestCase, Client
from django.urls import reverse
from .models import UserMaster,Candidate,Company,JobDetails,ApplyList


class UserMasterTestCase(TestCase):                       # UserMaster Model Testcase
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


class CandidateTestCase(TestCase):                  # Candidate Model testcase
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


class CompanyTestCase(TestCase):                # Company Model testcase
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
        return f'{self.company.firstname} {self.company.lastname}'


class ApplyListTestCase(TestCase):              # ApplyList Model test
    def setUp(self):
        self.candidate = Candidate.objects.create(
            firstname="John",
            lastname="Doe",
            contact="1234567890",
            city="Test City",
            address="Test Address",
            postalcode="123456",
            dob="1990-01-01",
            gender="Male",
            joblocation="Test Location",
            jobregion="Test Region",
            jobtype="Full-time",
        )
        self.job = JobDetails.objects.create(
            jobname="Test Job",
            companyname="Test Company",
            companyaddress="Test Company Address",
            jobdescription="This is a test job",
            qualification="Bachelor's Degree",
            responsibilties="Responsibility 1, Responsibility 2",
            location="Test Location",
            companywebsite="www.testcompany.com",
            companyemail="test@testcompany.com",
            companycontact="1234567890",
            salarypackage="50k - 100k",
            experience="1-3 years",
            jobtype="Full-time",
        )
        self.application = ApplyList.objects.create(
            candidate=self.candidate,
            job=self.job,
            education="Bachelor's Degree",
            experience=2,
            website="www.test.com",
            min_salary="50k",
            max_salary="75k",
            gender="Male",
        )

    def test_application_details(self):
        return f"{self.candidate.firstname} applied for {self.job.jobname}"

class JobDetailsTestCase(TestCase):                     # JObDetails Model testcase
    def setUp(self):
        self.job = JobDetails.objects.create(
            jobname="Test Job",
            companyname="Test Company",
            companyaddress="Test Company Address",
            jobdescription="This is a test job",
            qualification="Bachelor's Degree",
            responsibilties="Responsibility 1, Responsibility 2",
            location="Test Location",
            companywebsite="www.testcompany.com",
            companyemail="test@testcompany.com",
            companycontact="1234567890",
            salarypackage="50k - 100k",
            experience="1-3 years",
            jobtype="Full-time",
            )

    def test_job_details(self):
        return f"{self.job} details {self.job.jobname}"



