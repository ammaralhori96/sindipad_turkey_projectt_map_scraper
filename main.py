
import os
import random
import csv
import time
import pyautogui
from datetime import datetime, date
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeDriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from datetime import datetime, timedelta
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from fake_useragent import UserAgent
import requests
def broswer(url_user):
    global driver
    opt = Options()
    opt.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"
    ua = UserAgent()
    userAgent = ua.random
    print(userAgent)
    opt.add_argument(f'user-agent={userAgent}')
    opt.add_experimental_option("excludeSwitches", ['enable-automation'])  # to hide the brower be automated
    #opt.add_argument("--headless")  ### to hide browser
    driver = webdriver.Chrome(  options=opt, service= Service("drivers/chromedriver.exe") )
    # driver = webdriver.Chrome()
    t = webdriver.ActionChains( driver )
    driver.maximize_window()
    print(url_user)
    time.sleep(3)
    driver.get(  url_user )

city="Rize"
        
if "ListUrls.txt" in os.listdir():   
    with open("ListUrls.txt","r",encoding='utf-8') as a_file:
        for url in a_file:
            time.sleep(5)

            #userUrl="https://www.google.com.tr/maps/place/Uzung%C3%B6l/@40.6186688,40.2833083,15.16z/data=!4m6!3m5!1s0x4065945de49ab2e7:0x4e935acb0b0a48ad!8m2!3d40.6194407!4d40.2960778!16zL20vMDZkeGxi?hl=en&authuser=0"
            #userUrl="https://www.google.com.tr/maps/place/GRAND+%C3%96ZT%C3%9CRK+Uzung%C3%B6l/@40.6207735,40.2797654,15.16z/data=!4m9!3m8!1s0x4065c7fbbaa71a1b:0xf33ddebbcd9f34d2!5m2!4m1!1i2!8m2!3d40.6201223!4d40.2856253!16s%2Fg%2F11j0_jf6r3?hl=en&authuser=0"

            #userUrl=str(input("Enter map Url:"))
            userUrl=url
            xyLoc1= userUrl.find("!3d")
            xyLoc2=userUrl.find("!",xyLoc1+3)
            xyLoc3=userUrl.find("!",xyLoc2+3)
            xyLoc=""
            for i in range(xyLoc1+3,xyLoc3):
                xyLoc= xyLoc+userUrl[i]
            xyLoc=xyLoc.replace("!4d",",")
            print(xyLoc)
            try:
                broswer(userUrl)
            except:
                broswer( "https://"+ userUrl)


            time.sleep(5)

            def gittingInformations(areaType):
                
                userUrl=str(driver.current_url)
                xyLoc1= userUrl.find("!3d")
                xyLoc2=userUrl.find("!",xyLoc1+3)
                xyLoc3=userUrl.find("!",xyLoc2+3)
                xyLocN=""
                for i in range(xyLoc1+3,xyLoc3):
                    xyLocN= xyLocN+userUrl[i]
                xyLocN=xyLocN.replace("!4d",",")
                print(xyLocN)
                ####################cheking the name is found

                
                
                
                locName = driver.find_element(By.CLASS_NAME,"DUwDvf.fontHeadlineLarge" ).text
                print(locName)

                def find_row(word):
                    counter = 0
                    
                    if city+".txt" in os.listdir():   
                        with open(city+".txt","r",encoding='utf-8') as a_file:
                            for line in a_file:
                                if word in line:
                                    print(counter)
                                    a_file.close()
                                    return "yes"
                                counter += 1
                    else :
                        x= open(city+".txt","w",encoding='utf-8') 
                        x.close
                
                chickingXyLoc=find_row(locName)
                
                
                if(chickingXyLoc!="yes"):
                    with open(city+".txt", 'a',encoding='utf-8' ) as f:
                        f.write("\n"+locName)
                        f.close()
                    try:
                        locStarsClase = driver.find_element(By.CLASS_NAME,"fontBodyMedium.dmRWX" ).text
                        locStars=""
                        for i in locStarsClase:
                            if i == "\n": break
                            locStars=locStars+i
                        try:
                            if locStars== "":
                                locStars= 4.0
                            locStars=float(locStars)
                        except:
                            locStars=locStars.replace(",",".")
                            if locStars== "":
                                locStars= 4.0
                            locStars=float(locStars)
                    except:
                        locStars= 4.0
                    print(locStars)


                    randomNum=random.randint(10, 50)
                    data = [city ,areaType,locName, locStars,randomNum, xyLocN ]


                    with open('data.csv', 'a', encoding='utf-8', newline='') as f:
                        writer = csv.writer(f)

                        # write the data
                        writer.writerow(data)

                    return locName

                    #locNamper = driver.find_elements(By.CLASS_NAME,"RcCsl.fVHpi.w4vB1d.NOE9ve.M0S7ae.AG25L" )[1].text
                    #print(locNamper)
                    # time.sleep(5)
                    # print(locNamper[0])
                    # print(locNamper[1])
                    # if locNamper[0]!=0 or locNamper[1]!=0 :

                    # locNamper = driver.find_elements(By.CLASS_NAME,"RcCsl.fVHpi.w4vB1d.NOE9ve.M0S7ae.AG25L" )[2].text
                    # print(locNamper)
                else:
                    print("the area is exisist")

                    return "is exisist"


            ################download photos###################################

            # driver.find_element(By.CLASS_NAME,"YkuOqf" ).click() # photos button
            # time.sleep(3)
            # driver.find_element(By.CLASS_NAME,"zbrIY.oms55c" ).click() # back button
            # time.sleep(3)

            def gittingPhotos(checkExist , photoNum):
                if city in os.listdir("imgs\\"):   
                        os.mkdir("imgs\\"+city+"\\" +checkExist)
                else:  
                    os.mkdir("imgs\\"+city)
                    os.mkdir("imgs\\"+city+"\\" +checkExist)
    
                photosNumper= ""
                try: 
                    try:
                        driver.find_element(By.CLASS_NAME,"YkuOqf" ).click() # photos button
                    except:
                        driver.find_element(By.CLASS_NAME,"jtJMuf" ).click() # photos button2
                except: 
                    photosNumper="No Photos"
                    print(photosNumper)
                if photosNumper != "No Photos":
                    time.sleep(5)
                    for x in range (photoNum):
                        
                        try:
                            photo=driver.find_elements(By.CLASS_NAME,"Uf0tqf.loaded" )[x].get_attribute("style")
                            driver.execute_script("document.getElementsByClassName('m6QErb DxyBCb kA9KIf dS8AEf')[0].scroll(0,"+str(1000*x)+")")
                            
                            #pyautogui.moveTo(240,850)
                            #pyautogui.scroll(-1000)
                            time.sleep(1)
                            
                        
                            xyLoc1=photo.find('"')
                            xyLoc3=photo.find('"',xyLoc1+1)
                            photoUrl=""

                            for i in range(xyLoc1+1,xyLoc3):
                                photoUrl= photoUrl+photo[i]
                            #print(photoUrl)

                            # فتح صورة فارغة بإسم الصورة المطلوبة
                            f = open(
                                "imgs\\"+city+"\\" +checkExist +"\\"+ "Photo"  +  str(x)+ '.jpg',
                                'wb')

                            # طباعة محتويات الصورة المأخوذة بداخل الصفحة الفارغة
                            f.write(requests.get(photoUrl).content)
                            time.sleep(1)
                            f.close()
                        except: pass
                    driver.find_element(By.CLASS_NAME,"zbrIY.oms55c" ).click() # back button
                    time.sleep(3)

            checkExist=gittingInformations("area")
            if (checkExist != "is exisist"):
                gittingPhotos(checkExist, 15)      

                ################serching###################################
            def serching2(loc):
                    driver.find_element(By.CLASS_NAME,"gsst_a" ).click() # remove text button
                    time.sleep(3)
                    driver.find_element(By.CLASS_NAME,"tactile-searchbox-input.searchboxinput.xiQnY" ).send_keys(loc)
                    time.sleep(3)
                    driver.find_element(By.ID,"searchbox-searchbutton" ).click() # serch button
                    time.sleep(3)
                    driver.find_element(By.ID,"searchbox-searchbutton" ).click() # serch button
                    time.sleep(3)

            def serching( about , numperLoc, removeText):
                if removeText=="y":     
                    driver.find_element(By.CLASS_NAME,"gsst_a" ).click() # remove text button
                    time.sleep(3)
                    driver.find_element(By.CLASS_NAME,"tactile-searchbox-input.searchboxinput.xiQnY" ).send_keys(about)
                    time.sleep(3)
                    driver.find_element(By.CLASS_NAME,"mL3xi" ).click() # serch button
                time.sleep(5)
                print("numperLoc", str(numperLoc))
                driver.find_elements(By.CLASS_NAME,"hfpxzc" )[numperLoc].click() # numperLoc button
                time.sleep(5)




            ################################## eczane,Lokanta, cami############################################
            for n in range(3):
                
                if n ==0 :
                    numperYouWant=3
                    x=0
                    for g in range(10):
                        try:
                            if g!= 0: serching("eczane", g, "n")
                            elif g==0 :serching("eczane", g, "y") 
                            if (x != numperYouWant):
                                try: 
                                    try:
                                        driver.find_element(By.CLASS_NAME,"YkuOqf" ) # photos button
                                    except:
                                        driver.find_element(By.CLASS_NAME,"jtJMuf" )# photos button2
                                    checkExist=gittingInformations("eczane")
                                    if (checkExist != "is exisist"):
                                        gittingPhotos(checkExist, 5)
                                        x+=1
                                except: 
                                    photosNumper="No Photos"
                                    print(photosNumper) 
                                    checkExist=gittingInformations("eczane")
                                    if (checkExist != "is exisist"):
                                        gittingPhotos(checkExist, 5)
                                        x+=1
                                        os.replace("Logo.jpg","imgs\\"+city+"\\" +checkExist+ "\\Logo.jpg")

                            else:
                                break
                            try:
                                driver.execute_script("document.querySelector('.m6QErb.DxyBCb.kA9KIf.dS8AEf.ecceSd').firstChild.scroll(0,"+str(200*x)+"))")
                                #pyautogui.moveTo(240,850)
                                #pyautogui.scroll(-200)
                            except:
                                driver.execute_script("document.querySelector('.m6QErb.DxyBCb.kA9KIf.dS8AEf.ecceSd').scroll(0,"+str(200*x)+")")
                            time.sleep(1)
                    

                                            
                        except:
                            break
                    


                

                if n ==1 :
                    numperYouWant=5
                    x=0
                    serching2(xyLoc)
                    for g in range(10):
                        try:
                            if g!= 0: serching("Lokanta", g, "n")
                            elif g==0 :serching("Lokanta", g, "y")  
                            if (x != numperYouWant):
                                try: 
                                    try:
                                        driver.find_element(By.CLASS_NAME,"YkuOqf" ) # photos button
                                    except:
                                        driver.find_element(By.CLASS_NAME,"jtJMuf" )# photos button2
                                    checkExist=gittingInformations("Lokanta")
                                    if (checkExist != "is exisist"):
                                        gittingPhotos(checkExist,15)
                                        x+=1
                                except: 
                                    photosNumper="No Photos"
                                    print(photosNumper) 
                            else:
                                break

                            try:
                                driver.execute_script("document.querySelector('.m6QErb.DxyBCb.kA9KIf.dS8AEf.ecceSd').firstChild.scroll(0,"+str(200*x)+"))")
                                #pyautogui.moveTo(240,850)
                                #pyautogui.scroll(-200)
                            except:
                                driver.execute_script("document.querySelector('.m6QErb.DxyBCb.kA9KIf.dS8AEf.ecceSd').scroll(0,"+str(200*x)+")")
                            time.sleep(1)

                        except:
                            break
                        
                        
                        
                
                if n ==2 :
                    
                    numperYouWant=3
                    x=0
                    serching2(xyLoc)
                    for g in range(10):
                        try:
                            if g!= 0: serching("cami", g, "n")
                            elif g==0 :serching("cami", g, "y")  
                        
                            if (x != numperYouWant):
                                try: 
                                    try:
                                        driver.find_element(By.CLASS_NAME,"YkuOqf" ) # photos button
                                    except:
                                        driver.find_element(By.CLASS_NAME,"jtJMuf" )# photos button2
                                    checkExist=gittingInformations("cami")
                                    if (checkExist != "is exisist"):
                                        gittingPhotos(checkExist,1)
                                        x+=1
                                except: 
                                    photosNumper="No Photos"
                                    print(photosNumper) 
                                    checkExist=gittingInformations("eczane")
                                    if (checkExist != "is exisist"):
                                        gittingPhotos(checkExist, 5)
                                        x+=1
                                        os.replace("Logo.jpg","imgs\\"+city+"\\" +checkExist+ "\\Logo.jpg")
                            else:
                                break
                            
                            try:
                                driver.execute_script("document.querySelector('.m6QErb.DxyBCb.kA9KIf.dS8AEf.ecceSd').firstChild.scroll(0,"+str(200*x)+"))")
                                #pyautogui.moveTo(240,850)
                                #pyautogui.scroll(-200)
                            except:
                                driver.execute_script("document.querySelector('.m6QErb.DxyBCb.kA9KIf.dS8AEf.ecceSd').scroll(0,"+str(200*x)+")")
                            time.sleep(1)
                        except:
                            break
            


#####################################################################
            
else :
    x= open("ListUrls.txt","w",encoding='utf-8') 
    x.close
    




