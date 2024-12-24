import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLineEdit, QVBoxLayout, QListWidget

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.previous_answers = []
        self.initUI()

    def initUI(self):
        self.setWindowTitle('calc')
        self.setGeometry(300, 300, 300, 500)
        layout = QVBoxLayout()
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        layout.addWidget(self.display)
        buttons_layout = QGridLayout()
        buttons = ['7', '8', '9', '/',
                   '4', '5', '6', '*',
                   '1', '2', '3', '-',
                   '0', '.', '=', '+']

        for i, button_text in enumerate(buttons):
            row = i // 4
            col = i % 4
            btn = QPushButton(button_text)
            btn.clicked.connect(self.buttonClicked)
            buttons_layout.addWidget(btn, row, col)
        layout.addLayout(buttons_layout)
        clear_btn = QPushButton('C')
        clear_btn.clicked.connect(self.clear)
        layout.addWidget(clear_btn)
        self.history_list = QListWidget()
        self.history_list.setMaximumHeight(100)
        layout.addWidget(self.history_list)

        self.setLayout(layout)

    def buttonClicked(self):
        sender = self.sender()
        if sender.text() == '=':
            self.calculate()
        else:
            current = self.display.text()
            self.display.setText(current + sender.text())

    def calculate(self):
            result = eval(self.display.text())
            self.display.setText(str(result))
            self.add_to_history(result)

    def clear(self):
        self.display.clear()
        self.update_history_display()

    def add_to_history(self, result):
        self.previous_answers.append(str(result))
        if len(self.previous_answers) > 5:
            self.previous_answers.pop(0)
        self.update_history_display()

    def update_history_display(self):
        self.history_list.clear()
        for answer in reversed(self.previous_answers):
            self.history_list.addItem(answer)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
