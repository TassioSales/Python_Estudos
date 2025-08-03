from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, RoundedRectangle, Line
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.properties import StringProperty, BooleanProperty
from database import DataBase
import re

# Set window size for better desktop experience
Window.size = (400, 700)
Window.minimum_width, Window.minimum_height = 300, 500

# Color scheme
COLORS = {
    'primary': '#6200EE',  # Purple
    'primary_dark': '#3700B3',
    'secondary': '#03DAC6',  # Teal
    'background': '#F5F5F5',
    'error': '#B00020',
    'on_primary': '#FFFFFF',
    'on_secondary': '#000000',
    'on_background': '#000000',
    'on_surface': '#000000',
    'surface': '#FFFFFF'
}

class RoundedButton(Button):
    """Custom button with rounded corners and elevation effect"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = ''
        self.background_color = get_color_from_hex(COLORS['primary'])
        self.color = get_color_from_hex(COLORS['on_primary'])
        self.font_size = '16sp'
        self.size_hint_y = None
        self.height = dp(50)
        self.padding = (dp(10), dp(5))
        self.background_down = ''
        
        # Add elevation effect
        self.elevation = 2
        self.bind(state=self._on_state)
    
    def _on_state(self, instance, value):
        if value == 'down':
            self.background_color = get_color_from_hex(COLORS['primary_dark'])
            self.elevation = 8
        else:
            self.background_color = get_color_from_hex(COLORS['primary'])
            self.elevation = 2

class InputField(TextInput):
    """Custom text input with better styling"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = ''
        self.background_active = ''
        self.background_color = (1, 1, 1, 1)
        self.foreground_color = (0, 0, 0, 1)
        self.multiline = False
        self.padding = [dp(15), dp(15)]
        self.size_hint_y = None
        self.height = dp(50)
        self.font_size = '16sp'
        self.background_color = get_color_from_hex('#FFFFFF')
        self.write_tab = False
        
        # Initialize line_color
        self.line_color = get_color_from_hex('#CCCCCC')
        
    def on_focus(self, instance, value):
        if value:
            # Animation for focus
            self.line_color = get_color_from_hex(COLORS['primary'])
        else:
            self.line_color = get_color_from_hex('#CCCCCC')

class LoginScreen(Screen):
    error_message = StringProperty('')
    is_loading = BooleanProperty(False)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.db = DataBase('users.txt')
        self.build_ui()
    
    def build_ui(self):
        # Main container
        main_layout = BoxLayout(orientation='vertical', padding=dp(30), spacing=dp(20))
        
        # Header
        header = Label(
            text='Bem-vindo', 
            font_size='32sp',
            bold=True,
            size_hint_y=None,
            height=dp(100),
            color=get_color_from_hex(COLORS['on_surface'])
        )
        
        # Error label
        self.error_label = Label(
            text=self.error_message,
            color=get_color_from_hex(COLORS['error']),
            size_hint_y=None,
            height=dp(30),
            halign='center',
            text_size=(Window.width - dp(60), None)
        )
        
        # Form fields
        form_layout = BoxLayout(orientation='vertical', spacing=dp(15))
        
        # Email field
        email_layout = BoxLayout(orientation='vertical', spacing=dp(5))
        email_layout.add_widget(Label(
            text='Email',
            color=get_color_from_hex(COLORS['on_surface']),
            size_hint_y=None,
            height=dp(20)
        ))
        self.email = InputField(hint_text='seu@email.com')
        email_layout.add_widget(self.email)
        
        # Password field
        password_layout = BoxLayout(orientation='vertical', spacing=dp(5))
        password_layout.add_widget(Label(
            text='Senha',
            color=get_color_from_hex(COLORS['on_surface']),
            size_hint_y=None,
            height=dp(20)
        ))
        self.password = InputField(hint_text='••••••••', password=True)
        password_layout.add_widget(self.password)
        
        # Add fields to form
        form_layout.add_widget(email_layout)
        form_layout.add_widget(password_layout)
        
        # Login button
        login_btn = RoundedButton(text='ENTRAR')
        login_btn.bind(on_press=self.login)
        
        # Register link
        register_layout = BoxLayout(size_hint_y=None, height=dp(50))
        register_label = Label(
            text='Não tem uma conta?',
            color=get_color_from_hex(COLORS['on_surface'])
        )
        register_btn = Button(
            text='Cadastre-se',
            background_color=(0, 0, 0, 0),
            color=get_color_from_hex(COLORS['primary']),
            bold=True,
            size_hint_x=None,
            width=dp(100)
        )
        register_btn.bind(on_press=self.go_to_register)
        
        register_layout.add_widget(register_label)
        register_layout.add_widget(register_btn)
        
        # Add all widgets to main layout
        main_layout.add_widget(header)
        main_layout.add_widget(self.error_label)
        main_layout.add_widget(form_layout)
        main_layout.add_widget(login_btn)
        main_layout.add_widget(register_layout)
        
        # Add a spacer to push content up
        main_layout.add_widget(BoxLayout(size_hint_y=1))
        
        # Add main layout to screen
        self.add_widget(main_layout)
    
    def validate_form(self):
        email = self.email.text.strip()
        password = self.password.text.strip()
        
        if not email or not password:
            self.show_error('Por favor, preencha todos os campos')
            return False
            
        if not re.match(r'^[^@]+@[^@]+\.[^@]+$', email):
            self.show_error('Por favor, insira um email válido')
            return False
            
        return True
    
    def show_error(self, message):
        self.error_message = message
        self.error_label.text = message
        anim = Animation(opacity=1, duration=0.3) + Animation(opacity=1, duration=2) + Animation(opacity=0, duration=0.3)
        anim.start(self.error_label)
    
    def login(self, instance):
        if not self.validate_form():
            return
            
        self.is_loading = True
        
        # Simulate network delay
        def do_login(dt):
            if self.db.validate(self.email.text, self.password.text):
                self.parent.current = 'welcome'
            else:
                self.show_error('Email ou senha incorretos')
            self.is_loading = False
            
        Clock.schedule_once(do_login, 0.5)
    
    def go_to_register(self, instance):
        self.parent.transition.direction = 'left'
        self.parent.current = 'register'

