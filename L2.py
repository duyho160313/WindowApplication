from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle("Quoc Duy")
main_win.resize(400,200)

# Widgets #
text = QLabel("What year did the channel receive the 'gold play button' from Youtube? ")
answer1 = QRadioButton("2005")
answer2 = QRadioButton("2010")
answer3 = QRadioButton("2015")
answer4 = QRadioButton("They don't receive the 'gold play button'")
#######

# Layout #
main_layout = QVBoxLayout()
main_layout.addWidget(text, alignment=Qt.AlignCenter)
layout_h1 = QHBoxLayout()
layout_h2 = QHBoxLayout()
layout_h2.addWidget(answer3, alignment=Qt.AlignCenter)
layout_h2.addWidget(answer4, alignment=Qt.AlignCenter)
layout_h1.addWidget(answer1, alignment=Qt.AlignCenter)
layout_h1.addWidget(answer2, alignment=Qt.AlignCenter)
main_layout.addLayout(layout_h1)
main_layout.addLayout(layout_h2)
##########
def show_win():
    message = QMessageBox()
    message.setText("Congrats! You correct.")
    message.exec_()
def show_lose():
    correct_ans = QMessageBox()
    correct_ans.setText("You wrong the correct answer is 'They don't receive the 'gold play button'")
    correct_ans.exec_()
answer1.clicked.connect(show_lose)
answer2.clicked.connect(show_lose)
answer3.clicked.connect(show_lose)
answer4.clicked.connect(show_win)
main_win.setLayout(main_layout)
main_win.show()
app.exec_()


