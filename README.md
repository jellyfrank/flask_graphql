# Graphql 演示项目

## 安装依赖

```python
pip install -r requirements.txt
```

## 初始化数据库

运行python manage.py shell进入脚本环境

```python
db.create_all()
```

执行初始化数据库

## 填充数据

执行sql:

```sql
insert into users ("name")  values ('张三');
```

# 运行

```python
python run.py
```