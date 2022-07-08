# -*-coding:utf-8-*-
# Autor:编程的小姐姐
# DateTime:2022/4/28 21:44
# File:test2

from movie import *
from sqlalchemy import and_,or_,not_

print(Movie.query.filter_by(name="功夫").all())
print(Cast.query.filter_by(name="周星驰").all())
print(Cast.query.filter_by(name="至尊宝").first().movie_id)
print(Cast.query.filter_by(name="至尊宝").first().name)


#查询Cast表中name中contains周的所有数据
print(Cast.query.filter(Cast.name.like("%周%")).all())
print(Cast.query.filter(Cast.name.like("%龙%")).all())
print(Cast.query.filter(Cast.name.like("龙%")).all())
print(Cast.query.filter(Cast.name.like("%")).all())


#逻辑查询 and_ or_ not_
# print(Cast.query.filter_by(name="周星驰",movie_id=1).all())
print(Cast.query.filter(and_(Cast.name=="至尊宝",Cast.movie_id==1)).all())
# print(Cast.query.filter_by(name="周星驰",movie_id=2).all())
print(Cast.query.filter(not_(and_(Cast.name=="至尊宝",Cast.movie_id==1))).all())


#关联查询  根据 1 取 多
m = Movie.query.filter_by(name="功夫").first()
print(m.cast)


#关联查询根据多查1
zhou = Cast.query.filter(Cast.name=="至尊宝").first()
print(zhou.movie_id)
print(zhou.Movie.name)


#删除数据
niuf = Cast.query.filter_by(name="牛夫人").first()
if niuf:
    db.session.delete(niuf)
    db.session.commit()


#更新数据
zixia = Cast.query.filter_by(name="朱茵").first()
if zixia:
    zixia.name = "紫霞仙子"
    db.session.add(zixia)
    db.session.commit()

Cast.query.filter(Cast.name=="周星驰").update({"name":"至尊宝"})
print(Cast.query.all())

db.session.commit()