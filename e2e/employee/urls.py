from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    #path("", views.IndexPage, name="index"),
    path("", views.SignupPage, name="signup"),
    path("home", views.IndexPage, name="index"),
    path("signup/", views.SignupPage, name="signup"),
    path("register/", views.RegisterUser, name="register"),
    #path("otppage/", views.OTPPage,name="otppage"),
    #path("otp/", views.OTPVerify, name="otp"),
    path("loginpage", views.Loginpage, name="loginpage"),
    path("loginuser", views.LoginUser, name="login"),
    path("profile/<int:pk>",views.ProfilePage,name="profile"),
    path("updateprofile/<int:pk>",views.UpdateProfile, name="updateprofile"),
    path("joblist/", views.CandidateJobListPage, name="joblist"),
    path("candidatelogout/", views.CandidateLogout, name="candidatelogout"),
    path("apply/<int:pk>", views.ApplyPage, name="apply"),
    path("applyjob/<int:pk>",views.ApplyJob, name="applyjob"),

    ###### Company Urls #####
    path("companyindex/", views.CompanyIndexPage, name="companyindex"),
    path("companyprofile/<int:pk>", views.CompanyProfilePage, name="companyprofile"),
    path("updatecompanyprofile/<int:pk>", views.UpdateCompanyProfile, name="updatecompanyprofile"),
    path("jobpostpage/", views.JobPostPage, name="jobpostpage"),
    path("jobpost/", views.JobDetailSubmit, name="jobpost"),
    path("joblistpage/", views.JobListPage, name="joblistpage"),
    path("applyjoblist/", views.JobApplyList, name="applyjoblist"),
    path("companylogout/", views.CompanyLogout, name="companylogout"),


    ###### ADMIN ######
    path("adminloginpage/", views.AdminLoginPage, name="adminloginpage"),
    path("adminlogin/",views.AdminLogin, name="adminlogin"),
    path("adminindex/", views.AdminIndexPage, name="adminindex"),
    path("admindashboard/", views.AdminDashBoard, name="admindasboard"),
    path("adminuserlist/", views.AdminUserList, name="userlist"),
    path("admincompanylist", views.AdminCompanyList, name="companylist"),
    path("adminlogout/", views.AdminLogout, name="adminlogout"),
    path("deleteuser/<int:pk>", views.UserDelete, name="deleteuser"),
    path("deletecompany/<int:pk>", views.CompanyDelete, name="deletecompany"),
    path("verifycompanypage/<int:pk>", views.VerifyCompanyPage, name="verifypage"),
    path("verifycompany/<int:pk>", views.VerifyCompany, name="verify"),

]