from typing import Self
from PyQt6 import QtCore
from PyQt6.QtWidgets import *
from PyQt6.QtWidgets import QWidget
from my_interface import *
import sys
from PyQt6 import *

import random 

class Window(Ui_MainWindow,QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.lineEdit.text()
        self.pushButton.clicked.connect(self.det_answer)
        self.answer.setText('')
        self.my_lst =  ['бесспорно','предрешено','пока не ясно попробуя снова','даже не думай','мне кажется да','вероятнее всего','спроси позже','мой ответ - нет','никаких сомнений','хорошие перспективы','лучше не рассказывать',' по моим данным нет','определенно да','знаки говорят да','сейчас нельзя предсказать','перспективы не очень хорошие','можешь быть уверен в этом','да','сконцентрируйся и попроси опять','весьма сомнительно']
     
    


    def det_answer(self):
        self.text = self.lineEdit.text()
        if self.text.strip():
    
            self.answer.setText(random.choice(self.my_lst))
        else:
            self.answer.setText('Чтобы я мог ответить задай мне вопрос') 
        


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec())