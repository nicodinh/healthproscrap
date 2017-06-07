import sys
##from PyQt4.QtGui import QApplication
##from PyQt4.QtCore import QUrl
##from PyQt4.QtWebKit import QWebPage

"""
# Developer : Pritam Samadder
# Developer Email : pritamsamadder048@gmail.com

# Scrap Url : "http://annuairesante.ameli.fr"
"""

import selenium
from selenium import webdriver
from selenium import *
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


import bs4
from bs4 import BeautifulSoup as bs
import urllib.request
import datetime
import csv
import html
import time
import re
import sys, os


catagorylist=['1','2','3','4','5','6','33###R_0###','7','8','47###R_0###','9','10','11','12','13','14','15',"16","17","18","19","20","20###R_0###","21","23###R_0###","40###N_0###","22","23","24","25","34###R_0###","26","27","28","29","30","32###R_0###","31","32","24###R_0###","50###R_0###","33","34","35","36","37","38","39","37###R_1###","40","41","42","43","44","61###N_0###","14###R_0###","45","46","47","4###R_0###","48","49","50","6###N_0###","51","15###R_0###","52","53","54","55","5###R_0###","56","57","58","37###R_0###","59","60","39###R_0###","61","62","38###R_0###","3###N_0###","14###R_1###","17###R_0###","3###R_0###","21###R_0###"]
#catagorydict={'1':"Acupuncteur",'2':'Allergologue','3':'Ambulance /Véhicule sanitaire léger','4':'Anatomo-Cyto-Pathologiste','5':"Anesthésiste réanimateur",'6':'Angiologue',"33###R_0###":"Biologiste (Médecin biologiste)",'7':'Cancérologues','8':'Cardiologue','47###R_0###':'Chirurgien cervico-facial (Oto-Rhino-Laryngologue (ORL) et chirurgien cervico-facial)','9':'Chirurgien général','10':"Chirurgien infantile",'11':'Chirurgien maxillo-facial','12':'Chirurgien maxillo-facial et stomatologiste','13':'Chirurgien oral','14':'Chirurgien orthopédiste et traumatologue','15':'Chirurgien plasticien','16':"Chirurgien thoracique et cardio-vasculaire",'17':'Chirurgien urologue', 'Chirurgien vasculaire', 'Chirurgien viscéral', 'Chirurgiens-dentistes', 'Dentistes (Chirurgiens-dentistes)', 'Dermatologue et vénérologue', 'Diabétologue (Endocrinologue-diabétologue)', 'Dialyse (Néphrologue)', 'Echographiste', 'Endocrinologue-diabétologue', 'Fournisseur de matériel médical et para-médical', 'Gastro-entérologue et hépatologue', 'Généraliste (Médecin généraliste)', 'Gériatre', 'Gynécologues / Obstétricien', 'Hématologue', 'Homéopathe', 'Infirmier', 'Kinésithérapeute (Masseur-kinésithérapeute)', 'Laboratoires', 'Masseur-kinésithérapeute', 'Matériel (Fournisseur de matériel médical et para-médical)', 'Matériel (Pharmacien)', 'Médecin biologiste', 'Médecin généraliste', 'Médecin généticien', 'Médecin spécialiste en médecine nucléaire', 'Médecin spécialiste en santé publique et médecine sociale', 'Médecin thermaliste', 'Médecine appliquée aux sports', 'Médecine sociale (Médecin spécialiste en santé publique et médecine sociale)', 'Néphrologue', 'Neurochirurgien', 'Neurologue', 'Neuropsychiatre', 'Ophtalmologiste', 'Orthopédie dento-faciale (Stomatologistes)', 'Orthopédiste (Chirurgien orthopédiste et traumatologue)', 'Orthophoniste', 'Orthoptiste', 'Oto-Rhino-Laryngologue (ORL) et chirurgien cervico-facial', 'Pathologiste (Anatomo-Cyto-Pathologiste)', 'Pédiatre', 'Pédicure-podologue', 'Pharmacien', 'Phlébologue (Angiologue)', 'Phoniatre', 'Plasticien (Chirurgien plasticien)', 'Pneumologue', 'Psychiatres', 'Radiologue', 'Radiothérapeute', 'Réanimateur (Anesthésiste réanimateur)', 'Réanimateur médical', 'Rhumatologue', 'Sage-femme', 'Santé publique (Médecin spécialiste en santé publique et médecine sociale)', 'Spécialiste en médecine interne', 'Spécialiste en médecine physique et de réadaptation', 'Sports (Médecine appliquée aux sports)', 'Stomatologistes', 'Taxi conventionné', 'Thermaliste (Médecin thermaliste)', 'Transport sanitaire (Ambulance /Véhicule sanitaire léger)', 'Traumatologue (Chirurgien orthopédiste et traumatologue)', 'Urologue (Chirurgien urologue)', 'Véhicule sanitaire léger (Ambulance /Véhicule sanitaire léger)', 'Vénérologue (Dermatologue et vénérologue)'}
catagorytitle=['Acupuncteur', 'Allergologue', 'Ambulance /Véhicule sanitaire léger', 'Anatomo-Cyto-Pathologiste', 'Anesthésiste réanimateur', 'Angiologue', 'Biologiste (Médecin biologiste)', 'Cancérologues', 'Cardiologue', 'Chirurgien cervico-facial (Oto-Rhino-Laryngologue (ORL) et chirurgien cervico-facial)', 'Chirurgien général', 'Chirurgien infantile', 'Chirurgien maxillo-facial', 'Chirurgien maxillo-facial et stomatologiste', 'Chirurgien oral', 'Chirurgien orthopédiste et traumatologue', 'Chirurgien plasticien', 'Chirurgien thoracique et cardio-vasculaire', 'Chirurgien urologue', 'Chirurgien vasculaire', 'Chirurgien viscéral', 'Chirurgiens-dentistes', 'Dentistes (Chirurgiens-dentistes)', 'Dermatologue et vénérologue', 'Diabétologue (Endocrinologue-diabétologue)', 'Dialyse (Néphrologue)', 'Echographiste', 'Endocrinologue-diabétologue', 'Fournisseur de matériel médical et para-médical', 'Gastro-entérologue et hépatologue', 'Généraliste (Médecin généraliste)', 'Gériatre', 'Gynécologues / Obstétricien', 'Hématologue', 'Homéopathe', 'Infirmier', 'Kinésithérapeute (Masseur-kinésithérapeute)', 'Laboratoires', 'Masseur-kinésithérapeute', 'Matériel (Fournisseur de matériel médical et para-médical)', 'Matériel (Pharmacien)', 'Médecin biologiste', 'Médecin généraliste', 'Médecin généticien', 'Médecin spécialiste en médecine nucléaire', 'Médecin spécialiste en santé publique et médecine sociale', 'Médecin thermaliste', 'Médecine appliquée aux sports', 'Médecine sociale (Médecin spécialiste en santé publique et médecine sociale)', 'Néphrologue', 'Neurochirurgien', 'Neurologue', 'Neuropsychiatre', 'Ophtalmologiste', 'Orthopédie dento-faciale (Stomatologistes)', 'Orthopédiste (Chirurgien orthopédiste et traumatologue)', 'Orthophoniste', 'Orthoptiste', 'Oto-Rhino-Laryngologue (ORL) et chirurgien cervico-facial', 'Pathologiste (Anatomo-Cyto-Pathologiste)', 'Pédiatre', 'Pédicure-podologue', 'Pharmacien', 'Phlébologue (Angiologue)', 'Phoniatre', 'Plasticien (Chirurgien plasticien)', 'Pneumologue', 'Psychiatres', 'Radiologue', 'Radiothérapeute', 'Réanimateur (Anesthésiste réanimateur)', 'Réanimateur médical', 'Rhumatologue', 'Sage-femme', 'Santé publique (Médecin spécialiste en santé publique et médecine sociale)', 'Spécialiste en médecine interne', 'Spécialiste en médecine physique et de réadaptation', 'Sports (Médecine appliquée aux sports)', 'Stomatologistes', 'Taxi conventionné', 'Thermaliste (Médecin thermaliste)', 'Transport sanitaire (Ambulance /Véhicule sanitaire léger)', 'Traumatologue (Chirurgien orthopédiste et traumatologue)', 'Urologue (Chirurgien urologue)', 'Véhicule sanitaire léger (Ambulance /Véhicule sanitaire léger)', 'Vénérologue (Dermatologue et vénérologue)']
catagorydict={'1': 'Acupuncteur', '2': 'Allergologue', '3': 'Ambulance /Véhicule sanitaire léger', '4': 'Anatomo-Cyto-Pathologiste', '5': 'Anesthésiste réanimateur', '6': 'Angiologue', '33###R_0###': 'Biologiste (Médecin biologiste)', '7': 'Cancérologues', '8': 'Cardiologue', '47###R_0###': 'Chirurgien cervico-facial (Oto-Rhino-Laryngologue (ORL) et chirurgien cervico-facial)', '9': 'Chirurgien général', '10': 'Chirurgien infantile', '11': 'Chirurgien maxillo-facial', '12': 'Chirurgien maxillo-facial et stomatologiste', '13': 'Chirurgien oral', '14': 'Chirurgien orthopédiste et traumatologue', '15': 'Chirurgien plasticien', '16': 'Chirurgien thoracique et cardio-vasculaire', '17': 'Chirurgien urologue', '18': 'Chirurgien vasculaire', '19': 'Chirurgien viscéral', '20': 'Chirurgiens-dentistes', '20###R_0###': 'Dentistes (Chirurgiens-dentistes)', '21': 'Dermatologue et vénérologue', '23###R_0###': 'Diabétologue (Endocrinologue-diabétologue)', '40###N_0###': 'Dialyse (Néphrologue)', '22': 'Echographiste', '23': 'Endocrinologue-diabétologue', '24': 'Fournisseur de matériel médical et para-médical', '25': 'Gastro-entérologue et hépatologue', '34###R_0###': 'Généraliste (Médecin généraliste)', '26': 'Gériatre', '27': 'Gynécologues / Obstétricien', '28': 'Hématologue', '29': 'Homéopathe', '30': 'Infirmier', '32###R_0###': 'Kinésithérapeute (Masseur-kinésithérapeute)', '31': 'Laboratoires', '32': 'Masseur-kinésithérapeute', '24###R_0###': 'Matériel (Fournisseur de matériel médical et para-médical)', '50###R_0###': 'Matériel (Pharmacien)', '33': 'Médecin biologiste', '34': 'Médecin généraliste', '35': 'Médecin généticien', '36': 'Médecin spécialiste en médecine nucléaire', '37': 'Médecin spécialiste en santé publique et médecine sociale', '38': 'Médecin thermaliste', '39': 'Médecine appliquée aux sports', '37###R_1###': 'Médecine sociale (Médecin spécialiste en santé publique et médecine sociale)', '40': 'Néphrologue', '41': 'Neurochirurgien', '42': 'Neurologue', '43': 'Neuropsychiatre', '44': 'Ophtalmologiste', '61###N_0###': 'Orthopédie dento-faciale (Stomatologistes)', '14###R_0###': 'Orthopédiste (Chirurgien orthopédiste et traumatologue)', '45': 'Orthophoniste', '46': 'Orthoptiste', '47': 'Oto-Rhino-Laryngologue (ORL) et chirurgien cervico-facial', '4###R_0###': 'Pathologiste (Anatomo-Cyto-Pathologiste)', '48': 'Pédiatre', '49': 'Pédicure-podologue', '50': 'Pharmacien', '6###N_0###': 'Phlébologue (Angiologue)', '51': 'Phoniatre', '15###R_0###': 'Plasticien (Chirurgien plasticien)', '52': 'Pneumologue', '53': 'Psychiatres', '54': 'Radiologue', '55': 'Radiothérapeute', '5###R_0###': 'Réanimateur (Anesthésiste réanimateur)', '56': 'Réanimateur médical', '57': 'Rhumatologue', '58': 'Sage-femme', '37###R_0###': 'Santé publique (Médecin spécialiste en santé publique et médecine sociale)', '59': 'Spécialiste en médecine interne', '60': 'Spécialiste en médecine physique et de réadaptation', '39###R_0###': 'Sports (Médecine appliquée aux sports)', '61': 'Stomatologistes', '62': 'Taxi conventionné', '38###R_0###': 'Thermaliste (Médecin thermaliste)', '3###N_0###': 'Transport sanitaire (Ambulance /Véhicule sanitaire léger)', '14###R_1###': 'Traumatologue (Chirurgien orthopédiste et traumatologue)', '17###R_0###': 'Urologue (Chirurgien urologue)', '3###R_0###': 'Véhicule sanitaire léger (Ambulance /Véhicule sanitaire léger)', '21###R_0###': 'Vénérologue (Dermatologue et vénérologue)'}


