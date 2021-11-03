'''

Nama    : Annissa Mutiaputri
no.ID   : 01123956110-20
Tema    : FGA Big Data Python

----------------
GAME PENJUMLAHAN
----------------
Sebuah permainan sederhana yang dibangun menggunakan Tkinter.
User menginput hasil penjumlahan dari 2 bilangan yang diacak antara 1-50.
User diharapkan untuk menjawab sebanyak-banyaknya dalam waktu 30 detik.

'''

#Library
import tkinter as tk
from tkinter import messagebox as mbox
from random import randint


#Class
class Game(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("GAME PENJUMLAHAN")
        self.bil=[0,0]
        self.benar=0
        self.after(1,self.start)
    def setfont(self,size=14):
        self.fontset = 'Helvetica '+str(size)
        return self.fontset
    def random_angka(self):
        for i in range(2):
            self.bil[i]=randint(1,50)
        self.jawaban_bener=self.bil[0]+self.bil[1]        
    def start(self):
        a = mbox.askquestion("GAME PENJUMLAHAN", "Selamat datang\nJumlahkan semua angkanya!\nWaktu : 30 detik\nSUDAH SIAP?")
        if a != 'yes':
            self.destroy()
        else:
            self.after(1,self.tampilan)              
    def ending(self):
        text = "WAKTU HABIS\nSkor kamu : {}\nTerimakasih telah bermain.".format(self.benar)
        a = mbox.showinfo("GAME PENJUMLAHAN", text)
        if a == 'ok': self.destroy()   
    def tampilan(self):
        self.after(30000,self.ending)
        self.random_angka()
        #row 0
        tk.Label(self,text='GAME PENJUMLAHAN',font = self.setfont(16)).grid(row=0,column=2,columnspan=3)
        #row 1
        tk.Label(self,text='Jumlah Benar : ',width=0,font = self.setfont(12)).grid(row=1,column=2,columnspan=2)
        self.jml_benar = tk.Entry(self,font = self.setfont,width=0)
        self.jml_benar.insert('end', self.benar)
        self.jml_benar.grid(row=1,column=4)
        self.jml_benar.bind('<Return>', self.proses)
        self.jml_benar.configure(state='readonly')
        #row 2
        tk.Label(self).grid(row=2)
        #row 3
        tk.Label(self, width=3).grid(row=3, column=0)                            #col 0 
        self.angk1 = tk.Entry(self,font = self.setfont,width=3)                  #col 1 (angka random 1)
        self.angk1.insert('end', self.bil[0])
        self.angk1.grid(row=3,column=1)
        self.angk1.bind('<Return>', self.proses)
        self.angk1.configure(state='readonly')
        tk.Label(self,text='+',font = self.setfont,width=3).grid(row=3,column=2) #col 2
        self.angk2 = tk.Entry(self,font = self.setfont,width=3)                  #col 3 (angka random 2)
        self.angk2.insert('end', self.bil[1])
        self.angk2.grid(row=3,column=3)                                          
        self.angk2.bind('<Return>', self.proses)
        self.angk2.configure(state='readonly')
        tk.Label(self,text='=',font = self.setfont,width=3).grid(row=3,column=4) #col 4
        self.jawab_box = tk.Entry(self,font = self.setfont,width=3)              #col 5 (Textbox Jawaban)
        self.jawab_box.grid(row=3,column=5)                                      
        self.jawab_box.bind('<Return>', self.proses)
        self.jawab_box.focus()
        tk.Label(self, width=3).grid(row=3, column=6)                            #col 6
        #row 4
        tk.Label(self).grid(row=4)
        #row 5
        tk.Label(self,text='** Tekan ENTER untuk menjawab **',font = self.setfont(12)).grid(row=5,columnspan=7)
    def proses(self,event=None):
        self.jawaban_input = self.jawab_box.get()
        if int(self.jawaban_input)==(self.jawaban_bener):
            self.benar+=1
            self.jawab_box.delete(0,'end')
            self.random_angka()
            self.angk1.configure(state='normal')
            self.angk2.configure(state='normal')
            self.jml_benar.configure(state='normal')
            self.angk1.delete(0,'end')
            self.angk2.delete(0,'end')
            self.jml_benar.delete(0,'end')
            self.angk1.insert('end', self.bil[0])
            self.angk2.insert('end', self.bil[1])
            self.jml_benar.insert('end', self.benar)
            self.angk1.configure(state='readonly')
            self.angk2.configure(state='readonly')
            self.jml_benar.configure(state='readonly')
        else:
            self.jawab_box.delete(0,'end')

#Main            
call=Game()
call.mainloop()
