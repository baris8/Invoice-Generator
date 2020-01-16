import csv
from selenium import webdriver
import time as t
import K


def prepare(driver):
    driver.find_element_by_name("invoice_logo").clear()
    driver.find_element_by_name("invoice_logo").send_keys("Rechnung")

    driver.find_element_by_name("invoice_logosubline").clear()

    driver.find_element_by_name("invoice_absenderzeile").clear()
    driver.find_element_by_name("invoice_absenderzeile").send_keys(K.meine_adresse)

    driver.find_element_by_name("invoice_unternehmensinformationen").clear()
    driver.find_element_by_name("invoice_unternehmensinformationen").send_keys(K.erreichbar)
    ######################################
    driver.find_element_by_name("invoice_dokumentennummer").clear()
    driver.find_element_by_name("invoice_kundennummer").clear()
    driver.find_element_by_name("invoice_datum").clear()
    driver.find_element_by_name("invoice_einleitungstext").clear()

    driver.find_element_by_name("invoice_zahlungsbedingungen").clear()
    driver.find_element_by_name("invoice_zahlungsbedingungen").send_keys(K.text)

    driver.find_element_by_name("invoice_schlusstext").clear()
    #########################################
    driver.find_element_by_name("invoice_footerbox1").clear()
    driver.find_element_by_name("invoice_footerbox1").send_keys(K.foot_one)
    driver.find_element_by_name("invoice_footerbox2").clear()
    driver.find_element_by_name("invoice_footerbox2").send_keys(K.foot_two)
    driver.find_element_by_name("invoice_footerbox3").clear()
    driver.find_element_by_name("invoice_footerbox3").send_keys(K.foot_three)

    driver.find_element_by_name("invoice_page").clear()

def fill_data(driver, datum, adresse, bezeichnung, netto, nr):
    driver.find_element_by_name("invoiceitems_beschreibung[1]").clear()
    driver.find_element_by_name("invoiceitems_beschreibung[1]").send_keys(bezeichnung)

    driver.find_element_by_name("invoiceitems_einzelpreis[1]").clear()
    driver.find_element_by_name("invoiceitems_einzelpreis[1]").send_keys(netto)

    driver.find_element_by_name("invoice_empfaenger").clear()
    driver.find_element_by_name("invoice_empfaenger").send_keys(adresse)

    dokument_nr = K.rechnung_nr + str(nr).zfill(3)
    driver.find_element_by_name("invoice_dokumentennummer").clear()
    driver.find_element_by_name("invoice_dokumentennummer").send_keys(dokument_nr)

    driver.find_element_by_name("invoice_datum").clear()
    driver.find_element_by_name("invoice_datum").send_keys(K.datum + datum)


# opens chrome with the needed url
driver = webdriver.Chrome()
url = "https://rechnungen-muster.de/rechnung-schreiben#rechnung-schreiben"
driver.get(url)

t.sleep(2)

prepare(driver)


print("Bitte ändere die nötigen Angaben einmalig. Lösch die 2. Zeile in der Beschreibung auf der Seite")
input("Wenn die Vorbereitungen abgeschlossen sind drücke Enter\nVergiss nicht die Anzahl auf 1 zu setzten!")

with open("august.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    line_count = 0

    for row in csv_reader:
        if line_count == 0:
            datum = row[0]
            netto = row[7]
            adresse = row[-3]
            bezeichnung = row[-2]
            print(datum + " " + netto + " " + adresse + " " + bezeichnung)
        else:
            datum = row[0]
            netto = row[7]
            adresse = row[-3]
            bezeichnung = row[-2]
            fill_data(driver, datum, adresse, bezeichnung, netto, line_count)

            driver.find_element_by_class_name("button-gen").click()
            print(datum + " " + netto + " " + adresse + " " + bezeichnung)


        line_count += 1
