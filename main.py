from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.config import Config


class NumberButton(Button):
    def __init__(self, just_calc_app, **kwargs):
        Button.__init__(self, **kwargs)
        self.just_calc_app = just_calc_app
        self.customize(kwargs['text'])

    def customize(self, text):
        self.text = text
        self.font_size = '24sp'
        self.background_normal = ''
        self.background_down = ''
        self.background_color = [0.1, 0.74, 0.61, 1]
        if self.text == '.' or self.text == '0':
            self.just_calc_app.lower_grid_layout.add_widget(self)
        else:
            self.just_calc_app.upper_number_grid_layout.add_widget(self)

    def on_press(self):
        self.background_color = [0.09, 0.63, 0.52, 1]
        return Button.on_press(self)

    def on_release(self):
        self.background_color = [0.1, 0.74, 0.61, 1]
        self.just_calc_app.draw_normal_color()
        if self.just_calc_app.calculated:
            self.just_calc_app.user_label.text = ''
            self.just_calc_app.calculated = False
        self.just_calc_app.user_label.text += self.text
        return Button.on_release(self)


class OperationButton(Button):
    def __init__(self, just_calc_app, **kwargs):
        Button.__init__(self, **kwargs)
        self.just_calc_app = just_calc_app
        self.customize(kwargs['text'])

    def customize(self, text):
        self.text = text
        self.font_size = '24sp'
        self.background_normal = ''
        self.background_down = ''
        self.background_color = [0.9, 0.49, 0.13, 1]
        self.just_calc_app.operation_grid_layout.add_widget(self)

    def on_press(self):
        self.background_color = [0.83, 0.33, 0, 1]
        return Button.on_press(self)

    def on_release(self):
        self.background_color = [0.9, 0.49, 0.13, 1]
        self.just_calc_app.draw_normal_color()
        if self.just_calc_app.calculated:
            self.just_calc_app.user_label.text = ''
            self.just_calc_app.calculated = False
        self.just_calc_app.user_label.text += self.text
        return Button.on_release(self)


class ClearButton(Button):
    def __init__(self, just_calc_app, **kwargs):
        Button.__init__(self, **kwargs)
        self.just_calc_app = just_calc_app
        self.customize()

    def customize(self):
        self.text = 'C'
        self.font_size = '24sp'
        self.background_normal = ''
        self.background_down = ''
        self.background_color = [0.61, 0.35, 0.71, 1]
        self.just_calc_app.lower_grid_layout.add_widget(self)

    def on_press(self):
        self.background_color = [0.56, 0.27, 0.68, 1]
        return Button.on_press(self)

    def on_release(self):
        self.background_color = [0.61, 0.35, 0.71, 1]
        self.just_calc_app.draw_normal_color()
        if self.just_calc_app.calculated:
            self.just_calc_app.user_label.text = ''
            self.just_calc_app.calculated = False
        else:
            self.just_calc_app.user_label.text = self.just_calc_app.user_label.text[:-1]
        return Button.on_release(self)


class ReturnButton(Button):
    def __init__(self, just_calc_app, **kwargs):
        Button.__init__(self, **kwargs)
        self.just_calc_app = just_calc_app
        self.customize()

    def customize(self):
        self.text = '='
        self.font_size = '24sp'
        self.size_hint = (2, 1)
        self.background_normal = ''
        self.background_down = ''
        self.background_color = [0.61, 0.35, 0.71, 1]
        self.just_calc_app.lower_grid_layout.add_widget(self)

    def on_press(self):
        self.background_color = [0.56, 0.27, 0.68, 1]
        return Button.on_press(self)

    def on_release(self):
        self.background_color = [0.61, 0.35, 0.71, 1]
        if not self.just_calc_app.calculated:
            if self.just_calc_app.user_label.text != '' and not self.just_calc_app.calculate():
                self.just_calc_app.draw_warning_color()
        return Button.on_release(self)


