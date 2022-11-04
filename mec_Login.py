import mechanize
from bs4 import BeautifulSoup
import operator

# html_text = requests.get("https://afeladat2017.whiteshield.net/login").text 
br = mechanize.Browser()
br.set_handle_robots(False)
cookies = mechanize.CookieJar()
br.set_cookiejar(cookies)
br.addheaders = [('User-agent','Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36')]
br.set_handle_refresh(False)
br.open("https://afeladat2017.whiteshield.net/login")
br.select_form(nr=0)

res = br.submit();
html = res.read()
soup = BeautifulSoup(html,"lxml")
form = soup.find("form", action="/login")
math= form.find("span", id="math").text
math_input = form.find("input", id="id_captcha_1")  

first_math = int(math[0])
second_math = int(math[-2])
web_operators = math[1]
ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}
operator = ops[web_operators](first_math,second_math)
str_operator = str(operator)
Cap=[]

br.select_form(nr=0)
text = "admin"
br.form["username"] = text
br.form["password"] = text
br.form["captcha_1"] = str_operator
Cap.append(first_math)
Cap.append(web_operators)
Cap.append(second_math)

response = br.submit()

print("submit:",response.read())
