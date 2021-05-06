from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import GuessNumbers
from .forms import PostForm

# Create your views here.
def index(request):
    lottos = GuessNumbers.objects.all()
    return render(request, 'lotto/default.html', {'lottos' : lottos})
    # request: 사용자 요청을 흘려보냄
    #{}: context, 값을 key와 value로 구성된 dict로 -> html에서 꺼내서 쓸 수 있음

def post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            lotto = form.save(commit=False) # DB에 저장 전 잠시 보류
            lotto.generate() # save()까지 실행
            return redirect('index') # 지정된 이름을 가진 url로 redirect
        return render(request, 'lotto/form.html', {'form' : form})

    else:
        form = PostForm()
        return render(request, 'lotto/form.html', {'form' : form})

def detail(request, lottokey):
    lotto = GuessNumbers.objects.get(pk=lottokey)
    return render(request, "lotto/detail.html", {"lotto": lotto})

def hello(request):
    return HttpResponse('<h1 style="color:red;">Hello, World!</h1>')
