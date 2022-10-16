from PyQt6 import QtWidgets, uic
from analyser import Analyser

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi('test.ui', self)
        self.show()
        self.select_soure_file_button.clicked.connect(self.select_file)
        self.analyser = Analyser()
        self.make_word_cloud.clicked.connect(self.run)
    def select_file(self):
        self.file_path = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "",
            "",
            "texts (*.txt *.docx *.fb2)"
        )[0]
        self.source_file_path_line.setText(self.file_path)
    def run(self):
        self.analyser.make_text_from_file()
        self.analyser.make_words_from_text()
        self.analyser.make_normalized_words("NOUN")
        self.analyser.make_most_frequent_words(100)
        self.analyser.make_wordcloud()
        self.analyser.save_wordcloud_to_file("wordcloud.png")




        """print(self.Adjf.isChecked())
        print(self.words_number.value())"""

app = QtWidgets.QApplication([])
window = Window()
app.exec()