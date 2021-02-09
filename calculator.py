import PyQt5.QtWidgets as qtw

class MainWindow(qtw.QWidget):

	def __init__(self):
		super().__init__()

		self.setWindowTitle("my pyQt app")

		self.setLayout(qtw.QVBoxLayout())

		self.setUI()

		self.show()

	def setUI(self):
		container = qtw.QWidget()
		container.setLayout(qtw.QGridLayout())

		# create the buttons
		btn_1 = qtw.QPushButton('1', self)
		btn_2 = qtw.QPushButton('2', self)
		btn_3 = qtw.QPushButton('3', self)
		btn_4 = qtw.QPushButton('4', self)
		btn_5 = qtw.QPushButton('5', self)
		btn_6 = qtw.QPushButton('6', self)
		btn_7 = qtw.QPushButton('7', self)
		btn_8 = qtw.QPushButton('8', self)
		btn_9 = qtw.QPushButton('9', self)
		btn_0 = qtw.QPushButton('0', self)

		btn_1.clicked.connect(self.clickBtn1)
		btn_2.clicked.connect(self.clickBtn2)
		btn_3.clicked.connect(self.clickBtn3)
		btn_4.clicked.connect(self.clickBtn4)
		btn_5.clicked.connect(self.clickBtn5)
		btn_6.clicked.connect(self.clickBtn6)
		btn_7.clicked.connect(self.clickBtn7)
		btn_8.clicked.connect(self.clickBtn8)
		btn_9.clicked.connect(self.clickBtn9)
		btn_0.clicked.connect(self.clickBtn0)

		btn_plus = qtw.QPushButton('+', self)
		btn_minus = qtw.QPushButton('-', self)
		btn_times = qtw.QPushButton('x', self)
		btn_divid = qtw.QPushButton('/', self)
		
		btn_plus.clicked.connect(self.clickBtnPlus)
		btn_minus.clicked.connect(self.clickBtnMinus)
		btn_times.clicked.connect(self.clickBtnTimes)
		btn_divid.clicked.connect(self.clickBtnDivid)

		btn_enter = qtw.QPushButton('Enter')
		btn_clear = qtw.QPushButton('Clear')

		btn_enter.clicked.connect(self.clickBtnEnter)
		btn_clear.clicked.connect(self.clickBtnClear)

		self.lineEdit = qtw.QLineEdit()

		# add buttons to layout
		container.layout().addWidget(self.lineEdit,0,0,1,12)

		container.layout().addWidget(btn_enter,1,0,1,6)
		container.layout().addWidget(btn_clear,1,6,1,6)

		container.layout().addWidget(btn_7,2,0,1,3)
		container.layout().addWidget(btn_8,2,3,1,3)
		container.layout().addWidget(btn_9,2,6,1,3)

		container.layout().addWidget(btn_4,3,0,1,3)
		container.layout().addWidget(btn_5,3,3,1,3)
		container.layout().addWidget(btn_6,3,6,1,3)

		container.layout().addWidget(btn_1,4,0,1,3)
		container.layout().addWidget(btn_2,4,3,1,3)
		container.layout().addWidget(btn_3,4,6,1,3)

		container.layout().addWidget(btn_0,5,0,1,9)

		container.layout().addWidget(btn_plus,2,9,1,3)
		container.layout().addWidget(btn_minus,3,9,1,3)
		container.layout().addWidget(btn_times,4,9,1,3)
		container.layout().addWidget(btn_divid,5,9,1,3)

		self.layout().addWidget(container)
	
	def clickBtn1(self):
		calcul = self.lineEdit.text()
		self.lineEdit.setText(calcul + '1')

	def clickBtn2(self):
		calcul = self.lineEdit.text()
		self.lineEdit.setText(calcul + '2')

	def clickBtn3(self):
		calcul = self.lineEdit.text()
		self.lineEdit.setText(calcul + '3')

	def clickBtn4(self):
		calcul = self.lineEdit.text()
		self.lineEdit.setText(calcul + '4')

	def clickBtn5(self):
		calcul = self.lineEdit.text()
		self.lineEdit.setText(calcul + '5')

	def clickBtn6(self):
		calcul = self.lineEdit.text()
		self.lineEdit.setText(calcul + '6')

	def clickBtn7(self):
		calcul = self.lineEdit.text()
		self.lineEdit.setText(calcul + '7')

	def clickBtn8(self):
		calcul = self.lineEdit.text()
		self.lineEdit.setText(calcul + '8')

	def clickBtn9(self):
		calcul = self.lineEdit.text()
		self.lineEdit.setText(calcul + '9')

	def clickBtn0(self):
		calcul = self.lineEdit.text()
		self.lineEdit.setText(calcul + '0')
	
	def clickBtnPlus(self):
		calcul = self.lineEdit.text()
		self.lineEdit.setText(calcul + " + ")

	def clickBtnMinus(self):
		calcul = self.lineEdit.text()
		self.lineEdit.setText(calcul + " - ")
	
	def clickBtnTimes(self):
		calcul = self.lineEdit.text()
		self.lineEdit.setText(calcul + " * ")

	def clickBtnDivid(self):
		calcul = self.lineEdit.text()
		self.lineEdit.setText(calcul + " / ")

	def clickBtnEnter(self):
		calcul = self.lineEdit.text()

		try:
			result = eval(calcul)
		except:
			self.lineEdit.setText("Error in the operation")
		else:
			self.lineEdit.setText(str(result))

	def clickBtnClear(self):
		self.lineEdit.setText('')

app = qtw.QApplication([])
mw = MainWindow()
app.exec_()
