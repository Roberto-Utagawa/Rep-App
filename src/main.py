from kivy.lang import Builder # O Builder conecta o banckend com o frontend #
from kivy.app import App

GUI = Builder.load_file("gui.kv") # Carrega o frontend #

class rep_app(App):

    def build(self):
        return GUI

rep_app().run()