from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Adj meg egy elérési útvonalat a chromedriver.exe fájlhoz
service = Service("c:/Users/feher/OneDrive/Dokumentumok/Nyíregyházi Egyetem - PTI/Programozas/Python/AutoGoogleSearch_Selenium/chromedriver-win64/chromedriver.exe")

# Böngésző opciók beállítása
options = Options()

# Chrome böngésző megnyitása a megfelelő Service és Options osztállyal
browser = webdriver.Chrome(service=service, options=options)

# Felhasználói bemenet
search_string = input("Input the URL or string you want to search for: ")

# A szöveg struktúrába állítása a keresési URL-hez
search_string = search_string.replace(' ', '+')

# Google keresési URL megnyitása
browser.get("https://www.google.com/search?q=" + search_string)

# Várj, amíg a felhasználó be nem zárja a böngészőt
input("Nyomj meg egy gombot a program befejezéséhez...")
browser.quit()  # Böngésző bezárása, ha a felhasználó megnyomta a gombot
