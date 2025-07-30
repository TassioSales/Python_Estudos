import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.config import Config

# Define a cor de fundo da janela (cinza escuro)
Config.set('graphics', 'clearcolor', (0.15, 0.15, 0.15, 1))


class CalculadoraApp(App):
    def build(self):
        # Layout principal que organiza os widgets verticalmente
        self.layout_principal = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Visor da calculadora
        self.visor = Label(
            text='0',
            font_size=60,
            halign='right',
            valign='middle',
            size_hint=(1, 0.3),
            text_size=(None, None)
        )
        self.visor.bind(size=self.visor.setter('text_size'))
        self.layout_principal.add_widget(self.visor)

        # Layout para os botões em grade
        botoes_layout = GridLayout(cols=4, spacing=10)

        # Lista de botões a serem criados
        self.botoes = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '.', '+'
        ]

        # Botão de igualdade separado para estilização diferente
        self.botoes_especiais = {
            '=': (0.2, 0.6, 1, 1),  # Cor azul
            'C': (1, 0.3, 0.3, 1),  # Cor vermelha
            '/': (0.8, 0.8, 0.8, 1),  # Cor cinza claro
            '*': (0.8, 0.8, 0.8, 1),
            '-': (0.8, 0.8, 0.8, 1),
            '+': (0.8, 0.8, 0.8, 1),
        }

        # Cria e adiciona os botões ao layout de grade
        for simbolo in self.botoes:
            cor_fundo = self.botoes_especiais.get(simbolo, (0.3, 0.3, 0.3, 1))  # Cinza padrão
            botao = Button(
                text=simbolo,
                font_size=32,
                background_color=cor_fundo,
                background_normal=''  # Necessário para a cor de fundo funcionar
            )
            botao.bind(on_press=self.ao_pressionar_botao)
            botoes_layout.add_widget(botao)

        self.layout_principal.add_widget(botoes_layout)

        # Botão de igualdade ocupando a largura total
        botao_igual = Button(
            text='=',
            font_size=40,
            size_hint=(1, 0.15),
            background_color=self.botoes_especiais.get('='),
            background_normal=''
        )
        botao_igual.bind(on_press=self.calcular_resultado)
        self.layout_principal.add_widget(botao_igual)

        return self.layout_principal

    def ao_pressionar_botao(self, instance):
        texto_atual = self.visor.text
        simbolo_pressionado = instance.text

        if simbolo_pressionado == 'C':
            # Limpa o visor
            self.visor.text = '0'
        else:
            if texto_atual == '0' or texto_atual == 'Erro':
                self.visor.text = simbolo_pressionado
            else:
                self.visor.text += simbolo_pressionado

    def calcular_resultado(self, instance):
        expressao = self.visor.text
        try:
            # A função eval() avalia a expressão matemática de forma segura
            # Cuidado: eval pode ser inseguro com entradas não controladas.
            # Para esta calculadora, onde o input é controlado, é aceitável.
            resultado = str(eval(expressao))
            self.visor.text = resultado
        except Exception:
            self.visor.text = 'Erro'


# Ponto de entrada da aplicação
if __name__ == '__main__':
    CalculadoraApp().run()