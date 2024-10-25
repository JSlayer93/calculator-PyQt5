import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLayout, QTextEdit, QGridLayout, QPushButton, QLineEdit, QLabel, QVBoxLayout, QStackedWidget
from PyQt5.QtCore import Qt
from decimal import Decimal
import os
# importing json to write and read data
import json

def resource_path(relative_path):
    """ Get the absolute path to the resource, accounting for PyInstaller packaging """
    if getattr(sys, 'frozen', False):
        # If the application is packaged
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Use resource_path to get the path to data.json
data_file_path = resource_path('data.json')

f = open(data_file_path, 'r+')
data = json.load(f)

def add_new_history(equation, result):
    # Append the new equation and result to the history list
    update = data["history"].append({"equation": equation, "result": result})
    f.seek(0)
    json.dump(data, f, indent=4)

# initializing Main window class to show window
class Main_window(QMainWindow):
    def __init__(self):
        super().__init__()
        # setting up title for window
        self.setWindowTitle("Main window")
        self.setGeometry(450, 400, 600, 700)
        # creataing memory
        self.result = 0
        # creating number to show
        self.number = ''
        # creating text which lineEdit will show
        self.text = ''
        
        # creating buttons
        self.button_negative = QPushButton('-/+')
        self.button0 = QPushButton('0')
        self.button_point = QPushButton('.')
        self.button_equal = QPushButton('=')
        self.button1 = QPushButton('1')
        self.button2 = QPushButton('2')
        self.button3 = QPushButton('3')
        self.button_plus = QPushButton('+')
        self.button4 = QPushButton('4')
        self.button5 = QPushButton('5')
        self.button6 = QPushButton('6')
        self.button_minus = QPushButton('-')
        self.button7 = QPushButton('7')
        self.button8 = QPushButton('8')
        self.button9 = QPushButton('9')
        self.button_multiply = QPushButton('*')
        self.button_divsion = QPushButton('/')
        self.button_data = QPushButton('data')
        self.button_clear = QPushButton('C')
        self.button_remove = QPushButton('<')
        # creating line edit (text)
        self.text_screen = QLineEdit()
        # to center window
        self.move(QApplication.desktop().screen().rect().center() - self.rect().center())
        # calling initUI funtion to make UI
        self.initUi()
    
    # defining function to make UI
    def initUi(self):
        # creating central widget to make layout on windows
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        # Example of setting up a QGridLayout with number buttons arranged in columns
        grid = QGridLayout()

        # Set the desired width and height for all buttons
        button_width = 150  # Adjust this value as needed
        button_height = 116  # Adjust this value as needed

        # Set width and height for individual buttons and add them to the grid
        self.button7.setFixedWidth(button_width)
        self.button7.setFixedHeight(button_height)
        grid.addWidget(self.button7, 2, 0)
        self.button8.setFixedWidth(button_width)
        self.button8.setFixedHeight(button_height)
        grid.addWidget(self.button8, 2, 1)
        self.button9.setFixedWidth(button_width)
        self.button9.setFixedHeight(button_height)
        grid.addWidget(self.button9, 2, 2)
        self.button_multiply.setFixedWidth(button_width)
        self.button_multiply.setFixedHeight(button_height)
        grid.addWidget(self.button_multiply, 2, 3)
        self.button4.setFixedWidth(button_width)
        self.button4.setFixedHeight(button_height)
        grid.addWidget(self.button4, 3, 0)
        self.button5.setFixedWidth(button_width)
        self.button5.setFixedHeight(button_height)
        grid.addWidget(self.button5, 3, 1)
        self.button6.setFixedWidth(button_width)
        self.button6.setFixedHeight(button_height)
        grid.addWidget(self.button6, 3, 2)
        self.button_minus.setFixedWidth(button_width)
        self.button_minus.setFixedHeight(button_height)
        grid.addWidget(self.button_minus, 3, 3)
        self.button1.setFixedWidth(button_width)
        self.button1.setFixedHeight(button_height)
        grid.addWidget(self.button1, 4, 0)
        self.button2.setFixedWidth(button_width)
        self.button2.setFixedHeight(button_height)
        grid.addWidget(self.button2, 4, 1)
        self.button3.setFixedWidth(button_width)
        self.button3.setFixedHeight(button_height)
        grid.addWidget(self.button3, 4, 2)
        self.button_plus.setFixedWidth(button_width)
        self.button_plus.setFixedHeight(button_height)
        grid.addWidget(self.button_plus, 4, 3)
        self.button0.setFixedWidth(button_width)
        self.button0.setFixedHeight(button_height)
        grid.addWidget(self.button0, 5, 1)
        self.button_point.setFixedWidth(button_width)
        self.button_point.setFixedHeight(button_height)
        grid.addWidget(self.button_point, 5, 2)
        self.button_negative.setFixedWidth(button_width)
        self.button_negative.setFixedHeight(button_height)
        grid.addWidget(self.button_negative, 5, 0)
        self.button_equal.setFixedWidth(button_width)
        self.button_equal.setFixedHeight(button_height)
        grid.addWidget(self.button_equal, 5, 3)
        self.button_divsion.setFixedWidth(button_width)
        self.button_divsion.setFixedHeight(button_height)
        grid.addWidget(self.button_divsion, 1, 2)
        self.button_data.setFixedWidth(button_width)
        self.button_data.setFixedHeight(button_height)
        grid.addWidget(self.button_data, 1, 3)
        self.button_clear.setFixedWidth(button_width)
        self.button_clear.setFixedHeight(button_height)
        grid.addWidget(self.button_clear, 1, 1)
        self.button_remove.setFixedWidth(button_width)
        self.button_remove.setFixedHeight(button_height)
        grid.addWidget(self.button_remove, 1, 0)
        self.text_screen.setFixedHeight(button_height)
        grid.addWidget(self.text_screen, 0, 0, 1, 4)  # Span across 4 columns
        self.text_screen.setReadOnly(True)

        # this code says method on_click will run every time i click some button
        self.button7.clicked.connect(self.on_click)
        self.button8.clicked.connect(self.on_click)
        self.button9.clicked.connect(self.on_click)
        self.button_multiply.clicked.connect(self.on_click)
        self.button4.clicked.connect(self.on_click)
        self.button5.clicked.connect(self.on_click)
        self.button6.clicked.connect(self.on_click)
        self.button_minus.clicked.connect(self.on_click)
        self.button1.clicked.connect(self.on_click)
        self.button2.clicked.connect(self.on_click)
        self.button3.clicked.connect(self.on_click)
        self.button_plus.clicked.connect(self.on_click)
        self.button0.clicked.connect(self.on_click)
        self.button_point.clicked.connect(self.on_click)
        self.button_negative.clicked.connect(self.on_click)
        self.button_equal.clicked.connect(self.on_click)
        self.button_divsion.clicked.connect(self.on_click)
        self.button_data.clicked.connect(self.on_click)
        self.button_clear.clicked.connect(self.on_click)
        self.button_remove.clicked.connect(self.on_click)

        # setting up object names to style elements
        self.text_screen.setObjectName("text_screen")
        # creating css for entire page
        self.setStyleSheet("""
                           QPushButton{
                               font-size: 40px
                           }
                           QLineEdit#text_screen{
                               font-size: 40px
                           }
                           QLineEdit::placeholder {
                                color: gray;             /* Placeholder text color */
                                font-size: 10pt;         /* Placeholder font size (smaller) */
                                vertical-align: top;     /* Aligns the placeholder text at the top */
                            }
                           
        """)
        
        # applying grid to central widget to aplly it to window
        central_widget.setLayout(grid)
        
    def on_click(self):
        button = self.sender()

        try:
            int(button.text())
            if self.number == '' and button.text() == '0':
                pass
            else:
                self.number = self.number + str(button.text())
                self.text = self.text + str(button.text())         
        except:
            if button.text() == "C":
                self.result = 0
                self.number = ''
                self.text = ''
            elif button.text() == 'data':
                self.show_new_screen()
            elif button.text() == '<':
                self.number = self.number[:-1]
                self.text = self.text[:-1]
            elif button.text() == '.' and len(self.number) >= 1:
                self.number = self.number + '.'
                self.text = self.text + '.'
            elif button.text() == '-/+' and self.text != '' and len(self.text) == len(self.number):
                self.number = str(Decimal(self.number) * -1)
                self.text = str(Decimal(self.text) * -1)
            elif button.text() == "=" and self.text != '' and self.text[0] != '0':
                if self.number != '':
                    add_new_history(self.text, str(eval(self.text)))
                    self.text= str(eval(self.text))
                    self.number = self.text
                else:
                    add_new_history(self.text[:-1], str(eval(self.text[:-1])))
                    self.text = str(eval(self.text[:-1]))
                    self.number = self.text
            elif self.number != '' and button.text() != '-/+' and button.text() != '=':
                self.number = ''
                self.text = self.text + button.text()
            
        self.text_screen.setText(self.text)
        
    def show_new_screen(self):
        # Switch to the next screen
        stacked_widget.setCurrentIndex(stacked_widget.currentIndex() + 1)
    
    
