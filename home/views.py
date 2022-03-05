from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import datetime
from django.contrib import messages


import ast
from django.contrib.staticfiles import finders

from django.template.loader import  get_template

from datetime import datetime

from django.shortcuts import redirect
from django.contrib.auth.models import User
from username_validator import UsernameValidator
from django.http import JsonResponse
import json
from django.core.files.storage import FileSystemStorage
import datetime
from datetime import date

from .forms import *
from django.contrib.auth import authenticate , login,logout
from .models import *
import os
from django.core.exceptions import ObjectDoesNotExist

from pathlib import Path
#import barcode
#from barcode.writer import ImageWriter

#ean = barcode.get('ean13', '123456789102', writer=ImageWriter())
#filename = ean.save('ean13')
#emp=employee.objects.get(id=1)
#emp.delete()

from io import BytesIO
from django.core.files import File

from PIL import Image
def logoutUser(request):
    logout(request)
    return redirect('loginUser')
def loginUser(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':

            username = request.POST.get('username')
            password =request.POST.get('password')
            if username =='' or password=='':
                messages.warning(request,"Please Enter Username and Password")
                return redirect('loginUser')
            else:
                

                user = authenticate(request, username=username, password=password)

                if user is not None:
                    login(request, user)
                    return redirect('/')
                else:
                    messages.warning(request, 'Username OR password is incorrect')
                    return redirect('loginUser')
        else:
            return render(request,'login.html')

def register(request):
    if request.method=='POST':
        
        username = request.POST.get('username')
        password =request.POST.get('password')
        email = request.POST.get('email')
        phone =request.POST.get('phone')
        if username=='' or password =='' or email =='' or phone=='':
            print("empty")
        else:
            
            User.objects.create(username=username,password=password,email=email,first_name=phone)
            return redirect('/')
        
    return render(request,'register.html')
def validation(request):
    
    
    data = json.loads(request.body)
    
    try:
        c=UsernameValidator().validate_all(data['name'])
        return JsonResponse(['true'],safe=False)
    except:
        
        return JsonResponse(['false'],safe=False)
       

def dashboard(request):
    if request.user.is_authenticated:
        
        BASE_DIR = Path(__file__).resolve().parent.parent
        photo=os.path.join(BASE_DIR,'static\img')
        return render(request,'dashboard.html')
    else:
        return redirect('/')
    
    
def load_emp(request):
    if request.method=='GET':
        idd = request.GET.get('DepartmentId')
        
        dname=subDeptart.objects.get(id=idd)
        opt2_html=''
        emps=employee.objects.filter(subDept=dname)
        opt2_html='"<option value=''>---select Employee---</option>"'
        for model in emps:
            opt2_html += "<option value='"+str(model.id)+"'>"+str(model)+"</option>"
            
    return JsonResponse(opt2_html,safe=False)
def getInfo(request):
    from django.core.serializers import serialize 
    from django.core.serializers.json import DjangoJSONEncoder

    if request.method=='GET':
        idd = request.GET.get('DepartmentId')
        data=employee.objects.get(id=idd)
        emp_list=[]
        emp_list.append(data.ename)
        emp_list.append(data.father_name)
        emp_list.append(data.Designation)
        emp_list.append(data.subDept)
        emp_list.append(data.Replacment)
        emp_list.append(data.salery)
        emp_list.append(data.Cnic)

        return JsonResponse(emp_list,safe=False)
     
def Update_info(request):
    
    emp=''
    depts=dept.objects.all().order_by('dname')
    pram={'dept':depts,'emp':emp}
    return render(request,'update_info.html',pram)
def addEmp(request):
    add='not'
    info=''
    if request.method=="POST":
        name = request.POST.get('name')
        fname = request.POST.get('fname')
        designation = request.POST.get('designation')
        mainDept = request.POST.get('mainDept')
        subDept = request.POST.get('subDept')
        Replacement = request.POST.get('Replacement')
        Salery = request.POST.get('Salery')
        cnic = request.POST.get('cnic')
        phone = request.POST.get('phone')
        Issue_Date = request.POST.get('Issue_Date')
        pic = request.FILES['pic']
        CINC_img = request.FILES['CINC_img'];
        
        Address = request.POST.get('Address')
        """im = Image.open(pic)

        #im.convert('RGB') # convert mode

        #im.thumbnail(size) # resize image

        #thumb_io = BytesIO() # create a BytesIO object

        im.save(thumb_io, 'JPEG', quality=85) # save image to BytesIO object
        im .show(pic)
        thumbnail = File(thumb_io, name=name)"""
        #extension = pic.split('.')[-1]
        #og_filename = pic.split('.')[0]
        #new_filename = "%s.%s" % (name, extension)
        print(subDept)
        subd=subDeptart.objects.get(id=subDept)
        emp,created=employee.objects.get_or_create(ename=name,father_name=fname,Designation=designation,subDept=subd,salery=Salery,Cnic=cnic,phone=phone,issueDate=Issue_Date,Address=Address,pic=pic,nicCopy=CINC_img)
        
        if created:
            emp.save()
            info=name
            add='added'
            subD=dept.objects.all()
            emp=employee.objects.all().order_by('ename')
            pram={'subD':subD,'emp':emp,'add':add,'info':info,'date':date.today()}
            return redirect('addEmp')
        
    subD=dept.objects.all()
    emp=employee.objects.all().order_by('ename')
    dates=date.today().strftime('%Y-%m-%d')
    
    pram={'subD':subD,'emp':emp,'date':dates}
    return render(request,'addEmp.html',pram)

def load_subDept(request):
    if request.method=='GET':
        id = request.GET.get('DepartmentId')
        page = request.GET.get('page')
        if id=='':
            opt2_html='"<option value=''>---select SubDepart---</option>"'
        else:
            
        
            dname=dept.objects.get(id=id)
            subd=subDeptart.objects.filter(Dname=dname)
            if page=='view':
                opt2_html='"<option value=''>select Sub Department</option>"'
               
            else:
                opt2_html='"<option value=''>Select Sub Department</option>"'
            for model in subd:
                
                opt2_html += "<option value='"+str(model.id)+"'>"+str(model)+"</option>"
  
    return JsonResponse(opt2_html,safe=False)
def view_allEmp(request):
    if request.method=="POST":
        subdept=request.POST['total_fee']
        
        text=request.POST['text']
        sub=subDeptart.objects.get(id=subdept)
        emp=''
        if text!=None:
            emp = employee.objects.filter(ename__icontains=text)
        
        depts=dept.objects.all()
        sdept=subDeptart.objects.all()
        pram={'emp':emp,'dept':depts,'subD':sdept}
        return render (request,'view_allEmp.html',pram)
    emp=employee.objects.all().order_by('ename')
    depts=dept.objects.all()
    sdept=subDeptart.objects.all()
    pram={'emp':emp,'dept':depts,'subD':sdept}
    return render (request,'view_allEmp.html',pram)
def detail_view(request,pk):
    emp=employee.objects.get(id=pk)
    pram={'emp':emp}
    return render(request, 'detail_view.html', pram)
def days_cur_month():
    from datetime import date, timedelta, datetime
    m = datetime.now().month
    y = datetime.now().year
    ndays = (date(y, m+1, 1) - date(y, m, 1)).days
    d1 = date(y, m, 1)
    d2 = date(y, m, ndays)
    delta = d2 - d1

    return [(d1 + timedelta(days=i)).strftime('%Y-%m-%d') for i in range(delta.days + 1)]

def take_Attendance(request):
    import calendar
    now = datetime.datetime.now()
    days=calendar.monthrange(now.year, now.month)[1]
    context = range(1, days+1)
    if request.method=='POST':
        da=request.POST['date']
        
        deptID=request.POST['dept']
        depts=dept.objects.all()
        sdept=subDeptart.objects.all()
        emp=employee.objects.filter(subDept=subDeptart.objects.get(id=deptID))
        #d=days_cur_month()
        import calendar
        now = datetime.datetime.now()
        days=calendar.monthrange(now.year, now.month)[1]
        context = range(1, days+1)
        pram={'emps':emp,'dept':depts,'subD':sdept,'date':da,'dates':context}
        return render(request, 'Attendance.html', pram)
    emp=employee.objects.all().order_by('ename')
    depts=dept.objects.all()
    sdept=subDeptart.objects.all()
    pram={'emps':emp,'dept':depts,'subD':sdept,'dates':context}
    return render(request, 'Attendance.html', pram)
def submibt_Attendance(request):
    from datetime import datetime
    from django.core import serializers
    if request.method=='GET':
        emps = ast.literal_eval(request.GET.get('list'))
        dat = request.GET.get('date')
        flag=False
        dt=datetime.strptime(dat , '%Y-%m-%d')
        
        month=dt.strftime('%Y-%m')
        
        mo,created=Attendance_month.objects.get_or_create(month=month)
        if created:
            mo.save()
        retStr=[]
        for e in emps:
            
            em=employee.objects.get(id=e['id'])
            try:
                emp,created=Attendance.objects.get_or_create(date=dat,emp=em,months_attendance=mo,subd=em.subDept,status=e['status'])
                if created:
                   
                    emp.save()
                    
                    retStr.append(em.ename)
                    
                    
                    
                else:
                    
                    flag=True
            except:
                
                flag=True
               
        if flag:
            h=''
            for e in retStr:

                h=h+","+str(e)+","
            return HttpResponse("Attendance Marked those Employees "+h+ " Other Employee Alread Marked")
            
        else:
            return HttpResponse("Employees Attendance Saved in Database")
    else:
        return HttpResponse("Request Data Not Found")
def getDataForUpdate(request):
    from datetime import datetime
    from django.core import serializers
    if request.method=='GET':
        id=request.GET.get('id')
        datee=request.GET.get('date')
        
        #dt = datetime.strptime(date, '%Y-%m-%d')
        
        dt=datetime.strptime(datee , '%Y-%m-%d')
        
        month=dt.strftime('%Y-%m')
        day=dt.strftime('%Y-%m-%d')
        try:
            emp=employee.objects.get(id=id)
            mo=Attendance_month.objects.get(month=month)
            att=Attendance.objects.filter(months_attendance=mo,date=day,emp=emp).values('id', 'emp', 'months_attendance','status')
            if att:
                dtt=datetime.strptime(datee , '%Y-%m-%d').date()
                
                li=list(att)
                
                li.append(emp.ename)
                li.append((date.today()-dtt).days)
                json_posts = json.dumps(li)
            
            else:
                json_posts='Attendance Not Found'
        except ObjectDoesNotExist:
            json_posts='Attendance Not Found'
            
    return HttpResponse(json_posts)
def UpdateEmpStatus(request):
    if request.method=='GET':
        st=request.GET.get('newStatus')
        id=request.GET.get('id')
        at=Attendance.objects.get(id=id)
        if (at.date-date.today()).days<=3:
            at.status=st
            at.save()
            return HttpResponse("Employee Attendance Updated")
        else:
            return HttpResponse("Employee Attendance Update Within 3 Days")
def link_callback(uri, rel):
            """
            Convert HTML URIs to absolute system paths so xhtml2pdf can access those
            resources
            """
            result = finders.find(uri)
            if result:
                    if not isinstance(result, (list, tuple)):
                            result = [result]
                    result = list(os.path.realpath(path) for path in result)
                    path=result[0]
            else:
                    sUrl = settings.STATIC_URL        # Typically /static/
                    sRoot = settings.STATIC_ROOT      # Typically /home/userX/project_static/
                    mUrl = settings.MEDIA_URL         # Typically /media/
                    mRoot = settings.MEDIA_ROOT       # Typically /home/userX/project_static/media/

                    if uri.startswith(mUrl):
                            path = os.path.join(mRoot, uri.replace(mUrl, ""))
                    elif uri.startswith(sUrl):
                            path = os.path.join(sRoot, uri.replace(sUrl, ""))
                    else:
                            return uri

            # make sure that file exists
            if not os.path.isfile(path):
                    raise Exception(
                            'media URI must start with %s or %s' % (sUrl, mUrl)
                    )
            return path
def render_pdf_view(request,pk):
    emp=employee.objects.get(id=pk)
    template_path = 'html2Pdf.html'
    
    context = {'emp': emp}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)
    
    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response, link_callback=link_callback)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
def historyOfAttendance(request):
    
    if request.method=="POST":
        dep=request.POST.get('dept')
        mon=request.POST.get('month')
        print('dept ',dep,'months',mon)
        #emp=employee.objects.filter(subDept=dep)
        
            
        #getmonth=Attendance_month.objects.get(id=mon)
        #depta=subDeptart.objects.get(id=dep)filter(months_attendance=mon,subd=dep).order_by('date')
        emp=Attendance.objects.filter(months_attendance=mon,subd=dep).order_by('date')
        print(emp)
    
    months=Attendance_month.objects.all().order_by('-id')
    deptt=dept.objects.all().order_by('dname')
    pram={'months':months,'dept':deptt}
    return render(request, 'historyAttendance.html',pram)