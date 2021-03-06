from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog
#같은 폴더에 있는 models라는 파이썬 파일로부터 Blog클래스를 import


def home(request):
    blogs = Blog.objects#blogs라는 변수에 객체목록을 저장 #쿼리셋
    return render(request, 'home.html', {'blogs':blogs})#세번째 인자로 사전형객체로 blogs키값으로 blogs를 받는다.

def detail(request, blog_id):
#home에 비해 인자를 하나 더 받는다.
    details = get_object_or_404(Blog, pk = blog_id)
    #details변수안에 몇번객체를 넣어줄건데 이 몇번 객체는 get_object_or_404로 받아준다.
    #get_object_or_404는 두개의 인자를 받는데, 첫번째는 어떤 클래스로부터 받는지, 두번째는 검색조건 즉 pk값을 써준다.

    return render(request, 'detail.html', {'details':details})

def new(request):#new.html띄우는 함수
    return render(request, 'new.html')

def create(request):#입력받은 내용을 데이터베이스에 넣어주는 함수
    blog = Blog()#Blog라는 클래스로부터 blog라는 객체를 하나 생성
    blog.title = request.GET['title']#블로그 객체안에 title을 넣어준다.
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()#이것을 쓰기 위해 위에 import해준다.
    blog.save()#지금까지 객체에 넣은 내용을 데이터베이스에 저장해라
    return redirect('/blog/'+str(blog.id))#redirect(URL)은 이 위에 있는 것들을 다 처리하고 이 URL로 넘기세요 라는 뜻
    #str을 써준이유는 url은 항상 str인데, blog.id는 int형이기때문에 문자열로 형변환.
    #위에 있는 것이 다 처리되고, save로 데이터베이스에 저장되고, /blog/str(blog_id)로 곧장 이동이 된다.
    


