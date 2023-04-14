from django.contrib.auth import logout
from django.shortcuts import render, redirect
from .models import UserMaster, Candidate, Company, JobDetails, ApplyList
from random import randint


# Create your views here.


def IndexPage(request):  # Index(Home) page
    return render(request, "app/index.html")


def SignupPage(request):  # Signup Page
    return render(request, "app/signup.html")


def RegisterUser(request):  # Registering the user
    if request.POST['role'] == 'Candidate':
        role = request.POST['role']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        user = UserMaster.objects.filter(email=email)

        if user:
            message = "User Already Exist"
            return render(request, "app/signup.html", {'msg': message})
        else:
            if password == cpassword:
                otp = randint(10000, 99999)
                newuser = UserMaster.objects.create(role=role, otp=otp, email=email, password=password)
                newcand = Candidate.objects.create(user_id=newuser, firstname=fname, lastname=lname)
                return render(request, "app/login.html", {'email': email})
    else:
        role = request.POST['role']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        user = UserMaster.objects.filter(email=email)

        if user:
            message = "User Already Exist"
            return render(request, "app/signup.html", {'msg': message})
        else:
            if password == cpassword:
                otp = randint(10000, 99999)
                newuser = UserMaster.objects.create(role=role, otp=otp, email=email, password=password)
                newcomp = Company.objects.create(user_id=newuser, firstname=fname, lastname=lname)
                return render(request, "app/login.html", {'email': email})


# OTP VERIFICATION

# def OTPPage(request):
#   return render(request,"app/otpverify.html")
#
# def OTPVerify(request):
#    email = request.POST['email']
#    otp = request.POST['otp']
#
#    user = UserMaster.objects.get(email=email)
#
#    if user:
#        if user.otp == otp:
#            message = "otp verified successfully"
#            return render(request, "app/login.html", {'msg': message})
#        else:
#            message = "otp is incorrect"
#            return render(request, "app/otpverify.html", {'msg': message})
#    else:
#        return render(request, "app/signup.html")
def Loginpage(request):  # Login Page
    return render(request, "app/login.html")


def LoginUser(request):  # Check  users  credentials

    if request.POST['role'] == "Candidate":
        email = request.POST['email']
        password = request.POST['password']

        user = UserMaster.objects.get(email=email)
        if user:
            if user.password == password and user.role == "Candidate":
                can = Candidate.objects.get(user_id=user)
                request.session['id'] = user.id
                request.session['role'] = user.role
                request.session['firstname'] = can.firstname
                request.session['lastname'] = can.lastname
                request.session['email'] = user.email
                request.session['password'] = user.password
                return redirect('index')
            else:
                message = "Password not correct"
                return render(request, "app/login.html", {'msg': message})
        else:
            message = "user Not Found"
            return render(request, "app/signup.html", {'msg': message})
    else:
        email = request.POST['email']
        password = request.POST['password']

        user = UserMaster.objects.get(email=email)
        if user:
            if user.password == password and user.role == "Company":
                com = Company.objects.get(user_id=user)
                request.session['id'] = user.id
                request.session['role'] = user.role
                request.session['firstname'] = com.firstname
                request.session['lastname'] = com.lastname
                request.session['email'] = user.email
                request.session['password'] = user.password
                return redirect('companyindex')
            else:
                message = "Password not correct"
                return render(request, "app/login.html", {'msg': message})
        else:
            message = "user Not Found"
            return render(request, "app/signup.html", {'msg': message})


def ProfilePage(request, pk):  # Showing Profile page for Candidates
    user = UserMaster.objects.get(pk=pk)
    can = Candidate.objects.get(user_id=user)
    return render(request, "app/profile.html", {'user': user, 'can': can})


def UpdateProfile(request, pk):  # Update candidates profile
    user = UserMaster.objects.get(pk=pk)
    if user.role == "Candidate":
        can = Candidate.objects.get(user_id=user)
        can.contact = request.POST.get('contact')
        can.city = request.POST.get('city')
        can.address = request.POST.get('address')
        can.dob = request.POST.get('dob')
        can.profile_pic = request.FILES.get('profile_pic')
        can.joblocation = request.POST.get('joblocation')
        can.jobregion = request.POST.get('jobregion')
        can.jobtype = request.POST.get('jobtype')
        can.postalcode = request.POST.get('postalcode')
        can.resume = request.FILES.get('resume')
        can.gender = request.POST.get('gender')
        can.save()
        url = f'/profile/{pk}'  # format url- to pass
        return redirect(url)


def CandidateJobListPage(request):  # Show Job Listing to candidates
    all_job = JobDetails.objects.all()
    return render(request, "app/job-listings.html", {'all_job': all_job})


def CandidateLogout(request):  # Logout Option
    del request.session['email']
    del request.session['password']
    return redirect("loginpage")


# Counts for Index page
# def Counts(request):
#    candidate_count = UserMaster.objects.filter(role='Candidate').count()
#    company_count = UserMaster.objects.filter(role='Company').count()
#
#    # Render the counts in the home page
#    user_count = {
#        'candidate_count': candidate_count,
#        'company_count': company_count,
#    }
#
#    return redirect(request, 'index', {'user_count': user_count})

def ApplyPage(request, pk):  # Job application page
    user = request.session.get('id')
    if user:
        can = Candidate.objects.get(user_id=user)
        job = JobDetails.objects.get(id=pk)
    return render(request, "app/apply.html", {'user': user, 'can': can, 'job': job})


