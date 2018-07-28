#假设的登录查询
select * from user where login = "victor" and password="123"

server端代码

string sql = "select * from users where login='"+formusr+"'and password='"+formpwd+"'";

#输入字符

formusr='' or 1=1

formpwd=anything

#实际查询代码

select * from users where username='' or 1=1 and password='anything`
