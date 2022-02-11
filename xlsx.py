import requests

import xlsxwriter


class Excel:
    def __init__(self):
        self.workbook = xlsxwriter.Workbook(filename="filename")
        self.sheet = self.workbook.add_worksheet()

    def save(self):
        """
        Method for saving the workbook.
        """

        self.workbook.close()

    def _set_base_columns(self):
        """
        Method for setting the base (head) columns of the workbook.
        """

        title_format = self.workbook.add_format({"align": "center", "valign": "vcenter", "font_size": 10, "bold": 1})
        for col in range(0, 28):
            self.sheet.set_column(0, col, 20)
            self.sheet.set_row(0, col)

        self.sheet.write(0, 0, "Подкатегория 4", title_format)
        self.sheet.write(0, 1, "Картинка подкатегории 4", title_format)
        self.sheet.write(0, 2, "Подкатегория 3", title_format)
        self.sheet.write(0, 3, "Картинка подкатегории 3", title_format)
        self.sheet.write(0, 4, "Подкатегория 2", title_format)
        self.sheet.write(0, 5, "Картинка подкатегории 2", title_format)
        self.sheet.write(0, 6, "Подкатегория 1", title_format)
        self.sheet.write(0, 7, "Картинка подкатегории 1", title_format)
        self.sheet.write(0, 8, "Самая верхняя категория", title_format)
        self.sheet.write(0, 9, "Картинка самой верхней категории", title_format)
        self.sheet.write(0, 10, "Наименование", title_format)
        self.sheet.write(0, 11, "Артикул", title_format)
        self.sheet.write(0, 12, "url-артикул", title_format)
        self.sheet.write(0, 13, "Наименование с подклеенным артикулом", title_format)
        self.sheet.write(0, 14, "Главное фото", title_format)
        self.sheet.write(0, 15, "Другие фото", title_format)
        self.sheet.write(0, 16, "Основная цена", title_format)
        self.sheet.write(0, 17, "Описание", title_format)
        self.sheet.write(0, 18, "Характеристики опций", title_format)
        self.sheet.write(0, 19, "Колличество", title_format)
        self.sheet.write(0, 20, "Название опции-товара", title_format)
        self.sheet.write(0, 21, "Артикул опции-товара", title_format)
        self.sheet.write(0, 22, "Цена опций в Евро", title_format)
        self.sheet.write(0, 23, "Картинка опций", title_format)
        self.sheet.write(0, 24, "Колличество товаров в опции", title_format)
        self.sheet.write(0, 25, "Полный url товара", title_format)
        self.sheet.write(0, 26, "Производитель", title_format)
        self.sheet.write(0, 27, "Название характеристики 1", title_format)
        self.sheet.write(0, 28, "Значение характеристики 1", title_format)
        self.sheet.write(0, 29, "Название характеристики 2", title_format)
        self.sheet.write(0, 30, "Значение характеристики 2", title_format)
        self.sheet.write(0, 31, "Название характеристики 3", title_format)
        self.sheet.write(0, 32, "Значение характеристики 3", title_format)
        self.sheet.write(0, 33, "Название характеристики 4", title_format)
        self.sheet.write(0, 34, "Значение характеристики 4", title_format)
        self.sheet.write(0, 35, "Название характеристики 5", title_format)
        self.sheet.write(0, 36, "Значение характеристики 5", title_format)
        self.sheet.write(0, 37, "Название характеристики 6", title_format)
        self.sheet.write(0, 38, "Значение характеристики 6", title_format)
        self.sheet.write(0, 39, "Название характеристики 7", title_format)
        self.sheet.write(0, 40, "Значение характеристики 7", title_format)
        self.sheet.write(0, 41, "Название характеристики 8", title_format)
        self.sheet.write(0, 42, "Значение характеристики 8", title_format)
        self.sheet.write(0, 43, "Название характеристики 9", title_format)
        self.sheet.write(0, 44, "Значение характеристики 9", title_format)
        self.sheet.write(0, 45, "Название характеристики 10", title_format)
        self.sheet.write(0, 46, "Значение характеристики 10", title_format)
        self.sheet.write(0, 47, "Название характеристики 11", title_format)
        self.sheet.write(0, 48, "Значение характеристики 11", title_format)
        self.sheet.write(0, 49, "Название характеристики 12", title_format)
        self.sheet.write(0, 50, "Значение характеристики 12", title_format)
        self.sheet.write(0, 51, "Название характеристики 13", title_format)
        self.sheet.write(0, 52, "Значение характеристики 13", title_format)
        self.sheet.write(0, 53, "Название характеристики 14", title_format)
        self.sheet.write(0, 54, "Значение характеристики 14", title_format)
        self.sheet.write(0, 55, "Название характеристики 15", title_format)
        self.sheet.write(0, 56, "Значение характеристики 15", title_format)
        self.sheet.write(0, 57, "Название характеристики 16", title_format)
        self.sheet.write(0, 58, "Значение характеристики 16", title_format)
        self.sheet.write(0, 59, "Название характеристики 17", title_format)
        self.sheet.write(0, 60, "Значение характеристики 17", title_format)
        self.sheet.write(0, 61, "Название характеристики 18", title_format)
        self.sheet.write(0, 62, "Значение характеристики 18", title_format)
        self.sheet.write(0, 63, "Название характеристики 19", title_format)
        self.sheet.write(0, 64, "Значение характеристики 19", title_format)
        self.sheet.write(0, 65, "Название характеристики 20", title_format)
        self.sheet.write(0, 66, "Значение характеристики 20", title_format)


