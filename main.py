from tkinter import *
from tkinter import TclError
import threading
import time

def about():
    print("A")


def destroy_windows():
    launch_karauta.destroy()
    launch_ikea.destroy()
    launch_verka.destroy()
    launch_biltema.destroy()
    karauta_urls.destroy()
    biltema_urls.destroy()
    ikea_urls.destroy()
    verka_urls.destroy()
    run_btn.destroy()
    about_btn.destroy()


def destroy_labels(labels: list):
    for label in labels:
        label.destroy()


def run():
    from karauta_main import main
    k_urls = karauta_urls.get()
    destroy_windows()

    threads = []
    status_label = Label(window, text="Паршу сайт K-RAUTA")
    status_label.grid(row=1, column=1)
    window.update()
    status_labels = []
    if k_urls != "":
        if k_urls.find(";") != -1:
            k_urls_list = k_urls.split(";")
            for link in k_urls_list:
                if link != "" and link != "\n":
                    status_labels.append(Label(window, text=f"Ссылка: {link}", bg="#FFA500"))
            row = 2
            for label in status_labels:
                label.grid(row=row, column=1)
                row += 1

            num = 0
            window.update()
            for z in k_urls_list:
                if z != "" and z != "\n":
                    name = z.split("/")[-1]
                    try:
                        main(z, name)
                        status_labels[num].config(bg="#00ff00")
                        window.update()
                        window.update()
                    except Exception as e:
                        print(e.__class__.__name__)
                        status_labels[num].config(bg="#FF0000")
                    num += 1
            window.update()
        else:
            name = k_urls.split("/")[-1]
            main(k_urls, name)


if __name__ == '__main__':
    window = Tk()
    window.title("Парсеры Финских сайтов by DMT")

    karauta_urls = Entry(window)
    launch_karauta = Label(window, text="Ссылки карауты")
    biltema_urls = Entry(window)
    launch_biltema = Label(window, text="Ссылки Билтемы")
    ikea_urls = Entry(window)
    launch_ikea = Label(window, text="Ссылки Икеи")
    verka_urls = Entry(window)
    launch_verka = Label(window, text="Ссылки Веркаупы")

    run_btn = Button(window, text="Запустить", command=lambda: run())

    about_btn = Button(window, text="Версия", command=lambda: about)

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