class Data_Screen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('data')
        self.button_history = QPushButton("History")
        self.button_back = QPushButton('back')
        self.initUi()
        
    def initUi(self):
        # creating central widget to make layout on windows
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        # Example of setting up a QGridLayout with number buttons arranged in columns
        horizontal_layout = QVBoxLayout()
        # setting up button height and width
        button_width = 600
        button_height = 116
        # adding button to horizontal layout
        horizontal_layout.addWidget(self.button_history)
        horizontal_layout.addWidget(self.button_back)
        self.button_history.setFixedHeight(button_height)
        self.button_back.setFixedHeight(button_height)
        
        # setting up css code to style buttons
        self.setStyleSheet("""
                           QPushButton{
                               font-size: 40px
                           }
                           
        """)
        
        self.button_back.clicked.connect(self.click_back)
        self.button_history.clicked.connect(self.click_history)
        
        central_widget.setLayout(horizontal_layout)
        
    def click_back(self):
        # Switch to the next screen
        stacked_widget.setCurrentIndex(stacked_widget.currentIndex() - 1)
        
    def click_history(self):
        # Switch to the next screen
        stacked_widget.setCurrentIndex(stacked_widget.currentIndex() + 1)
        
        
class History_Screen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.text = QLineEdit(self)
        self.button_back = QPushButton('back', self)
    
        self.initUi()
    
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton, QVBoxLayout, QWidget

