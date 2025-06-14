import tkinter as tk

pencere=tk.Tk()

####


label=tk.Label(text='Sayilari giriniz',)
label.pack()
entry1=tk.Entry()
entry1.pack()



entry2=tk.Entry()
entry2.pack()


sonuc_labeli=tk.Label()

def toplama():
    sayi1 = float(entry1.get())
    sayi2 = float(entry2.get())
    print(sayi1 + sayi2)
    sonuc = sayi1 + sayi2
    sonuc_labeli.config(text=f'Sonuc : {sonuc}')


def cikarma():
    sayi1 = float(entry1.get())
    sayi2 = float(entry2.get())
    if sayi1 - sayi2!=0:
        print(sayi1 - sayi2)
        sonuc = sayi1 - sayi2
        sonuc_labeli.config(text=f'Sonuc : {sonuc}')
    else:
        sonuc_labeli.config(text='Duzgun yaz sikmeyim seni simdi')


def bolme():
    sayi1 = float(entry1.get())
    sayi2 = float(entry2.get())
    print(sayi1 / sayi2)
    sonuc = sayi1 / sayi2
    sonuc_labeli.config(text=f'Sonuc : {sonuc} ')


def carpma():
    sayi1 = float(entry1.get())
    sayi2 = float(entry2.get())
    print(sayi1 * sayi2)
    sonuc = sayi1 * sayi2
    sonuc_labeli.config(text=f'Sonuc : {sonuc} ')



buton_toplama=tk.Button(text='toplama',command=toplama)
buton_cikarma=tk.Button(text='cikarma',command=cikarma)
buton_bolme=tk.Button(text='bolme',command=bolme)
buton_carpma=tk.Button(text='carpma',command=carpma)

buton_toplama.pack()
buton_cikarma.pack()
buton_bolme.pack()
buton_carpma.pack()


sonuc_labeli.pack()



####

pencere.mainloop()