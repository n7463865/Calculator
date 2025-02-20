import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLineEdit, QPushButton

class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        # Configuração da janela
        self.setWindowTitle('Calculadora')
        self.setGeometry(300, 300, 400, 300)

        # Layout principal (Grid Layout)
        self.layout = QGridLayout()

        # Tela de exibição
        self.display = QLineEdit(self)
        self.display.setReadOnly(True)
        self.layout.addWidget(self.display, 0, 0, 1, 4)

        # Botões da calculadora
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]
        
        # Adicionar os botões ao layout
        for button_text, row, col in buttons:
            button = QPushButton(button_text)
            button.clicked.connect(self.on_button_click)
            self.layout.addWidget(button, row, col)

        # Botão de limpar
        self.clear_button = QPushButton('C')
        self.clear_button.clicked.connect(self.clear_display)
        self.layout.addWidget(self.clear_button, 5, 0, 1, 4)

        # Configurar o layout da janela
        self.setLayout(self.layout)

    def on_button_click(self):
        sender = self.sender()
        current_text = self.display.text()
        button_text = sender.text()

        if button_text == '=':
            try:
                result = eval(current_text)
                self.display.setText(str(result))
            except Exception:
                self.display.setText("Erro")
        else:
            self.display.setText(current_text + button_text)

    def clear_display(self):
        self.display.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())