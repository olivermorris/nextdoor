]from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import geckodriver_autoinstaller
import time
from collections import Counter
from  more_itertools import unique_everseen
from twilio.rest import Client
from selenium import webdriver
import geckodriver_autoinstaller
import random
login_chooser = 0
while True:
    login_chooser += 1
    links = []
    titles = []
    filter_dic = []
    geckodriver_autoinstaller.install()
    driver = webdriver.Firefox()
    from collections import OrderedDict
    driver.get("http://www.nextdoor.com/login")




    def listToString(s):

        # initialize an empty string
        message = " "

        # return string
        return (message.join(s))








    def xmlchange():
        f = open("/opt/lampp/htdocs/hello.xml", "w")
        boiler =  '''<Response>
        <Say voice="alice">'''
        textcall
        boiler2 = '''</Say>
        </Response>'''
        f.write(boiler + textcall + boiler2)




    def call():
        account_sid = "AC496b35f20be4a64c203b38d8a14cfa33"
        auth_token = "8b5aac61705703b5bd9a245754d29fc6"
        client = Client(account_sid, auth_token)

        call = client.calls.create(
                                url='http://1043438b5f9d.ngrok.io/hello.xml',
                                to='+19722759653',
                                from_='+12184839689'
                            )
        print(call.sid)









    #defines the function to log in to nextdoor
    def login():
        search = driver.find_element_by_id("id_email")
        search.send_keys("oliverbenmorris@gmail.com")
        time.sleep(2)
        password = driver.find_element_by_id("id_password")
        password.send_keys("Lupe1864")
        password.send_keys(Keys.RETURN)
        time.sleep(7)

    def login1():
        search = driver.find_element_by_id("id_email")
        search.send_keys("guadalupemariagarza1936@gmail.com")
        time.sleep(2)
        password = driver.find_element_by_id("id_password")
        password.send_keys("Lupe1864")
        password.send_keys(Keys.RETURN)
    if login_chooser % 2 == 0:
        login1()

    else:
        login()

    href_list = []
    title_list = []
    dirty_href_list = []
    SCROLL_PAUSE_TIME = 2

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")
    x = 0
    while x<3:
        x += 1
        time.sleep(10)
        cont = True
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)
        elems = driver.find_elements_by_tag_name('a')
        for elem in elems:
            try:
                href = elem.get_attribute('href')
                if href is not None:
                    print(href)
                    dirty_href_list.append(href)

            except:
                print("epic fail")

            print("e")


     # note to self just indented remove if issue
        content = driver.find_elements_by_class_name('_1IVvEt-w')
        print(content)
        for cont in content:
                try:
                    content = driver.find_element_by_class_name('_1IVvEt-w')
                    print (cont.text)
                    title_list.append(cont.text)
                except:
                    print("Failed, skipping now 😃")
                    contt += 1

        # Calculate new scroll height and compare with last scroll height
        time.sleep(5)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height



    href_list = filter(lambda item: '/p/' in item , dirty_href_list)
    href_list = list(unique_everseen(href_list))
    title_list = list(unique_everseen(title_list))

    #print(len(href_list))
    #print(len(title_list))


    final_title = []
    for href_item in href_list:
        f = open('links','a')
        f.write(href_item)
        f.write(',')
        f.close()


    final_title_list = filter(lambda item: 'ontractor' in item , title_list)
    final_title_list2 = filter(lambda item: 'andyman' in item , title_list)
    final_title_list3 = filter(lambda item: 'emodel' in item , title_list)
    final_title_list4 = filter(lambda item: 'eccomendation' in item , title_list)
    final_title_list5 = filter(lambda item: 'itchen' in item , title_list)
    final_title_list6 = filter(lambda item: 'athroom' in item , title_list)
    final_title_list7 = filter(lambda item: 'enovation' in item , title_list)
    final_title_list7 = filter(lambda item: 'eplace' in item , title_list)
    final_title_list8 = filter(lambda item: 'aint' in item , title_list)
    final_title_list9 = filter(lambda item: 'arpenter' in item , title_list)
    final_title_list10 = filter(lambda item: 'nstall' in item , title_list)
    #final_title_list11 = filter(lambda item: 'rywall' in item , title_list)





    for title_item in title_list:
        try:
            final_title.append(title_item)
        except:
            print("failure")



    call_message = []
    call_link = []






    for finalz2 in final_title_list2:
        locc = title_list.index(finalz2)
        #print(len(final_title,"finaltitallength"))
        print(len(href_list))
        print(locc)
        print(href_list[locc])
        print(final_title[locc])
        print(finalz2)
        print("placement")
        call_message.append(finalz2)
        call_link.append(href_list[locc])
        call_link.append("   ")






    for finalz3 in final_title_list3:
        locc = title_list.index(finalz3)
        #print(len(final_title,"finaltitallength"))
        print(len(href_list))
        print(locc)
        print(href_list[locc])
        print(final_title[locc])
        print(finalz3)
        print("placement")
        call_message.append(finalz3)
        call_link.append(href_list[locc])
        call_link.append("   ")



    for finalz4 in final_title_list4:
        locc = title_list.index(finalz4)
        #print(len(final_title,"finaltitallength"))
        print(len(href_list))
        print(locc)
        print(href_list[locc])
        print(final_title[locc])
        print(finalz4)
        print("placement")
        call_message.append(finalz4)
        call_link.append(href_list[locc])
        call_link.append("   ")


    for finalz5 in final_title_list5:
        locc = title_list.index(finalz5)
        #print(len(final_title,"finaltitallength"))
        print(len(href_list))
        print(locc)
        print(href_list[locc])
        print(final_title[locc])
        print(finalz5)
        print("placement")
        call_message.append(finalz5)
        call_link.append(href_list[locc])
        call_link.append("   ")



    for finalz6 in final_title_list6:
        locc = title_list.index(finalz6)
        #print(len(final_title,"finaltitallength"))
        print(len(href_list))
        print(locc)
        print(href_list[locc])
        print(final_title[locc])
        print(finalz6)
        print("placement")
        call_message.append(finalz6)
        call_link.append(href_list[locc])
        call_link.append("   ")




    for finalz7 in final_title_list7:
        locc = title_list.index(finalz7)
        #print(len(final_title,"finaltitallength"))
        print(len(href_list))
        print(locc)
        print(href_list[locc])
        print(final_title[locc])
        print(finalz7)
        print("placement")
        call_message.append(finalz7)
        call_link.append(href_list[locc])
        call_link.append("   ")



    for finalz8 in final_title_list8:
        locc = title_list.index(finalz8)
        #print(len(final_title,"finaltitallength"))
        print("placement")
        call_message.append(finalz8)
        call_link.append(href_list[locc])
        call_link.append("   ")





    for finalz9 in final_title_list9:
        locc = title_list.index(finalz9)
        #print(len(final_title,"finaltitallength"))
        print(finalz9)
        print("placement")
        call_message.append(finalz9)
        call_link.append(href_list[locc])
        call_link.append("   ")


    for finalz10 in final_title_list10:
        locc = title_list.index(finalz10)
        #print(len(final_title,"finaltitallength"))
        print(finalz10)
        print("placement")
        call_message.append(finalz10)
        call_link.append(href_list[locc])
        call_link.append("   ")



    for finalz in final_title_list:
        locc = title_list.index(finalz)
        #print(len(final_title,"finaltitallength"))
        print(len(href_list))
        print(locc)
        print(href_list[locc])
        print(final_title[locc])
        print(finalz)
        print("placement")
        call_message.append(finalz)
        call_link.append(href_list[locc])
        call_link.append("   ")










    def listToString(s):

        # initialize an empty string
        str1 = ""

        # traverse in the string
        for ele in s:
            str1 += ele

        # return string
        return str1


    # Driver code
    s = call_message
    textcall = (listToString(s))
    xmlchange()
    #call()
    loc = 
    s = call_link
    texttext = (listToString(s))











    account_sid = "AC496b35f20be4a64c203b38d8a14cfa33"
    auth_token = "8b5aac61705703b5bd9a245754d29fc6"
    def sender():
        client = Client(account_sid, auth_token)
        message = client.messages \
                        .create(
                             body=texttext,
                             from_='+12184839689',
                             to='+19722759653'
                             )

    textlen = len(texttext)
    if textlen>1:
        sender()
    else:
        print("nothing to see here")
    time.sleep(1200)
    driver.close()
