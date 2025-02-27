import random

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QBoxLayout, QWidget, QVBoxLayout

app = QApplication([])
my_win = QWidget()
my_win.setWindowTitle("Ho Quoc Duy")
my_win.resize(400, 200)
my_win.move(100,100)

################ Widgets #############
text = QLabel("Click to find out to winner")
generate_btn = QPushButton("Generate")
winner_lbl = QLabel("?")
###############################################


# Layout ##########################
layout_v = QVBoxLayout()
layout_v.addWidget(text, alignment=Qt.AlignCenter)
layout_v.addWidget(winner_lbl, alignment=Qt.AlignCenter)
layout_v.addWidget(generate_btn, alignment=Qt.AlignCenter)
#################################################

def winner_btn_clicked():
    number = random.randint(1, 100)
    winner_lbl.setText(str(number))
    text.setText("Winner:")

generate_btn.clicked.connect(winner_btn_clicked)

my_win.setLayout(layout_v)
my_win.show()
app.exec_()