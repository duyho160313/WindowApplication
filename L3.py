from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from random import shuffle
app = QApplication([])
###Object: Question
class Question():
    def __init__(self, question, right_ans, wrong_ans1, wrong_ans2, wrong_ans3):
        self.question = question
        self.right_ans = right_ans
        self.wrong_ans1 = wrong_ans1
        self.wrong_ans2 = wrong_ans2
        self.wrong_ans3 = wrong_ans3





# Widgets ##
#question screen
question = QLabel("Question")
answer_btn = QPushButton("Answer")
answer1 = QRadioButton("Answer1")
answer2 = QRadioButton("Answer2")
answer3 = QRadioButton("Answer3")
answer4 = QRadioButton("Answer4")
radio_group = QGroupBox("Answer options")
radio_btn_group = QButtonGroup()
radio_btn_group.addButton(answer1)
radio_btn_group.addButton(answer2)
radio_btn_group.addButton(answer3)
radio_btn_group.addButton(answer4)


#resutlts screen
message_lbl = QLabel("Correct")
correct_ans_lbl = QLabel("Correct answer!")
result_group = QGroupBox("Test result")
###################

# Layout ################################
main_layout = QVBoxLayout()
layout_h1 = QHBoxLayout()
layout_h2 = QHBoxLayout()

#Answer screen layout
layout_h1.addWidget(answer1)
layout_h1.addWidget(answer3)

layout_h2.addWidget(answer2)
layout_h2.addWidget(answer4)

layout_v1 = QVBoxLayout()
layout_v1.addLayout(layout_h1)
layout_v1.addLayout(layout_h2)
radio_group.setLayout(layout_v1)

#Result screen layout

layout_v2 = QVBoxLayout()
layout_v2.addWidget(message_lbl, alignment= (Qt.AlignLeft | Qt.AlignTop))
layout_v2.addWidget(correct_ans_lbl, alignment = Qt.AlignHCenter, stretch = 2)
result_group.setLayout(layout_v2)
result_group.hide()
###########
###########################################
# Add all Widgets into main layout
main_layout.addWidget(question, alignment=Qt.AlignHCenter | Qt.AlignVCenter)#question
main_layout.addWidget(radio_group)#answer group
main_layout.addWidget(result_group)#result group
main_layout.addWidget(answer_btn, alignment=Qt.AlignHCenter)#answer button
##############################
#list answers
answers = []
answers.append(answer1)
answers.append(answer2)
answers.append(answer3)
answers.append(answer4)
#FUNCTION
#1
def button_answer_clicked():
    if answer_btn.text() == "Answer":
        check_answer()#2
    else:
        shuffle(question_list)
        next_question()
#2
def check_answer():
    if answers[1].isChecked():
        main_win.score +=1
        show_correct("Correct!!")
    else:
        if answers[0].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct("Incorrect!!")
#3
def next_question():
    main_win.total += 1
    #STAtisticS
    print("Total question:", main_win.total)
    print("Right answers:", main_win.score)
    rate = (main_win.score / main_win.total) * 100
    print("Rating:",round(rate,2) , '%')
    main_win.cur_question += 1
    if main_win.cur_question >= len(question_list):
        main_win.cur_question = 0
    q = question_list[main_win.cur_question]
    ask(q)
#4
def show_correct(text):
    message_lbl.setText(text)
    show_result()
#5
def show_result():
    result_group.show()
    radio_group.hide()
    answer_btn.setText("Next question")
#6
def ask(q: Question):
    shuffle(answers)
    answers[1].setText(q.right_ans)
    answers[0].setText(q.wrong_ans1)
    answers[2].setText(q.wrong_ans2)
    answers[3].setText(q.wrong_ans3)
    question.setText(q.question)
    correct_ans_lbl.setText(q.right_ans)
    show_question()
#7
def show_question():
    result_group.hide()
    radio_group.show()
    radio_btn_group.setExclusive(False)
    answer1.setChecked(False)
    answer2.setChecked(False)
    answer3.setChecked(False)
    answer4.setChecked(False)
    radio_btn_group.setExclusive(True)
    answer_btn.setText("Answer")







answer_btn.clicked.connect(button_answer_clicked)
question_list = []
q1 = Question("What is your name?", "Duy", "Kane", 'ken', 'bill')
q2 = Question("Where do you born?", "Vietnam", "Singapore", "Malaysia", "Indonesia")
q3 = Question("What sport do you like?", "basketball", "football", "Tennis", "badminton")
q4 = Question("What do you do in breaktime", "play football", "play basketball", "play badminton", "play tennis")
q5 = Question('What is your  favorite subject', "Mandarin", "science", "Music", "English")
q6 = Question("What do you do on last holiday?", "Went to Australia", "Went to Hà Nội", "Went to Brazil", "Sleep at home")
q7 = Question('What is a group of cats called?', "A clowder", "Sea otter", "Nose", "Bats")
q8 = Question("Which has the thickest fur of any mammal?", "Sea otter", "Bumblebee bat", 'Giraffe', "Crocodile")
q9 = Question('What mammal has the most powerful bite?', "Hippopotamus", "Giraffe", "Bumblebee bat", "Sea otter")
q10 = Question("How far away can a wolf smell its prey?", "Almost two miles", "Almost one miles", "Almost three miles", "Almost ten miles")
question_list.append(q1)
question_list.append(q2)
question_list.append(q3)
question_list.append(q4)
question_list.append(q5)
question_list.append(q6)
question_list.append(q7)
question_list.append(q8)
question_list.append(q9)
question_list.append(q10)
ask(question_list[0])
##################
main_win = QWidget()
main_win.cur_question = -1
main_win.score = 0
main_win.total = 0
main_win.setLayout(main_layout)
main_win.show()
app.exec_()