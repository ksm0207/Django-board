from django.db import models

# 가장 해야할것
# 첫번째 게시글을 만들어보자 --> 제목 글 내용 작성자 등


class Post(models.Model):
    # 게시글(post) -->  제목 (postname) 내용(contents) model 생성
    postname = models.CharField(max_length=50)
    contents = models.TextField()
    # blank = True : 입력을 받았을때 입력이 없어도됨
    # null = True : DB상에서 Null 값을 허용
    # 게시글 Post에 이미지 추가
    photos = models.ImageField(blank=True, null=True)

    # 게시글의 제목이 Post object(1) (2) 대신 아래함수 사용
    def __str__(self):
        return self.postname

