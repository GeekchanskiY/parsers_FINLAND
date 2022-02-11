from tkinter import *
from tkinter import messagebox

def about():
    print("A")


def run():
    print("YAY")


if __name__ == '__main__':
    window = Tk()
    window.title("Парсеры Финских сайтов")

    karauta_urls = Entry(window)
    launch_karauta = Label(window, text="Ссылки карауты")
    biltema_urls = Entry(window)
    launch_biltema = Label(window, text="Ссылки Билтемы")
    ikea_urls = Entry(window)
    launch_ikea = Label(window, text="Ссылки Икеи")
    verka_urls = Entry(window)
    launch_verka = Label(window, text="Ссылки Веркаупы")

    run_btn = Button(window, text="Запустить", command=run)

    about_btn = Button(window, text="Версия", command=about)

    karauta_urls.grid(row=1, column=3, padx=20, pady=10)
    launch_karauta.grid(row=1, column=1, padx=20, pady=10)
    biltema_urls.grid(row=2, column=3, padx=20, pady=10)
    launch_biltema.grid(row=2, column=1, padx=20, pady=10)
    ikea_urls.grid(row=3, column=3, padx=20, pady=10)
    launch_ikea.grid(row=3, column=1, padx=20, pady=10)
    verka_urls.grid(row=4, column=3, padx=20, pady=10)
    launch_verka.grid(row=4, column=1, padx=20, pady=10)

    about_btn.grid(row=6, column=3, padx=20, pady=20)
    run_btn.grid(row=6, column=1, padx=20, pady=20)
    window.mainloop()
