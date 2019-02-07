import sys
from PyQt5.QtCore import QRect, QCoreApplication
from PyQt5.QtWidgets import QSizePolicy, QWidget, QPushButton, QStatusBar, QMenuBar, \
    QLabel, QLineEdit, QTextEdit, QTableWidget, QMainWindow, QApplication, QDialog, QTableWidgetItem
from PyQt5.QtCore import Qt, QMetaObject, QSize


class UiMainWindow(object):
    def setup_ui(self, main_window):
        main_window.setObjectName("MainWindow")
        main_window.resize(936, 560)

        self.status_bar = QStatusBar(main_window)
        self.central_widget = QWidget(main_window)

        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(main_window.sizePolicy().hasHeightForWidth())
        main_window.setSizePolicy(sizePolicy)
        main_window.setTabletTracking(True)

        self.button_open_file = QPushButton(self.central_widget)
        self.button_open_file.setGeometry(QRect(380, 10, 101, 25))

        self.input_name_of_file = QLineEdit(self.central_widget)
        self.input_name_of_file.setGeometry(QRect(130, 10, 231, 25))

        self.comment_for_input_name_file = QLabel(self.central_widget)
        self.comment_for_input_name_file.setGeometry(QRect(10, 20, 131, 17))

        self.input_replacement_symbol = QLineEdit(self.central_widget)
        self.input_replacement_symbol.setGeometry(QRect(310, 40, 171, 25))
        self.input_replacement_symbol.setText("")

        self.input_text = QTextEdit(self.central_widget)
        self.input_text.setGeometry(QRect(10, 70, 471, 421))

        self.comment_for_input_name_rep_sym = QLabel(self.central_widget)
        self.comment_for_input_name_rep_sym.setGeometry(QRect(10, 50, 301, 16))

        self.table_of_replacements = QTableWidget(self.central_widget)
        self.table_of_replacements.setGeometry(QRect(530, 40, 391, 461))

        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_of_replacements.sizePolicy().hasHeightForWidth())

        self.table_of_replacements.setSizePolicy(sizePolicy)
        self.table_of_replacements.setSizeIncrement(QSize(0, 0))
        self.table_of_replacements.setFocusPolicy(Qt.StrongFocus)
        self.table_of_replacements.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.table_of_replacements.setAcceptDrops(False)
        self.table_of_replacements.setColumnCount(1)
        self.table_of_replacements.setRowCount(0)
        self.table_of_replacements.horizontalHeader().setDefaultSectionSize(388)
        self.table_of_replacements.setHorizontalHeaderLabels(['Value for replacement'])

        self.comment_for_rep_tab = QLabel(self.central_widget)
        self.comment_for_rep_tab.setGeometry(QRect(530, 10, 241, 17))

        self.button_start = QPushButton(self.central_widget)
        self.button_start.setGeometry(QRect(840, 510, 80, 25))

        self.button_continue = QPushButton(self.central_widget)
        self.button_continue.setGeometry(QRect(400, 510, 80, 25))

        self.comment_for_button_continue = QLabel(self.central_widget)
        self.comment_for_button_continue.setGeometry(QRect(80, 510, 301, 20))

        self.menu_bar = QMenuBar(main_window)
        self.menu_bar.setGeometry(QRect(0, 0, 936, 22))

        main_window.setCentralWidget(self.central_widget)
        main_window.setMenuBar(self.menu_bar)
        main_window.setStatusBar(self.status_bar)

        self.retranslate_ui(main_window)

        QMetaObject.connectSlotsByName(main_window)

    def retranslate_ui(self, main_window):
        _translate = QCoreApplication.translate
        main_window.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_open_file.setText(_translate("MainWindow", "Открыть файл"))
        self.comment_for_input_name_file.setText(_translate("MainWindow", "Введите имя файла:"))
        self.comment_for_input_name_rep_sym.setText(_translate("MainWindow",
                                                               "Введите символ /"
                                                               " символы которые будут заменены:"))
        self.comment_for_rep_tab.setText(_translate("MainWindow", "Введите текст для каждой замены"))
        self.button_start.setText(_translate("MainWindow", "Start"))
        self.button_continue.setText(_translate("MainWindow", "Continue"))
        self.comment_for_button_continue.setText(_translate("MainWindow",
                                                            "Нажмите на кнопку, когда текст будет подготовлен"))


class UiDialog(object):
    def setup_ui(self, dialog):
        dialog.setObjectName("Dialog")
        dialog.resize(582, 504)

        self.comment_for_output = QLabel(dialog)
        self.comment_for_output.setGeometry(QRect(20, 10, 71, 17))

        self.button_save = QPushButton(dialog)
        self.button_save.setGeometry(QRect(500, 470, 71, 25))

        self.input_save_file_name = QLineEdit(dialog)
        self.input_save_file_name.setGeometry(QRect(280, 470, 211, 25))

        self.comment_for_save_name = QLabel(dialog)
        self.comment_for_save_name.setGeometry(QRect(30, 470, 241, 17))

        self.output = QTextEdit(dialog)
        self.output.setGeometry(QRect(20, 40, 551, 411))

        self.retranslate_ui(dialog)
        QMetaObject.connectSlotsByName(dialog)

    def retranslate_ui(self, dialog):
        _translate = QCoreApplication.translate
        dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.comment_for_output.setText(_translate("Dialog", "Результат:"))
        self.button_save.setText(_translate("Dialog", "Save"))
        self.comment_for_save_name.setText(_translate("Dialog", "Название файла, по умолчанию res.txt"))


class ResWindow(QDialog, UiDialog):
    def __init__(self, root):
        super().__init__()
        self.root = root
        self.setup_ui(self)
        self.output.setText(self.root.output_text)
        self.button_save.clicked.connect(self.save)

    def save(self):
        name_of_file = self.input_save_file_name.text()

        if not name_of_file:
            name_of_file = 'res.txt'

        with open(name_of_file, 'w') as out:
            print(self.root.output_text, file=out)


class MyWidget(QMainWindow, UiMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui(self)
        self.text_editor = QTextEdit()
        self.button_open_file.clicked.connect(self.open_file)
        self.button_start.clicked.connect(self.create_res)
        self.button_continue.clicked.connect(self.create_replacements)
        self.replacement_symbol = self.text = self.output_text = ''
        self.list_of_replacement = []

    def open_file(self):
        name_of_file = self.input_name_of_file.text()

        try:
            text = open(name_of_file).read()

        except FileNotFoundError:
            text = 'You found a fitch, not a bag'

        self.input_text.setText(text)

    def create_res(self):
        self.create_output_text()
        res = ResWindow(self)
        res.exec()

    def create_replacements(self):
        self.table_of_replacements.clear()
        self.table_of_replacements.setHorizontalHeaderLabels(['Value for replacement'])
        self.table_of_replacements.setRowCount(0)
        self.text = self.input_text.toPlainText()
        self.replacement_symbol = self.input_replacement_symbol.text()
        if not self.replacement_symbol:
            pass

        else:
            for _ in range(self.text.count(self.replacement_symbol)):
                text = QTableWidgetItem(self.text_editor.toPlainText())
                self.table_of_replacements.insertRow(self.table_of_replacements.rowCount())
                self.table_of_replacements.setItem(_, 0, text)

    def create_output_text(self):
        self.output_text = self.text

        for _ in range(self.table_of_replacements.rowCount()):
            elem = self.table_of_replacements.item(_, 0).text()
            self.output_text = self.output_text.replace(self.replacement_symbol, elem, 1)


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
