import sys
import os
import django
sys.dont_write_bytecode = True
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from db.models import *

# 아래에 코드를 기록하세요.
# 코드 실행은 터미널에서 shell을 실행시켜서 해주세요. 
# $ python manage.py shell_plus 

# ---
directors = [
    ("봉준호", "1993-01-01", "KOR"),
    ("김한민", "1999-01-01", "KOR"),
    ("최동훈", "2004-01-01", "KOR"),
    ("이정재", "2022-01-01", "KOR"),
    ("이경규", "1992-01-01", "KOR"),
    ("한재림", "2005-01-01", "KOR"),
    ("Joseph Kosinski", "1999-01-01", "KOR"),
    ("김철수", "2022-01-01", "KOR"),
]

for director in directors:
    name_ = director[0]
    debut_ = director[1]
    country_ = director[2]
    Director.objects.create(name=name_, debut=debut_, country=country_)


# ---
genres = ['액션', '드라마', '사극', '범죄', '스릴러', 'SF', '무협', '첩보', '재난']

for title_ in genres:
    genre = Genre()
    genre.title = title_
    genre.save()


# ---
Bong = Director.objects.get(name='봉준호')

print(f'id : {Bong.id}')
print(f'name : {Bong.name}')
print(f'debut : {Bong.debut}')
print(f'country : {Bong.country}')

drama = Genre.objects.get(title='드라마')

print(f'id : {drama.id}')
print(f'title : {drama.title}')


# ---
Bong = Director.objects.get(name='봉준호')
drama = Genre.objects.get(title='드라마')

movie = Movie(
    director = Bong,
    genre = drama,
    title = '기생충',
    opening_date = '2019-5-30',
    running_time = 132,
    screening = False
)
movie.save()


# ---
movies = [
    ("봉준호", "드라마", "괴물", "2006-07-27", 119, False),
    ("봉준호", "SF", "설국열차", "2013-10-30", 125, False),
    ("김한민", "사극", "한산", "2022-07-27", 129, True),
    ("최동훈", "SF", "외계+인", "2022-07-20", 142, False),
    ("이정재", "첩보", "헌트", "2022-08-10", 125, True),
    ("이경규", "액션", "복수혈전", "1992-10-10", 88, False),
    ("한재림", "재난", "비상선언", "2022-08-03", 140, True),
    ("Joseph Kosinski", "액션", "탑건 : 매버릭", "2022-06-22", 130, True),
]

for i in movies:
    movie = Movie(
        director = Director.objects.get(name=i[0]),
        genre = Genre.objects.get(title=i[1]),
        title = i[2],
        opening_date = i[3],
        running_time = i[4],
        screening = i[5]
    )
    movie.save()


# ---
movie = Movie.objects.all()

for i in movie:
    print(i.director.name, i.genre, i.title, i.opening_date, i.screening)


# ---
for i in movie:
    print(i.director.name, i.genre.title, i.title, i.opening_date, i.screening)


# ---
order_reverse = Movie.objects.order_by('-opening_date').all()
for i in order_reverse:
    print(i.director.name, i.genre.title, i.title, i.opening_date, i.screening)


# ---
order_ = Movie.objects.order_by('opening_date').all()

for i in order_:
    print(i.director.name, i.genre.title, i.title, i.opening_date, i.screening)
    break


# ---
order_ = Movie.objects.order_by('opening_date').filter(screening=True).all()

for i in order_:
    print(i.director.name, i.genre.title, i.title, i.opening_date, i.screening)


# ---
order_ = Movie.objects.order_by('opening_date').filter(director=1).all()

for i in order_:
    print(i.director.name, i.genre.title, i.title, i.opening_date, i.screening)


# ---
bbong = Movie.objects.order_by('opening_date').filter(director=1).all()[1]

print(bbong.director.name, bbong.genre.title, bbong.title, bbong.opening_date, bbong.screening)


# ---
time = Movie.objects.order_by('running_time').filter(running_time__gt=119).all()

for i in time:
    print(i.director.name, i.genre.title, i.title, i.opening_date, i.running_time, i.screening)


# ---
times = Movie.objects.order_by('running_time').filter(running_time__gte=119).all()

for i in times:
    print(i.director.name, i.genre.title, i.title, i.opening_date, i.running_time, i.screening)


# ---
toto = Movie.objects.order_by('opening_date').filter(opening_date__gte='2022-01-01').all()

for i in toto:
    print(i.director.name, i.genre.title, i.title, i.opening_date, i.running_time, i.screening)


# ---
bong_movie = Movie.objects.order_by('opening_date').filter(genre=2, director=1).all()

for i in bong_movie:
    print(i.director.name, i.genre.title, i.title, i.opening_date, i.running_time, i.screening)


# ---
nobong = Movie.objects.order_by('opening_date').exclude(director=1).all()

for i in nobong:
    print(i.director.name, i.genre.title, i.title, i.opening_date, i.running_time, i.screening)