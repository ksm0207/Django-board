from django.shortcuts import render, redirect

from .models import Post  # View Model ( Post 게시글 ) 가져오기

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


# board 게시글을 부르는 함수


def posting(request, pk):
    # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
    post = Post.objects.get(pk=pk)
    # posting.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
    return render(request, "main/posting.html", {"post": post})


def new_post(request):
    if request.method == "POST":
        if request.POST["photos"]:
            new_article = Post.object.create(
                postname=request.POST["postname"],
                contents=request.POST["contents"],
                photos=request.POST["photos"],
            )
        else:
            new_article = Post.objects.create(
                postname=request.POST["postname"],
                contents=request.POST["contents"],
                photos=request.POST["photos"],
            )
            print(new_article)
        return redirect("/board/")
    return render(request, "main/post.html")


def remove_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect("board")
    return render(request, "main/remove_post.html", {"Post": post})
