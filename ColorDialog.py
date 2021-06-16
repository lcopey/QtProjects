from PyQt5.QtWidgets import QApplication, QMainWindow, QColorDialog, QDialog, QComboBox, QLabel, QVBoxLayout, \
    QHBoxLayout, QDialogButtonBox
import sys


class ColorDialog(QColorDialog):
    def __init__(self):
        super(ColorDialog, self).__init__()
        self.setOptions(QColorDialog.NoButtons)
        layout = self.layout()

        line_style = QComboBox()
        line_style.addItem('dash')
        line_style.addItem('line')
        line_style_text = QLabel('Line style :')
        inner = QHBoxLayout()
        inner.addStretch()
        inner.addWidget(line_style_text)
        inner.addWidget(line_style)
        layout.addLayout(inner)

        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        self.button_box.clicked.connect(self.accept)
        self.button_box.clicked.connect(self.reject)
        layout.addWidget(self.button_box)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wdg = ColorDialog()
    res = wdg.exec_()
    print(res)
    sys.exit(app.exec_())