class RegisterScreen(Screen):
    error_message = StringProperty('')
    is_loading = BooleanProperty(False)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.db = DataBase('users.txt')
        self.build_ui()
    
    def build_ui(self):
        # Main container
        main_layout = BoxLayout(orientation='vertical', padding=dp(30), spacing=dp(20))
        
        # Header
        header = Label(
            text='Criar Conta', 
            font_size='32sp',
            bold=True,
            size_hint_y=None,
            height=dp(80),
            color=get_color_from_hex(COLORS['on_surface'])
        )
        
        # Error label
        self.error_label = Label(
            text=self.error_message,
            color=get_color_from_hex(COLORS['error']),
            size_hint_y=None,
            height=dp(30),
            halign='center',
            text_size=(Window.width - dp(60), None)
        )
        
        # Form fields
        form_layout = BoxLayout(orientation='vertical', spacing=dp(15))
        
        # Name field
        name_layout = BoxLayout(orientation='vertical', spacing=dp(5))
        name_layout.add_widget(Label(
            text='Nome Completo',
            color=get_color_from_hex(COLORS['on_surface']),
            size_hint_y=None,
            height=dp(20)
        ))
        self.name_input = InputField(hint_text='Seu nome completo')
        name_layout.add_widget(self.name_input)
        
        # Email field
        email_layout = BoxLayout(orientation='vertical', spacing=dp(5))
        email_layout.add_widget(Label(
            text='Email',
            color=get_color_from_hex(COLORS['on_surface']),
            size_hint_y=None,
            height=dp(20)
        ))
        self.email = InputField(hint_text='seu@email.com')
        email_layout.add_widget(self.email)
        
        # Password field
        password_layout = BoxLayout(orientation='vertical', spacing=dp(5))
        password_layout.add_widget(Label(
            text='Senha (mínimo 6 caracteres)',
            color=get_color_from_hex(COLORS['on_surface']),
            size_hint_y=None,
            height=dp(20)
        ))
        self.password = InputField(hint_text='••••••••', password=True)
        password_layout.add_widget(self.password)
        
        # Add fields to form
        form_layout.add_widget(name_layout)
        form_layout.add_widget(email_layout)
        form_layout.add_widget(password_layout)
        
        # Register button
        register_btn = RoundedButton(text='CRIAR CONTA')
        register_btn.bind(on_press=self.register)
        
        # Back to login
        back_btn = Button(
            text='← Voltar para o login',
            background_color=(0, 0, 0, 0),
            color=get_color_from_hex(COLORS['primary']),
            size_hint_y=None,
            height=dp(50)
        )
        back_btn.bind(on_press=self.go_to_login)
        
        # Add all widgets to main layout
        main_layout.add_widget(header)
        main_layout.add_widget(self.error_label)
        main_layout.add_widget(form_layout)
        main_layout.add_widget(register_btn)
        main_layout.add_widget(back_btn)
        
        # Add a spacer to push content up
        main_layout.add_widget(BoxLayout(size_hint_y=1))
        
        # Add main layout to screen
        self.add_widget(main_layout)
    
    def validate_form(self):
        name = self.name_input.text.strip()
        email = self.email.text.strip()
        password = self.password.text.strip()
        
        if not all([name, email, password]):
            self.show_error('Por favor, preencha todos os campos')
            return False
            
        if len(name.split()) < 2:
            self.show_error('Por favor, insira seu nome completo')
            return False
            
        if not re.match(r'^[^@]+@[^@]+\.[^@]+$', email):
            self.show_error('Por favor, insira um email válido')
            return False
            
        if len(password) < 6:
            self.show_error('A senha deve ter no mínimo 6 caracteres')
            return False
            
        return True
    
    def show_error(self, message):
        self.error_message = message
        self.error_label.text = message
        anim = Animation(opacity=1, duration=0.3) + Animation(opacity=1, duration=2) + Animation(opacity=0, duration=0.3)
        anim.start(self.error_label)
    
    def register(self, instance):
        if not self.validate_form():
            return
            
        self.is_loading = True
        
        # Simulate network delay
        def do_register(dt):
            result = self.db.add_user(
                self.email.text, 
                self.password.text, 
                self.name_input.text
            )
            
            if result == 1:
                self.show_success('Conta criada com sucesso!')
                # Go back to login after a short delay
                def go_to_login(dt):
                    self.parent.transition.direction = 'right'
                    self.parent.current = 'login'
                    # Clear form
                    self.name_input.text = ''
                    self.email.text = ''
                    self.password.text = ''
                Clock.schedule_once(go_to_login, 1.5)
            else:
                self.show_error('Este email já está em uso')
                
            self.is_loading = False
            
        Clock.schedule_once(do_register, 0.5)
    
    def show_success(self, message):
        self.error_label.color = get_color_from_hex(COLORS['secondary'])
        self.error_message = message
        self.error_label.text = message
        anim = Animation(opacity=1, duration=0.3) + Animation(opacity=1, duration=1)
        anim.start(self.error_label)
        
    def go_to_login(self, instance):
        self.parent.transition.direction = 'right'
        self.parent.current = 'login'

