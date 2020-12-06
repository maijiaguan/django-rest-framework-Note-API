# django-rest-framework-Note-API
#### 笔记功能需求
1. 笔记增删改查
2. 笔记本增删改查
3. 标签增删改查
4. 笔记可以有三个版本
5. 关键字搜索
6. JWT令牌认证（rest_framework_simplejwt）
7. 短信验证码登录（第一次登录自动注册，解决了验证码登录的token认证）

#### 表结构设计

userProfile表
```
user_uid 用户id
mobile 手机号
username 用户名
email 邮箱
password 密码
```
notes笔记表
```
note_uid 笔记id
note_title 笔记标题
note_last_time 笔记最近更新时间
note_content_v1 笔记版本1
note_content_v1 笔记版本2
note_content_v1 笔记版本3
category_id 标签id
folder_id 笔记本id
user_id 用户id
```
category标签表
```
category_id 标签id
category_name 标签名
category_color 标签颜色
user_uid 用户id
```
notesFolder笔记本表
```
folder_id 笔记本id
folder_name 笔记本名
category_id 标签id
user_id 用户id
```
code 验证吗表
```
code_id 验证码id
mobile 手机号
code 验证码
add_time 创建时间
end_time 失效时间
```
#### 实现功能模块的API
初始化笔记列表API （get）
笔记增（post）、删（delete）、改（patch）、查（get）API
笔记本增（post）、删（delete）、改（patch）、查（get）API
标签增（post）、删（delete）、改（patch）、查（get）API
发送短信验证码API（get）
登录API（post）
更新access token API（post）

