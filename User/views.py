from django.shortcuts import render,redirect
from User.forms import UserRegisterForm,UserLoginForm,Userjobpostform,Chooseform,Applyform
from django.contrib.auth import(authenticate,get_user_model,login,logout,)
from User.models import Company
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import smtplib
import mimetypes
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
# from django.views.generic import ListView

def signup(request):
	if request.method == "POST":
		forms = UserRegisterForm(request.POST ,request.FILES)
		if forms.is_valid():
			user = forms.save(commit=False)
			#username = forms.cleaned_data['username']
			password = forms.cleaned_data['password']
			user.set_password(password)
			user.save()
			#login
			# new_user = authenticate(username=username, password=password)
			login(request, user)
			return redirect('../login_user')
	else:
		forms=UserRegisterForm()
	return render(request, 'User/register.html', {"forms": forms,})

def login_user(request):
	info = Company.objects.all()
	if request.method == "POST":
		forms = UserLoginForm(request.POST or None)
		if forms.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)
			login(request, user)
			# x= user.objects.get(Choose)
			# if user.x == 'Employeer':
			# 	return redirect('../profile')
			# elif user.x == 'Jobseeker':
			# 	pass

			return redirect('../choose')
	else:
		forms=UserLoginForm()
	return render(request, 'User/login.html', {"forms": forms,'info':info},)



# def base(request):
# 	if request.method == "POST":
# 		forms = UserJobsearchform(request.POST or None)
# 		if forms.is_valid():
# 			user = forms.save(commit=False)

# 			user.save()

# 			return redirect('../company')
# 	else:
# 		forms=UserJobsearchform()
# 	return render(request, 'User/index.html',{"forms": forms, })	


# query search
def base(request):
	info=Company.objects.all()
	query=request.GET.get("q")
# 	# page = request.GET.get("page",5)
	if query:
		info=info.filter(Q(job_title__icontains=query)|Q(Location__icontains=query))
		return render(request,'User/index.html',{'info':info,'query':query})
	else:
		return render(request, 'User/index.html',{'info':info})
		
# # 		# print("**"*10)
# # 		# print(info.count())
# # 		# paginator = Paginator(info, 5)
# # 		# try:
# # 		# 	info = paginator.page(page)
# # 		# except PageNotAnInteger:
# # 		# 	info = paginator.page(1)
# # 		# except EmptyPage:
# # 		# 	info = paginator.page(paginator.num_pages)
			
# full text search
# def base(request):
# 	qs=Company.objects.all()
# 	keywords = request.GET.get('q')
# 	if keywords:
# 		query = SearchQuery(keywords)
# 		title_vector = SearchVector('job_title', weight='A')
# 		content_vector = SearchVector('Location', weight='B')
# 		vectors = title_vector + content_vector
# 		qs = qs.annotate(search=vectors).filter(search=query).distinct()
# 		qs = qs.annotate(rank=SearchRank(vectors, query))
# 	return render(request,'User/index.html',{'qs':qs})

def logout(request):
	return render(request,'User/index.html')



def company(request):
	# )if request.user.is_staff or  request.user.is_superuser:
	# 	queryset=Company.objects.all()
	# query=request.GET.get("q")
	# if query:
	# 	info=queryset.filter(Q(job_title_icontains=query)).distinct()
	# print(query)
	# info=Company.objects.all(
	return render(request,'User/company.html')

def profile(request):
	info = Company.objects.all()
	return render(request, 'User/profile.html',{'info':info})#{'Choose':Choose})


def postjob(request):
	if request.method == "POST":
		forms = Userjobpostform(request.POST,request.FILES)
		if forms.is_valid():
			user = forms.save(commit=False)
			user.save()
			return redirect('../profile')
	else:
		forms = Userjobpostform()
	return render(request, 'User/post.html', {"forms": forms})

def aboutus(request):
	return render(request, 'User/about-us.html')

def contact(request):
	return render(request, 'User/contact.html')

def choose(request):
	if request.method=="POST":
		forms=Chooseform(request.POST,request.FILES)
		if forms.is_valid():
			Choose = request.POST['Choose']
			print(type(Choose))
			if Choose=='Employeer':
				return redirect('../profile')
			else:
				return redirect('../base')
	else:
		forms=Chooseform()
	return render(request,'User/choose.html',{'forms':forms})


def apply(request):
	if request.method=="POST":
		sender=request.POST['Applier_email']
		reciver=request.POST['Company_email']
		password=request.POST['password']
		# message=request.POST['cv']
		message="I'am intrested on your vacancy, CV submitted to the Admin."
		try:
			smtpObj=smtplib.SMTP('smtp.gmail.com',587)
			smtpObj.starttls()
			smtpObj.login(sender,password)
			smtpObj.sendmail(sender,reciver,message)
			print('Email send')
		except smtplib.SMTPException:
			print('mail not send')
		forms=Applyform(request.POST,request.FILES)
		if forms.is_valid():
			user = forms.save(commit=False)
			user.save()
			return redirect('../base')
	else:
		forms=Applyform()
	return render(request,'User/apply.html',{'forms':forms})
