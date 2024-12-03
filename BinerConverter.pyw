from fungsi2 import convertIterative,convertRecursive
import customtkinter
from CustomTkinterMessagebox import CTkMessagebox
import time

window = customtkinter.CTk()
window.geometry("700x450")
window.resizable(False,False)
window.title("Binary Convarter App")

ANGKA = customtkinter.IntVar()

def RecursiveExecute():
    """Memunculkan message box yang menampilkan hasil konversi bilangan desimal menjadi biner dengan metode rekursif"""
    
    if (ANGKA.get() < 0):
        CTkMessagebox.messagebox(title="error message",text="Masukan harus bilangan bulat positif")
    else:
        start = time.perf_counter_ns()
        biner = convertRecursive(angka=ANGKA.get())
        duration = time.perf_counter_ns() - start
        pesan = f"Hasil konversi = {biner}\nmembutuhkan waktu sebanyak: {duration:.2f} ns"
        CTkMessagebox.messagebox(title="Hasil konversi (Rekursif)",text=pesan,size="600x200")

def IterativeExecute():
    """Memunculkan message box yang menampilkan hasil konversi bilangan desimal menjadi biner dengan metode iteratif"""
    
    if (ANGKA.get() < 0):
        CTkMessagebox.messagebox(title="error message",text="Masukan harus bilangan bulat positif")
    else:
        start = time.perf_counter_ns()
        biner = convertIterative(angka=ANGKA.get())
        duration = time.perf_counter_ns() - start
        pesan = f"Hasil konversi = {biner}\nmembutuhkan waktu sebanyak: {duration:.2f} ns"
        CTkMessagebox.messagebox(title="Hasil konversi (Rekursif)",text=pesan,size="600x200")


Header = customtkinter.CTkLabel(window,text="Program Konversi Desimal ke Biner",text_color="lightblue",font = customtkinter.CTkFont("System",35))
Header.pack(pady = 10)

Frame = customtkinter.CTkFrame(master=window,height=400,width=400,border_color="lightblue",border_width=5)
Frame.pack(padx = 10,pady=30, fill = "x")

Label1 = customtkinter.CTkLabel(master=Frame,text="Masukkan bilangan bulat positif (dalam desimal): ",font=customtkinter.CTkFont("Times",20))
Label1.pack(fill = "x",padx = 10,pady = 10, expand = True)

Entry1 = customtkinter.CTkEntry(master=Frame,textvariable=ANGKA,font=customtkinter.CTkFont("Times",20))
Entry1.pack(fill = "x",padx = 10,pady = 10, expand = True)


buttonRecursive = customtkinter.CTkButton(Frame, text="konversi mode rekusif", command=RecursiveExecute)
buttonRecursive.pack(padx = 20,pady = 10)

buttonIterative = customtkinter.CTkButton(Frame, text="konversi mode iterative", command=IterativeExecute)
buttonIterative.pack(padx = 20,pady = 20)

akhir1 = customtkinter.CTkLabel(window,text="Dibuat oleh:",text_color="lightblue",font = customtkinter.CTkFont("System",20))
akhir1.pack(pady = 1)

akhir2 = customtkinter.CTkLabel(window,text="Rayya Syauqi Alulu'i (103012300268)",text_color="lightblue",font = customtkinter.CTkFont("System",20))
akhir2.pack(pady = 1)

akhir3 = customtkinter.CTkLabel(window,text="Ridwan Ramdhani (103012300191)",text_color="lightblue",font = customtkinter.CTkFont("System",20))
akhir3.pack(pady = 1)


window.mainloop()
