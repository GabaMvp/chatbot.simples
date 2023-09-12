import nltk
from nltk.chat.util import Chat, reflections
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QPushButton, QLabel, QLineEdit
from PyQt5.QtGui import QTextCursor 

# Pares de padrão e respostas para o chatbot
pares = [
    ["Oi|Olá|Hey", ["Oi!", "Olá!", "Hey!"]],
    ["Como você está?", ["Eu estou bem, obrigado por perguntar.", "Eu estou ótimo, e você?"]],
    ["Eu estou bem!|Estou bem!", ["isso é ótimo!"]],
    ["Qual é o seu nome?", ["Me chamam de gabaJr.", "Pode me chamar de chatbot."]],
    ["Qual é o sentido da vida?", ["Eu também gostaria de saber"]],
    ["Tchau|Até logo", ["Até mais!", "Tchau!"]]
]

# Criando o objeto Chat com os pares de padrão e resposta
chatbot = Chat(pares, reflections)

class ChatbotApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Chatbot')
        self.setGeometry(100, 100, 800, 600)

        self.layout = QVBoxLayout()

        self.chat_history = QTextEdit(self)
        self.chat_history.setReadOnly(True)
        self.layout.addWidget(self.chat_history)

        self.user_input = QLineEdit(self)
        self.layout.addWidget(self.user_input)

        self.send_button = QPushButton('Enviar', self)
        self.send_button.clicked.connect(self.send_message)
        self.layout.addWidget(self.send_button)

        self.setLayout(self.layout)

    def send_message(self):
        user_text = self.user_input.text()
        self.user_input.clear()

        response = chatbot.respond(user_text)
        self.display_message(f"Você: {user_text}\nChatbot: {response}\n")

    def display_message(self, message):
        self.chat_history.insertPlainText(message)
        self.chat_history.moveCursor(QTextCursor.End)  # Corrigindo a linha aqui

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ChatbotApp()
    ex.show()
    sys.exit(app.exec_())