class KExcel(Excel):
    def __init__(self, filename: str, data: list, prices: list):
        """
        Object used for creating, editing and saving excel documents.

        :param filename: The full file name (with format at the end. Example: foo.xlsx).
        :param data: The full data list with json of parameters
        """

        self.workbook = xlsxwriter.Workbook(filename="karauta_{}".format(filename))
        self.proces = prices
        self.sheet = self.workbook.add_worksheet()
        self._set_base_columns()
        self.write_products(data)

    def write_products(self, products: list):

        """
        Method for writing the products into the sheet.

        :param products: The list of the products.
        """

        last_row: int = 1

        for x in products:
            print(x)
            r = requests.get("https://www.k-rauta.fi/api/product/{}".format(x), headers={
                "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15"
                              " (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
            })

            if r.status_code == 404:
                continue

            r = r.json()
            try:
                self.sheet.write(last_row, 8, r["categories"][0]["name"])
            except IndexError:
                pass
            try:
                self.sheet.write(last_row, 6, r["categories"][1]["name"])
            except IndexError:
                pass
            try:
                self.sheet.write(last_row, 4, r["categories"][2]["name"])
            except IndexError:
                pass
            self.sheet.write(last_row, 10, r["name"])
            self.sheet.write(last_row, 11, r["ean"])
            self.sheet.write(last_row, 12, "/"+r["name"].replace(u" ", "-")+"/"+r["ean"])
            self.sheet.write(last_row, 13, r["name"] + " " + r["ean"])
            self.sheet.write(last_row, 14, r["images"][0]["url"])

            if len(r["images"]) >= 2:
                img_str = ""
                for i in range(1, len(r["images"])):
                    try:
                        img_str += r["images"][i]["url"]+";"
                    except IndexError:
                        pass
                self.sheet.write(last_row, 15, img_str)
            self.sheet.write(last_row, 16, self.proces[last_row-1])
            try:
                self.sheet.write(last_row, 17, r["descriptionLong"])
            except KeyError:
                try:
                    self.sheet.write(last_row, 17, r["description"])
                except KeyError:
                    pass
            self.sheet.write(last_row, 25, "https://www.k-rauta.fi/tuote/"+r["name"].replace(u" ", "-")+"/"+r["ean"])
            try:
                self.sheet.write(last_row, 26, r["brandName"])
            except KeyError:
                pass
            last_row += 1