catagorylist=['10','11','12','13','14','15',"16","17","18","19","20","20###R_0###","21","23###R_0###","40###N_0###","22","23","24","25","34###R_0###","26","27","28","29","30","32###R_0###","31","32","24###R_0###","50###R_0###","33","34","35","36","37","38","39","37###R_1###","40","41","42","43","44","61###N_0###","14###R_0###","45","46","47","4###R_0###","48","49","50","6###N_0###","51","15###R_0###","52","53","54","55","5###R_0###","56","57","58","37###R_0###","59","60","39###R_0###","61","62","38###R_0###","3###N_0###","14###R_1###","17###R_0###","3###R_0###","21###R_0###"]


def waitasec(val,debug=False):
    i=0
    while (i<=val):
        if(debug):
            print(i)
        i+=1


docdata=[]
explicit_timeout=10000
explicit_timecount=0
cangotonextpage=False
currentpage=1
completedpage=1
currentcatagory="1"
completedcatagory="1"


try:
    for cat in catagorylist:

        currentcatagory=cat

        browser = webdriver.Chrome()
        browser.get("http://annuairesante.ameli.fr")
        browser.find_element_by_id("buttonPS").click()
        #browser.find_element_by_id("formPro").click()

        browser.execute_script("document.getElementById('formProId').value = '{0}'; ".format(str(cat)))
        #print(browser.find_element_by_id("formProId").get_attribute("value"))
        waitasec(10000)

        # d="Acupuncteur"
        # for k in d:
        #     browser.find_element_by_id("formPro").send_keys(k)
        #     waitasec(10000)

        waitasec(1000)
        #print(browser.find_element_by_id("formProId").get_attribute("value"))
        browser.find_element_by_name("submit_final").click()

        waitasec(10000)
        waitasec(10000)
        time.sleep(3)
        sourcecode = browser.page_source
        totalpages=re.findall("[sur ]{4}[0-9]+",sourcecode)
        #print(totalpages)
        if(totalpages):
            totalpages=int(totalpages[0].split(" ")[1])
        else:
            totalpages=1
        print(catagorydict[cat]," has total ",totalpages," pages")
        for i in range(1,totalpages+1):
            cangotonextpage=False

            currentpage=i
            print("in page : ",i)

            while(not cangotonextpage):

                try:
                    browser.find_element_by_name("pageCible").click()
                    #browser.execute_script("document.getElementsByName('pageCible').value = '{0}'; ".format(str(i)))
                    browser.find_element_by_name("pageCible").send_keys(Keys.BACKSPACE)
                    browser.find_element_by_name("pageCible").send_keys(Keys.BACKSPACE)
                    browser.find_element_by_name("pageCible").send_keys(Keys.BACKSPACE)
                    browser.find_element_by_name("pageCible").send_keys(Keys.DELETE)
                    browser.find_element_by_name("pageCible").send_keys(Keys.DELETE)
                    browser.find_element_by_name("pageCible").send_keys(Keys.DELETE)
                    browser.find_element_by_name("pageCible").send_keys(str(i))
                    browser.find_element_by_name("pageCible").send_keys(Keys.RETURN)
                    cangotonextpage=True
                except Exception as e:

                    print("error occured while trying to go to next page")
                    print("Error : ",e)
                    cangotonextpage=False
                    #break

            soup = bs(sourcecode, "lxml")
            pagedoctors=soup.find_all("div",{ "class":"item-professionnel-inner"})

            while(len(pagedoctors)<1):
                sourcecode = browser.page_source
                soup = bs(sourcecode, "lxml")
                pagedoctors = soup.find_all("div", {"class": "item-professionnel-inner"})
                explicit_timecount += 1
                if (explicit_timecount > explicit_timeout):
                    break

            if(len(pagedoctors)>0):
                #print("found some doctors here")
                print("found {0} doctors in page {1} of catagory : {2}".format(len(pagedoctors),i,catagorydict[cat]))

                for doc in pagedoctors:
                    try:
                        doc_name=doc.find("div", "nom_pictos").find("a").text.strip()
                        tmpholder=doc.find("div","item left tel")
                        if(tmpholder):
                            doc_phno=tmpholder.text.strip()
                        else:
                            doc_phno="phone number not provided"
                        tmpholder=doc.find("div","item left adresse")
                        if(tmpholder):
                            doc_addr=tmpholder.text.strip()
                        else:
                            doc_addr="address not provided"
                        #print(doc_addr)

                        specialised_in=catagorydict[cat]

                        docdata.append([doc_name,specialised_in,doc_phno,doc_addr])
                        print("Extracting doc...")
                    except Exception as e:
                        print("error occures while extracting doctor data")
                        print("Error : ",e)
            else:
                print("could not find any doctors or may be internet connection is gone")

            completedpage=i


            #pass
        browser.quit()

        completedcatagory=cat

except Exception as e:
    print("error occured : ",e)
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(exc_type, fname, exc_tb.tb_lineno)
    try:
        #browser.quit()
        pass
    except:
        pass

    try:
        ff=open("status.txt","a")
        ff.write("\n\n")
        ff.write("{0}_{1}_{2}_{3}".format(currentcatagory,currentpage,completedcatagory,completedpage))
        ff.flush()
        ff.close()
    except Exception as e:
        print("error occured while writting status file")
        print("Error : ",e)




if(len(docdata)>0):
    try:
        f = open("doctor_list3.csv", 'w',newline='')
        writer = csv.writer(f)
        writer.writerow(["NAME","SPECIALISED IN","PHONE NUMBER","ADDRESS"])
        writer.writerow([" ", " ", " ", " "])
        for d in docdata:
            writer.writerow(d)


        f.flush()
        f.close()
    except:
        print("error while trying to write data to csv file")

        try:
            f.flush()
            f.close()
        except:
            pass

else:
    print("no data to write")