class Calculator(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = dp(12)
        self.padding = [dp(15)]
        self.size_hint = (1, 1)
        self.last_was_operator = False
        self.last_number = ''
        
        # Main container with shadow effect
        main_box = BoxLayout(orientation='vertical', spacing=dp(12))
        
        # Display with history
        self.history_label = Label(
            text='',
            font_size='20sp',
            halign='right',
            color=(0.7, 0.7, 0.7, 1),
            size_hint=(1, 0.2),
            text_size=(Window.width - dp(40), None),
            valign='bottom'
        )
        
        # Main display
        self.display = TextInput(
            text='0',
            font_size='52sp',
            readonly=True,
            halign='right',
            background_color=(0.95, 0.95, 0.95, 1),
            foreground_color=(0.1, 0.1, 0.1, 1),
            size_hint=(1, 0.4),
            multiline=False,
            padding=[20, 20],
            font_name='Roboto',
            background_normal='',
            background_active='',
            cursor_blink=False
        )
        
        # Add display to display container
        display_container = BoxLayout(orientation='vertical', size_hint=(1, 0.4), spacing=0)
        display_container.add_widget(self.history_label)
        display_container.add_widget(self.display)
        
        # Buttons grid
        buttons = [
            ['C', '⌫', '%', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['00', '0', '.', '=']
        ]
        
        # Create buttons grid
        grid = GridLayout(cols=4, spacing=dp(10), size_hint=(1, 0.6))
        
        for row in buttons:
            for label in row:
                btn = Button(
                    text=label,
                    font_size='28sp',
                    background_normal='',
                    background_color=self.get_button_color(label),
                    color=(1, 1, 1, 1) if label not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '00', '.'] else (0.1, 0.1, 0.1, 1),
                    border=(0, 0, 0, 0),
                    font_name='Roboto',
                    bold=True if label == '=' else False,
                    size_hint=(1, 1),
                    background_down='atlas://data/images/defaulttheme/button_pressed'
                )
                btn.bind(on_press=self.on_button_press)
                btn.bind(on_press=self.on_button_down)
                btn.bind(on_release=self.on_button_up)
                grid.add_widget(btn)
        
        # Add all widgets to main layout
        main_box.add_widget(display_container)
        main_box.add_widget(grid)
        self.add_widget(main_box)
    
    def get_button_color(self, label):
        if label in ['C', '⌫']:
            return get_color_from_hex('#F44336')  # Red for clear/delete
        elif label in ['+', '-', '*', '/', '=']:
            return get_color_from_hex(COLORS['primary'])
        elif label == '%':
            return get_color_from_hex('#9C27B0')  # Purple for percentage
        else:
            return get_color_from_hex('#F5F5F5')  # Light gray for numbers
    
    def on_button_down(self, instance):
        # Button press animation
        instance.opacity = 0.7
    
    def on_button_up(self, instance):
        # Button release animation
        instance.opacity = 1
    
    def format_number(self, num):
        # Format number with thousand separators
        try:
            if '.' in num:
                num_parts = num.split('.')
                return f"{int(num_parts[0]):,}.{num_parts[1]}"
            return f"{int(num):,}"
        except:
            return num
    
    def on_button_press(self, instance):
        current = self.display.text.replace(',', '')  # Remove formatting for calculations
        button_text = instance.text
        
        if button_text == 'C':
            self.display.text = '0'
            self.history_label.text = ''
            self.last_was_operator = False
            return
            
        elif button_text == '⌫':
            if len(current) > 1:
                self.display.text = self.format_number(current[:-1])
            else:
                self.display.text = '0'
            return
            
        elif button_text == '=':
            try:
                # Replace × with * and ÷ with / for evaluation
                expression = self.history_label.text + current
                expression = expression.replace('×', '*').replace('÷', '/')
                result = str(eval(expression))
                self.history_label.text = expression + ' ='
                self.display.text = self.format_number(result)
            except Exception as e:
                self.display.text = 'Erro'
                self.history_label.text = ''
            self.last_was_operator = False
            return
            
        elif button_text in '+-*/':
            if not self.last_was_operator:  # Prevent multiple operators in a row
                self.history_label.text += current + ' ' + button_text + ' '
                self.display.text = '0'
                self.last_was_operator = True
                return
                
        elif button_text == '%':
            try:
                result = str(float(current) / 100)
                self.display.text = self.format_number(result)
            except:
                self.display.text = 'Erro'
            return
            
        else:  # Number or decimal point
            if current == '0' or self.last_was_operator or self.display.text == 'Erro':
                self.display.text = button_text
            else:
                # Prevent multiple decimal points
                if button_text == '.' and '.' in current:
                    return
                self.display.text = current + button_text
                # Format the number as user types
                if button_text.isdigit() or button_text == '0':
                    self.display.text = self.format_number(self.display.text)
            self.last_was_operator = False

class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.build_ui()
    
    def build_ui(self):
        # Main container
        # Set window minimum size for better visibility
        Window.minimum_width = 400
        Window.minimum_height = 700
        
        main_layout = BoxLayout(orientation='vertical', padding=dp(15), spacing=dp(15))
        
        # Header
        header = BoxLayout(orientation='vertical', size_hint=(1, 0.2))
        welcome_label = Label(
            text='Bem-vindo(a)!', 
            font_size='24sp',
            bold=True,
            color=get_color_from_hex(COLORS['on_surface'])
        )
        
        # Welcome message
        welcome_message = Label(
            text='Calculadora',
            font_size='20sp',
            halign='center',
            color=get_color_from_hex(COLORS['on_surface'])
        )
        
        header.add_widget(welcome_label)
        header.add_widget(welcome_message)
        
        # Calculator
        calculator = Calculator()
        
        # Logout button
        logout_btn = RoundedButton(
            text='SAIR',
            size_hint=(0.8, None),
            height=dp(50),
            pos_hint={'center_x': 0.5}
        )
        logout_btn.bind(on_press=self.logout)
        
        # Add widgets to main layout
        main_layout.add_widget(header)
        main_layout.add_widget(calculator)
        main_layout.add_widget(logout_btn)
        
        # Add main layout to screen
        self.add_widget(main_layout)
    
    def logout(self, instance):
        self.parent.transition.direction = 'right'
        self.parent.current = 'login'

class MyApp(App):
    def build(self):
        # Set app theme
        self.set_theme()
        
        # Create the screen manager with fade transition
        sm = ScreenManager(transition=FadeTransition())
        
        # Add screens
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(RegisterScreen(name='register'))
        sm.add_widget(WelcomeScreen(name='welcome'))
        
        return sm
    
    def set_theme(self):
        # Set window background color
        from kivy.core.window import Window
        Window.clearcolor = get_color_from_hex(COLORS['background'])
        
        # Set label default styles
        from kivy.config import Config
        Config.set('kivy', 'keyboard_mode', 'systemanddock')
        
        # Set text selection color
        from kivy.utils import get_hex_from_color
        Config.set('kivy', 'selection_color', get_hex_from_color(get_color_from_hex(COLORS['primary']) + [0.3]))

if __name__ == '__main__':
    MyApp().run()
