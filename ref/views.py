from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
# from .forms import UserRegisterForm,ItemForm,ItemPictureForm
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserRegisterForm,MedicRegisterForm,ReferalForm
from .models import Test,TestType,Medic,Patient,Clinic

from django.views.generic import ListView,DeleteView,UpdateView
from django import forms
from django.forms import formset_factory,modelformset_factory,inlineformset_factory
from django.contrib.auth import authenticate, login
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.

def home_view(request):
    return render(request,'ref/home_page.html')


def register(request):
    # check what is the method in request
    if request.method == "POST":
        # fill in form with data from POST
        form = UserRegisterForm(request.POST)
        # validate form and save it
        if form.is_valid():
            form.save()
            # get data from form
            cd = form.cleaned_data
            # get user and data which will create Patient
            username = form.cleaned_data.get('username')
            cd = {i:cd[i] for i in cd if i not in ['username','email','password1','password2']}
            user = User.objects.last()
            patient = Patient.objects.create(**cd,user=user)
            patient.save()
            # authenticating newly created user into app
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            # logging with authentication and show message
            login(request, new_user)
            messages.success(request,f'Account was successfully created for you, {username}. You are logged in')
            return redirect('home-page')

    else:
        form = UserRegisterForm()
        context = {'form':form}
    return render(request,'ref/register.html',context=context)


def register_medic(request):
    # check method in request
    if request.method == "POST":
        # fill in form for creating user
        form = MedicRegisterForm(request.POST)
        # validate form and save the user
        if form.is_valid():
            form.save()
            # get data from POST request and create Medic
            cd = form.cleaned_data
            username = form.cleaned_data.get('username')
            cd = {i:cd[i] for i in cd if i not in ['username','email','password1','password2']}
            user = User.objects.last()
            medic = Medic.objects.create(**cd,user=user)
            medic.save()
      
            # authenticating newly created user into app
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            # logging with authentication
            login(request, new_user)
            messages.success(request,f'Account was successfully created for you, {username}. You are logged in')
            print(request.POST)
            return redirect('home-page')

    else:
        form = MedicRegisterForm()
        context = {'form':form}
    return render(request,'ref/register_medic.html',context=context)



def check_tests(request):
    # get all tests for logged patient
    person = Patient.objects.get(user=request.user)
    test = Test.objects.filter(fk_patient =person)
    context = {'items':test}
    return render(request,'ref/tests.html',context=context)

def check_tests_medic(request):
    # get all test for logged medic
    person = Medic.objects.get(user=request.user)
    test = Test.objects.filter(fk_medic=person)
    context = {'items':test}
    return render(request,'ref/tests.html',context=context)


def testing_details(request,pk):
    # gett details of a referal with all tests prescribed
    test = Test.objects.get(pk=pk)
    details = test.testtype_set.all()
    context = {'test':test,'details':details}
    return render(request,'ref/testing_details.html',context=context)


def groups(request, test_pk):
    # get data for printing out the document
    test = Test.objects.get(pk=test_pk)
    details = test.testtype_set.all()
    details_counter = len(details)
    context = {'test':test,'details':details,'details_counter':details_counter}
    return render(request,'ref/testing_printout.html',context=context)


def create_referal(request):
    # get the medic and fill in data with form (indicating relevant medic)
    medic = Medic.objects.get(user=request.user)
    test_types = TestType.objects.all()
    form = ReferalForm(initial={'fk_medic':medic})

    if request.method == "POST":
        # creating new test object
        data = {'fk_patient':Patient.objects.get(pk=request.POST['fk_patient']),'fk_medic':medic,'date_of_issue':request.POST['date_of_issue']}
        create_test = Test(**data)
        create_test.save()
        # preparing data only for selected tests
        tests = {x:y for x,y in request.POST.items() if "tests_selection" in str(x)}
        # looping over the selected tests to create them
        for test in tests.values():
            data_testtype = {'item':Test.objects.last(),'test_type':test}
            new_test_type = TestType(**data_testtype)
            new_test_type.save()
        messages.success(request,f'Referal successfully created')
        return redirect('check_tests_medic')
    context = {'form':form,'test_types':test_types}
    return render(request,'ref/referal_create.html',context)



# class based view for deleting offer
class TestDeleteView(SuccessMessageMixin,DeleteView):
    # model used
    model = Test
    template_name = 'ref/testing_delete.html'
    # if offer is successfully delete - go to main page
    success_url = '/check_tests_medic'
    success_message = "Test was successfully deleted"

    # overwritting delete function to return success message
    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(TestDeleteView, self).delete(request, *args, **kwargs)


def testing_update(request,pk):
    # getting relevant info on test and filling in the form
    test = Test.objects.get(pk=pk)
    form = ReferalForm(instance=test)
    test_types = test.testtype_set.all()
    # creating formset
    ItemFormSet = inlineformset_factory(Test, TestType, fields=('test_type',),extra=0)
    # filling in formset with the relevant instance of a test
    formset = ItemFormSet(instance=test)
    if request.method == 'POST':
        # validating formset with POST data
        formset = ItemFormSet(request.POST,instance=test)
        if formset.is_valid():
            formset.save()

        # CREATING NEW TESTS
        # preparing data only for selected tests
        tests = {x:y for x,y in request.POST.items() if "tests_selection" in str(x)}
        # looping over the selected tests to create them
        print(tests)
        for test in tests.values():
            data_testtype = {'item':Test.objects.last(),'test_type':test}
            new_test_type = TestType(**data_testtype)
            new_test_type.save()
        messages.success(request,f'Referal successfully modified')
        print(request.POST)
        return redirect('check_tests_medic')
    else:
        print(form.errors)
        print(formset.errors)
    context ={'form': form,'forming':formset}
    return render(request,'ref/testing_modify.html',context=context)