class History_Screen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.text = QTextEdit(self)
        self.button_back = QPushButton('back', self)

        self.initUi()

    def initUi(self):
        # initializing layout
        central_widget = QWidget()
        vertical_layout = QVBoxLayout(central_widget)

        # add widgets to layout
        vertical_layout.addWidget(self.text)
        vertical_layout.addWidget(self.button_back)

        # initializing button size
        button_width = 600
        button_height = 116

        self.text.setFixedHeight(700 - button_height)
        self.button_back.setFixedHeight(button_height)
        
        # setting up css code to style buttons
        self.setStyleSheet("""
                            QPushButton{
                                font-size: 40px
                            }
                            QTextEdit{
                                font-size: 30px
                            }
        """)
        
        self.button_back.clicked.connect(self.click_back)
        
        self.text.setReadOnly(True)
        self.setCentralWidget(central_widget)
        
        # Connect the currentChanged signal of the stacked_widget to a function
        stacked_widget.currentChanged.connect(self.on_screen_change)
        
    def on_screen_change(self, index):
        # Check if the current screen is the History_Screen
        if index == stacked_widget.indexOf(self):
            # Call your function here
            self.write_history()
        
    def write_history(self):
        for e in data['history']:
            self.text.setText(f"{self.text.toPlainText()}\n{e['equation']} = {e['result']}")
            
    def click_back(self):
        # Switch to the next screen
        stacked_widget.setCurrentIndex(stacked_widget.currentIndex() - 1)
            
        
# defining main function to show applicatoin
def main():
    global stacked_widget
    app = QApplication(sys.argv)
    # create socked widget
    stacked_widget = QStackedWidget()
    window = Main_window()
    data_screen = Data_Screen()
    history_screen = History_Screen()
    # Add the screens to the stacked widget
    stacked_widget.addWidget(window)
    stacked_widget.addWidget(data_screen)
    stacked_widget.addWidget(history_screen)
    # make window stay and now close
    stacked_widget.show()
    # close window only when i close application
    sys.exit((app.exec_(), f.close))
    
# only calling main function if we are running the code (not when we module, or import it)
if __name__ == "__main__":
    main()