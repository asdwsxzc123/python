# 获取title,count,rate,country,大于分数为8的不同国家电视剧数量
db.tv1.aggregate(
  {$project:{title:1,_id:0,count:'$rating.count',rate:'$rating.value',country:'$tv_category'}},
  {$match:{rate:{$gt:8}}},
  {$group:{_id:'$country',count:{$sum:1}}},
  {$project:{_id:0,country:'$_id',count:1}}
)

# 统计t1中所有name出现的次数
# 统计t1中所有name出现的次数并次数大于4
# 统计t1中所有name出现的次数并次数大于4(只显示次数)
db.t1.aggregate(
  {$group:{_id:'$name',count:{$sum:1}}},
  {$match:{count:{$gt:4}}},
  {$project:{_id:0,count:1}}
)