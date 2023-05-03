import functools

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5 import QtWidgets

from gui import Ui_Dialog

class GuiProgram(Ui_Dialog):

    def __init__(self, dialog):
        Ui_Dialog.__init__(self)              # Initialize Window
        self.setupUi(dialog)                  # Set up the UI

        self.frequency_peak = list(range(0,10))
        self.gamma_peak = list(range(10,20))

        self.initialize_table()

        self.pushButton.clicked.connect(self.table)

    # Инициализация: Пустая таблица
    def initialize_table(self):
        self.tableWidget.clear()
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["Частота МГц", "Гамма", ""])
        self.tableWidget.horizontalHeaderItem(0).setTextAlignment(Qt.AlignHCenter)
        self.tableWidget.horizontalHeaderItem(1).setTextAlignment(Qt.AlignHCenter)


    # РАБОТА С ТАБЛИЦЕЙ
    # Основная программа - (4.1) Заполение таблицы
    def table(self):
        # Задаем кол-во столбцов и строк
        self.tableWidget.setRowCount(len(self.frequency_peak))
        self.tableWidget.setColumnCount(3)

        # Задаем название столбцов
        self.tableWidget.setHorizontalHeaderLabels(["Частота МГц", "Гамма"])

        # Заполняем таблицу
        index = 0
        for f, g in zip(self.frequency_peak, self.gamma_peak):
            # значения частоты и гаммы для 0 и 1 столбца
            self.tableWidget.setItem(index, 0, QTableWidgetItem(str('%.3f' % f)))
            self.tableWidget.setItem(index, 1, QTableWidgetItem(str('%.7E' % g)))

            # Элемент 2 столбца - checkbox, сохранения данных
            check_box = QtWidgets.QCheckBox()  # Создаем объект чекбокс
            check_box.setCheckState(Qt.Checked)  # Задаем состояние - нажат
            # Обработчик нажатия, с передачей отправителя
            check_box.toggled.connect(
                functools.partial(
                    self.frequency_selection, check_box
                )
            )
            self.tableWidget.setCellWidget(index, 2, check_box)  # Вводим в таблицу

            index += 1

        # Размеры строк выровнять под содержимое
        self.tableWidget.resizeColumnsToContents()

    def frequency_selection(self, sender=None):
        print(sender)