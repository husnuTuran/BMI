from tkinter import *
screen = Tk()
screen.title('VKİ Hesaplayıcı')
screen.minsize(width=200, height=170)

weight_label = Label(text='Kilonuzu Giriniz (kg)')
weight_label.pack()

weight_entry = Entry()
weight_entry.pack()

length_label = Label(text='Boyunuzu Giriniz (cm)')
length_label.pack()

length_entry = Entry()
length_entry.pack()


def calculate():
    try:
        kilo = int(weight_entry.get())
        boy = int(length_entry.get())
        result_label['text'] = f'Kilo: {kilo}'
        result_label['text'] = f'Boy: {boy}'
        vki = round((kilo / ((boy * boy) / 10000)), 1)
        print(vki)

        if vki < 18.5:
            result_label['text'] = f'Sonuç: {vki} (Zayıfsınız)'
        elif vki >18.5 and vki < 24.9:
            result_label['text'] = f'Sonuç: {vki} (Kilonuz Normal)'
        elif vki >25 and vki < 29.9:
            result_label['text'] = f'Sonuç: {vki} (Fazla kilolosunuz)'
        elif vki > 30 and vki < 34.9:
            result_label['text'] = f'Sonuç: {vki} (Şişmansınız (1. Derece Obez))'
        elif vki >35 and vki < 39.9:
            result_label['text'] = f'Sonuç: {vki} (Obezsiniz (2. Derece Obez)'
        elif vki >40:
            result_label['text'] = f'Sonuç: {vki} (Aşırı şişmazsınız (3. Derece Obez)'
    except ValueError:
        result_label['text'] = 'Lütfen değerleri doğru giriniz!!'


button = Button(text='Hesapla', command=calculate)
button.pack()

result_label = Label(screen, text='')
result_label.pack()

screen.mainloop()