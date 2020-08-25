from django.shortcuts import render
from .models import Post


# render : html템플릿을 렌더링을 해준다 아래의 index 라는 함수는 서버에 요청이 들어왔을 시 index.html을
# 렌더링 해서 나에게 보여주는 역활을함


# index.html 페이지를 부르는 함수
def index(request):
    return render(request, "main/index.html")


# board.html 페이지를 부르는 함수
def board(request):

    # Post를 가져와 postlist 변수에 저장
    postlist = Post.objects.all()
    print(postlist)
    # board.html 페이지를 열때 모든 Post인 postlist도 같이 가져옴
    return render(request, "main/board.html", {"postlist": postlist})
