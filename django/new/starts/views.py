# django imports style guide
# 1. standard library 
# 2. 3rd party
# 3. Django
# 4. local django

import random
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')


def dinner(request):
    menus = ['피자', '탕수육', '탕볶밥']
    pick = random.choice(menus)
    context = {
        'pick': pick, # 넘겨줄 데이터가 많아져도 아래에 계속 추가해주면 된다
    }
    return render(request, 'dinner.html', context)


def throw(request):
    return render(request, 'throw.html')


def catch(request):
    message = request.GET.get('message')
    context = {
        'message': message,
    }
    return render(request, 'catch.html', context)