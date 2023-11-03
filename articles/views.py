from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all()

    context = {
        'articles' : articles
    }

    return render(request, 'index.html', context)

def create(request):
    # new/ => 빈 종이를 보여주는 기능
    # create/ => 사용자가 입력한 데이터를 저장
    
    # ===

    # GET create/ => 빈 종이를 보여주는 기능
    # POST create/ => 사용자가 입력한 데이터를 저장
    
    # 모든 경우의 수
    # 1. GET : form을 만들어서 html 문서를 사용자에게 리턴
    #               => 1~4 
    # 2. POST invalid data : 데이터 검증에 실패하는 경우
    # => 검증에 성공한 데이터만 가지고 form을 만들어서 html 문서를 사용자에게 리턴
    # 3. POST valid data (데이터 검증에 성공하는 경우)
    # => DB에 데이터 저장 후 index 페이지로 redirect

    # =========
    # 5. POST요청 (데이터가 잘못 들어온 경우)
    # 10. POSt요청 (데이터가 잘 들어온 경우)
    if request.method == 'POST':
        # 6. form에 사용자가 입력한(잘못된) 정보를 담아서 form을 생성
        # 11. 사용자가 입력한 정보를 담아서 form을 생성
        form = ArticleForm(request.POST)

        # 7. form을 검증 (실패)
        # 12. form을 검증(성공)
        if form.is_valid():
            # 13. form을 저장
            article = form.save()
            # 14. index페이지로 redirect
            return redirect('articles:index')
    
    # 1. GET 요청
    else:
        # 2. 비어있는 form을 만들어서
        form = ArticleForm()

    # 3. context dict에 담고
    # 8. 검증에 실패한 form을 context dict에 담고
    context = {
        'form':form,
    }

    # 4. create.html을 랜더링
    return render(request, 'create.html', context)



def delete (request, id):
    article = Article.objects.get(id=id)
    article.delete()

    return redirect('articles:index')


def update(request, id):
    # 밑에 둘 다 쓰고 있으니 위로 빼준다
    article = Article.objects.get(id=id)

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = ArticleForm(instance=article)

    context = {
        'form':form,
    }
    return render(request, 'update.html', context)