def ApplyJob(request, pk):  # Applying for the job
    user = request.session.get('id')
    if user:
        can = Candidate.objects.get(user_id=user)
        job = JobDetails.objects.get(id=pk)
        edu = request.POST.get('education')
        exp = request.POST.get('experience')
        minsal = request.POST.get('minsal')
        maxsal = request.POST.get('maxsal')
        web = request.POST.get('website')
        gender = request.POST.get('gender')
        resume = request.FILES.get('resume')
        newapply = ApplyList.objects.create(candidate=can, job=job, education=edu, experience=exp,
                                            website=web, min_salary=minsal, max_salary=maxsal,
                                            gender=gender, resume=resume)
        message = "Job Applied Successfully"
        return render(request, "app/apply.html", {'msg': message})


##################### Employer(Company) Views ##############

def CompanyIndexPage(request):  # Home page
    return render(request, "app/company/index.html")


def CompanyProfilePage(request, pk):  # Showing Company profile page
    user = UserMaster.objects.get(pk=pk)
    com = Company.objects.get(user_id=user)
    return render(request, "app/company/profile.html", {'user': user, 'com': com})


def UpdateCompanyProfile(request, pk):  # Update Company profile
    user = UserMaster.objects.get(pk=pk)
    if user.role == "Company":
        com = Company.objects.get(user_id=user)
        com.firstname = request.POST.get('firstname')
        com.lastname = request.POST.get('lastname')
        com.company_name = request.POST.get('company_name')
        com.state = request.POST.get('state')
        com.city = request.POST.get('city')
        com.contact = request.POST.get('contact')
        com.address = request.POST.get('address')
        com.save()
        url = f'/companyprofile/{pk}'  # format url- to pass
        return redirect(url)


def JobPostPage(request):  # Showing Job Post Page
    return render(request, "app/company/jobpost.html")


def JobDetailSubmit(request):  # Posting job
    user_id = request.session.get('id')
    user = UserMaster.objects.get(id=user_id)
    if user.role == "Company":
        com = Company.objects.get(user_id=user)
        jobname = request.POST.get('jobname')
        companyname = request.POST.get('companyname')
        companyaddress = request.POST.get('companyaddress')
        jobdescription = request.POST.get('jobdescription')
        qualification = request.POST.get('qualification')
        responsibilties = request.POST.get('responsibilties')
        location = request.POST.get('location')
        companywebsite = request.POST.get('companywebsite')
        companyemail = request.POST.get('companyemail')
        companycontact = request.POST.get('companycontact')
        salarypackage = request.POST.get('salarypackage')
        experience = request.POST.get('experience')
        logo = request.FILES.get('image')
        jobtype = request.POST.get('jobtype')

        newjob = JobDetails.objects.create(company_id=com, jobname=jobname, companyname=companyname,
                                           companyaddress=companyaddress,
                                           jobdescription=jobdescription, qualification=qualification,
                                           responsibilties=responsibilties, location=location,
                                           companywebsite=companywebsite,
                                           companyemail=companyemail, companycontact=companycontact,
                                           salarypackage=salarypackage,
                                           experience=experience, logo=logo, jobtype=jobtype)

        message = "Job Post Success"
        return render(request, "app/company/jobpost.html", {'msg': message})


def JobListPage(request):  # List the Posted jobs
    all_job = JobDetails.objects.all()
    return render(request, "app/company/jobpostlist.html", {'all_job': all_job})


def JobApplyList(request):  # Application List
    all_jobapply = ApplyList.objects.all()
    return render(request, "app/company/applyjoblist.html", {'all_jobapply': all_jobapply})


def CompanyLogout(request):  # Logout for comapny user
    del request.session['email']
    del request.session['password']
    return redirect("loginpage")


######### ADMIN ########

def AdminLoginPage(request):  # Admin Login
    return render(request, "app/admin/login.html")


def AdminIndexPage(request):  # Admin Dashboard
    if 'username' in request.session and 'password' in request.session:
        return render(request, "app/admin/index.html")
    else:
        return redirect('adminloginpage')


def AdminLogin(request):  # Checking user credentails of admin(validation)
    username = request.POST['username']
    password = request.POST['password']

    if username == "admin" and password == "admin":
        request.session['username'] = username
        request.session['password'] = password
        return redirect('adminindex')
    else:
        message = "User Name and Password does not Match"
        return render(request, "app/admin/login.html", {'msg': message})


def AdminUserList(request):  # Users List - Admin Section
    all_user = UserMaster.objects.filter(role="Candidate")
    return render(request, "app/admin/userlist.html", {'all_user': all_user})


def AdminCompanyList(request):  # Company List - Admin Section
    all_company = UserMaster.objects.filter(role="Company")
    return render(request, "app/admin/companylist.html", {'all_company': all_company})


def AdminDashBoard(request):  # Admin Dashboard
    return render(request, "app/admin/index.html")


def AdminLogout(request):  # Admin Logout
    logout(request)
    return render(request, "app/admin/login.html")


def UserDelete(request, pk):  # Managing users(Delete)
    user = UserMaster.objects.get(pk=pk)
    user.delete()
    return redirect('userlist')


def VerifyCompanyPage(request, pk):
    company = UserMaster.objects.get(pk=pk)
    if company:
        return render(request, "app/admin/verify.html", {'company': company})


def VerifyCompany(request, pk):
    company = UserMaster.objects.get(pk=pk)
    if company:
        company.is_verified = request.POST['verify']
        company.save()
        return redirect('companylist')


def CompanyDelete(request, pk):
    company = UserMaster.objects.get(pk=pk)
    company.delete()
    return redirect('companylist')