class JustCalcApp(App):
    def __init__(self, **kwargs):
        App.__init__(self, **kwargs)
        self.base_grid_layout = None
        self.user_label = None
        self.middle_grid_layout = None
        self.lower_grid_layout = None
        self.upper_number_grid_layout = None
        self.operation_grid_layout = None

        self.number_order = list('.0789456123')
        self.number_buttons = []

        self.operation_order = list('+−×÷^√')
        self.operation_buttons = []

        self.calculated = False

    def build(self):
        self.base_grid_layout = GridLayout()
        self.base_grid_layout.rows = 3

        self.user_label = Label()
        self.user_label.color = [0.16, 0.5, 0.73, 1]
        self.user_label.text = ''
        self.user_label.max_lines = 100
        self.user_label.font_size = '36sp'
        self.user_label.size_hint = (1, 0.4)

        self.middle_grid_layout = GridLayout()
        self.middle_grid_layout.cols = 2
        self.middle_grid_layout.size_hint = (1, 0.45)

        self.lower_grid_layout = GridLayout()
        self.lower_grid_layout.cols = 4
        self.lower_grid_layout.size_hint = (1, 0.15)

        self.upper_number_grid_layout = GridLayout()
        self.upper_number_grid_layout.cols = 3
        self.upper_number_grid_layout.size_hint = (0.6, 1)

        self.operation_grid_layout = GridLayout()
        self.operation_grid_layout.cols = 2
        self.operation_grid_layout.size_hint = (0.4, 1)

        for number_item in self.number_order:
            self.number_buttons.append(NumberButton(self, text=number_item))

        for operation_item in self.operation_order:
            self.operation_buttons.append(OperationButton(self, text=operation_item))

        ClearButton(self)
        ReturnButton(self)

        self.base_grid_layout.add_widget(self.user_label)

        self.middle_grid_layout.add_widget(self.upper_number_grid_layout)
        self.middle_grid_layout.add_widget(self.operation_grid_layout)

        self.base_grid_layout.add_widget(self.middle_grid_layout)
        self.base_grid_layout.add_widget(self.lower_grid_layout)

        return self.base_grid_layout

    def draw_warning_color(self):
        Window.clearcolor = [1, 0.8, 0.82, 1]
        self.user_label.color = [0.75, 0.22, 0.17, 1]

    def draw_normal_color(self):
        Window.clearcolor = [0.93, 0.94, 0.95, 1]
        self.user_label.color = [0.16, 0.5, 0.73, 1]

    def calculate(self):
        current_action_count = 0
        for char in list(self.user_label.text):
            if char in '+−×÷^√.':
                current_action_count += 1
                if current_action_count > 1:
                    return False
            elif char not in '+−×÷^√.':
                current_action_count = 0
        numbers = []
        actions = []
        str_number = ''
        for char in list(self.user_label.text):
            if char in '+−×÷^√':
                try:
                    numbers.append(float(str_number))
                except ValueError:
                    return False
                str_number = ''
                actions.append(char)
            else:
                str_number += char
        try:
            numbers.append(float(str_number))
        except ValueError:
            return False
        position = 0
        while position < len(actions):
            if actions[position] == '^':
                numbers[position] = numbers[position] ** numbers[position + 1]
                numbers.pop(position + 1)
                actions.pop(position)
            elif actions[position] == '√':
                numbers[position] = numbers[position + 1] ** (1 / numbers[position])
                numbers.pop(position + 1)
                actions.pop(position)
            position += 1
        position = 0
        while position < len(actions):
            if actions[position] == '×':
                numbers[position] = numbers[position] * numbers[position + 1]
                numbers.pop(position + 1)
                actions.pop(position)
            elif actions[position] == '÷':
                try:
                    numbers[position] = numbers[position] / numbers[position + 1]
                except ZeroDivisionError:
                    return False
                numbers.pop(position + 1)
                actions.pop(position)
            position += 1
        position = 0
        while position < len(actions):
            if actions[position] == '+':
                numbers[position] = numbers[position] + numbers[position + 1]
                numbers.pop(position + 1)
                actions.pop(position)
            elif actions[position] == '−':
                numbers[position] = numbers[position] - numbers[position + 1]
                numbers.pop(position + 1)
                actions.pop(position)
            position += 1
        if str(numbers[0]).endswith('.0'):
            result = int(numbers[0])
        else:
            result = numbers[0]
        self.user_label.text += '={0}'.format(result)
        self.calculated = True
        return True


if __name__ == '__main__':
    Config.set('kivy', 'window_icon', 'icons8-math-100.ico')
    Window.clearcolor = [0.93, 0.94, 0.95, 1]
    JustCalcApp().run()
