# 클래스 class



##### Article variables
# 글이 3개라는 전제에 3개의 글을 변수로 표현해봤습니다.
title1 = "개발"
author1 = "마르코"
content1 = "개발은 쉬워요"
view_count1 = 0

title2 = "코칭"
author2 = "마르코"
content2 = "코칭은 쉬워요"
view_count2 = 0

title3 = "창업"
author3 = "마르코"
content3 = "창업은 쉬워요"
view_count3 = 0

# #### Article class
# class Article:
#     title = "개발"
#     author = "마르코"
#     content = "개발은 쉬워요"
#     view_count = 0
#
#
# article1 = Article() # 인스턴스를 만들었다 혹은 객체를 만들었다. 라고 표현함
# print(article1.title)
# article2 = Article()
# article2.title = "코칭" # 아티클2의 내용을 코칭으로 바꾸었는데,
# print(article1.title) # 아티클1은 변경 안했으니 변동없고
# print(article2.title) # 아티클2는 코칭으로 바뀐게 나타남



##### Article class with __init__
class Article:
    author = "마르코"
    view_count = 0

    def __init__(self, title, content): # 인잇을 사용한 순간 타이틀과 콘텐트를 반드시 채워줘야만 한다.
        self.title = title # 셀프의 의미는 클래스안에있는 변수들에 접근하겠다는 약속. 외부에서 지정한 함수의 경우에는 셀프를 쓸 필요가 없었지만 클래스안에서 만든 함수에서는 클래스내의 변수에 접근하기 위해 셀프를 반드시 집어넣어줘야한다.
        self.content = content

    def read(self):
        self.view_count = self.view_count + 1

article1 = Article("개발", "개발은 쉬워요")
article2 = Article("코칭", "코칭은 쉬워요")
article3 = Article("창업", "창업은 쉬워요")

# print(article1.view_count)
# article1.read()
# # article1.view_count1 = article1.view_count1 + 1
# print(article1.view_count)




##### Article class inheritance 상속
class BrunchArticle(Article): # 이 괄호 안의 부분이 상속이야 위의 Article에서 )
    source = "브런치" # 이건 새로 추가한 변수이다. 윗줄에서 상속받은 부분에 없으니 새로 추가해둔 변수.

    def read(self):
        self.view_count = self.view_count + 2 # 부모클래스가 가지고 있던 함수를 덮어쓰고 내용을 바꿀 수 있다 (오버라이드 했다고 표현) 새로 정의한 내용이 표시됨.

brunch_article = BrunchArticle("개발", "개발은 쉬워요") # (활성화 , 인스턴스를 만든다)
print(brunch_article.title) # 상속됐기 때문에 타이틀이 찍히는걸 볼 수 있다.
print(brunch_article.source)
print(brunch_article.view_count) # 부모클래스가 가진 함수도 그대로 가지고 올 수 있다
brunch_article.read()
print(brunch_article.view_count)
