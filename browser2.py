import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QHBoxLayout,QVBoxLayout, QWidget, QPushButton
from PyQt5.QtWebEngineWidgets import QWebEngineView


class Browser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Web Browser")

        self.search_bar = QLineEdit()
        self.search_bar.returnPressed.connect(self.search)
        
        self.search_button = QPushButton("Search")
        self.search_button.clicked.connect(self.search)
        
        self.web_view = QWebEngineView()
        self.web_view.load(QUrl("https://www.google.com"))

        self.back_button = QPushButton("<")
        self.back_button.setFixedSize(20, 20)
        self.back_button.clicked.connect(self.web_view.back)

        self.forward_button = QPushButton(">")
        self.forward_button.setFixedSize(20, 20)
        self.forward_button.clicked.connect(self.web_view.forward)

        
        layout = QVBoxLayout()
        search_layout = QHBoxLayout()
        button_layout = QHBoxLayout()
        search_layout.addWidget(self.search_bar)
        search_layout.addWidget(self.search_button)
        button_layout.addWidget(self.back_button)
        button_layout.addWidget(self.forward_button)
        layout.addLayout(button_layout)
        layout.addLayout(search_layout)
        layout.addWidget(self.web_view)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def search(self):
        query = self.search_bar.text()
        url = "https://www.google.com/search?q=" + query
        self.web_view.load(QUrl(url))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    browser = Browser()
    browser.show()
    sys.exit(app.exec_())
