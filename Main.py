from selenium import webdriver
import winsound
import time
import re

# Liste de vélos intéressants
urls_to_check = ['https://www.decathlon.fr/p/velo-vtt-electrique-e-st-900-27-5-plus/_/R-p-168875',
                 'https://www.decathlon.fr/p/velo-vtt-electrique-e-st-520-gris-jaune-27-5/_/R-p-311400',
                 'https://www.decathlon.fr/p/velo-vtt-electrique-e-st-900-femme-turquoise-27-5/_/R-p-308514'
                 ]

seek_duration = 3  # Number of hours of run

for i in range(int(seek_duration * 60)):
    for url in urls_to_check:
        # Open a wed driver and get the sourcecode of the website
        wd = webdriver.Chrome()
        wd.get(url)
        html_page = wd.page_source
        wd.quit()

        ## If the product has only one possible size or color
        dispos = [m.start() for m in re.finditer("https://schema.org/InStock", html_page)]
        if dispos != []:
            winsound.Beep(700, 1000)
            print(url, "est diponible!!!")

        ## If there are different sizes for the product
        # indispos = [m.start() for m in re.finditer("https://schema.org/OutOfStock", html_page)]
        # dispos = [m.start() for m in re.finditer("https://schema.org/InStock", html_page)]
        # list_dispo = [(j, "dispo") for j in dispos] + [(j, "non dispo") for j in indispos]
        # list_dispo.sort(key=lambda pair: pair[0])
        # if list_dispo[1][1] == "dispo":
        #     winsound.Beep(700, 1000)
        #     print(url, "est diponible en taille M")

    # Wait one minute before next iteration
    time.sleep(60)
