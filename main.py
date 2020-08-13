from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.config import Config


class JustCalcApp(App):
    def __init__(self, **kwargs):
        App.__init__(self, **kwargs)
        self.base_grid_layout = None
        self.user_label = None
        self.middle_grid_layout = None
        self.number_7_button = None
        self.number_8_button = None
        self.number_9_button = None
        self.plus_button = None
        self.minus_button = None
        self.number_4_button = None
        self.number_5_button = None
        self.number_6_button = None
        self.multiply_button = None
        self.divide_button = None
        self.number_1_button = None
        self.number_2_button = None
        self.number_3_button = None
        self.power_button = None
        self.root_button = None
        self.lower_grid_layout = None
        self.point_button = None
        self.number_0_button = None
        self.clear_button = None
        self.return_button = None
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
        self.base_grid_layout.add_widget(self.user_label)

        self.middle_grid_layout = GridLayout()
        self.middle_grid_layout.cols = 5
        self.middle_grid_layout.size_hint = (1, 0.45)

        self.number_7_button = Button()
        self.customize_number_button(self.number_7_button, '7')
        self.number_7_button.on_press = self.number_7_button_press
        self.number_7_button.on_release = self.number_7_button_release

        self.number_8_button = Button()
        self.customize_number_button(self.number_8_button, '8')
        self.number_8_button.on_press = self.number_8_button_press
        self.number_8_button.on_release = self.number_8_button_release

        self.number_9_button = Button()
        self.customize_number_button(self.number_9_button, '9')
        self.number_9_button.on_press = self.number_9_button_press
        self.number_9_button.on_release = self.number_9_button_release

        self.plus_button = Button()
        self.customize_action_button(self.plus_button, '+')
        self.plus_button.on_press = self.plus_button_press
        self.plus_button.on_release = self.plus_button_release

        self.minus_button = Button()
        self.customize_action_button(self.minus_button, '−')
        self.minus_button.on_press = self.minus_button_press
        self.minus_button.on_release = self.minus_button_release

        self.number_4_button = Button()
        self.customize_number_button(self.number_4_button, '4')
        self.number_4_button.on_press = self.number_4_button_press
        self.number_4_button.on_release = self.number_4_button_release

        self.number_5_button = Button()
        self.customize_number_button(self.number_5_button, '5')
        self.number_5_button.on_press = self.number_5_button_press
        self.number_5_button.on_release = self.number_5_button_release

        self.number_6_button = Button()
        self.customize_number_button(self.number_6_button, '6')
        self.number_6_button.on_press = self.number_6_button_press
        self.number_6_button.on_release = self.number_6_button_release

        self.multiply_button = Button()
        self.customize_action_button(self.multiply_button, '×')
        self.multiply_button.on_press = self.multiply_button_press
        self.multiply_button.on_release = self.multiply_button_release

        self.divide_button = Button()
        self.customize_action_button(self.divide_button, '÷')
        self.divide_button.on_press = self.divide_button_press
        self.divide_button.on_release = self.divide_button_release

        self.number_1_button = Button()
        self.customize_number_button(self.number_1_button, '1')
        self.number_1_button.on_press = self.number_1_button_press
        self.number_1_button.on_release = self.number_1_button_release

        self.number_2_button = Button()
        self.customize_number_button(self.number_2_button, '2')
        self.number_2_button.on_press = self.number_2_button_press
        self.number_2_button.on_release = self.number_2_button_release

        self.number_3_button = Button()
        self.customize_number_button(self.number_3_button, '3')
        self.number_3_button.on_press = self.number_3_button_press
        self.number_3_button.on_release = self.number_3_button_release

        self.power_button = Button()
        self.customize_action_button(self.power_button, '^')
        self.power_button.on_press = self.power_button_press
        self.power_button.on_release = self.power_button_release

        self.root_button = Button()
        self.customize_action_button(self.root_button, '√')
        self.root_button.on_press = self.root_button_press
        self.root_button.on_release = self.root_button_release

        self.lower_grid_layout = GridLayout()
        self.lower_grid_layout.cols = 4
        self.lower_grid_layout.size_hint = (1, 0.15)

        self.point_button = Button()
        self.customize_number_button(self.point_button, '.')
        self.point_button.on_press = self.point_button_press
        self.point_button.on_release = self.point_button_release

        self.number_0_button = Button()
        self.customize_number_button(self.number_0_button, '0')
        self.number_0_button.on_press = self.number_0_button_press
        self.number_0_button.on_release = self.number_0_button_release

        self.clear_button = Button()
        self.customize_clear_button(self.clear_button, 'C')
        self.clear_button.on_press = self.clear_button_press
        self.clear_button.on_release = self.clear_button_release

        self.return_button = Button()
        self.customize_return_button(self.return_button, '=')
        self.return_button.on_press = self.return_button_press
        self.return_button.on_release = self.return_button_release

        self.base_grid_layout.add_widget(self.middle_grid_layout)
        self.base_grid_layout.add_widget(self.lower_grid_layout)

        return self.base_grid_layout

    def customize_number_button(self, button, text):
        button.text = text
        button.font_size = '24sp'
        button.background_normal = ''
        button.background_down = ''
        button.background_color = [0.1, 0.74, 0.61, 1]
        if text == '0' or text == '.':
            self.lower_grid_layout.add_widget(button)
        else:
            self.middle_grid_layout.add_widget(button)

    def customize_action_button(self, button, text):
        button.text = text
        button.font_size = '24sp'
        button.background_normal = ''
        button.background_down = ''
        button.background_color = [0.9, 0.49, 0.13, 1]
        self.middle_grid_layout.add_widget(button)

    def customize_clear_button(self, button, text):
        button.text = text
        button.font_size = '24sp'
        button.background_normal = ''
        button.background_down = ''
        button.background_color = [0.61, 0.35, 0.71, 1]
        self.lower_grid_layout.add_widget(button)

    def customize_return_button(self, button, text):
        button.text = text
        button.font_size = '24sp'
        button.size_hint = (2, 1)
        button.background_normal = ''
        button.background_down = ''
        button.background_color = [0.61, 0.35, 0.71, 1]
        self.lower_grid_layout.add_widget(button)

    @staticmethod
    def number_button_press(button):
        button.background_color = [0.09, 0.63, 0.52, 1]

    def number_button_release(self, button):
        button.background_color = [0.1, 0.74, 0.61, 1]
        self.draw_normal_color()
        if self.calculated:
            self.user_label.text = ''
            self.calculated = False

    @staticmethod
    def action_button_press(button):
        button.background_color = [0.83, 0.33, 0, 1]

    def action_button_release(self, button):
        button.background_color = [0.9, 0.49, 0.13, 1]
        self.draw_normal_color()
        if self.calculated:
            self.user_label.text = ''
            self.calculated = False

    @staticmethod
    def control_button_press(button):
        button.background_color = [0.56, 0.27, 0.68, 1]

    @staticmethod
    def control_button_release(button):
        button.background_color = [0.61, 0.35, 0.71, 1]

    def number_7_button_press(self):
        self.number_button_press(self.number_7_button)

    def number_7_button_release(self):
        self.number_button_release(self.number_7_button)
        self.user_label.text += self.number_7_button.text

    def number_8_button_press(self):
        self.number_button_press(self.number_8_button)

    def number_8_button_release(self):
        self.number_button_release(self.number_8_button)
        self.user_label.text += self.number_8_button.text

    def number_9_button_press(self):
        self.number_button_press(self.number_9_button)

    def number_9_button_release(self):
        self.number_button_release(self.number_9_button)
        self.user_label.text += self.number_9_button.text

    def number_4_button_press(self):
        self.number_button_press(self.number_4_button)

    def number_4_button_release(self):
        self.number_button_release(self.number_4_button)
        self.user_label.text += self.number_4_button.text

    def number_5_button_press(self):
        self.number_button_press(self.number_5_button)

    def number_5_button_release(self):
        self.number_button_release(self.number_5_button)
        self.user_label.text += self.number_5_button.text

    def number_6_button_press(self):
        self.number_button_press(self.number_6_button)

    def number_6_button_release(self):
        self.number_button_release(self.number_6_button)
        self.user_label.text += self.number_6_button.text

    def number_1_button_press(self):
        self.number_button_press(self.number_1_button)

    def number_1_button_release(self):
        self.number_button_release(self.number_1_button)
        self.user_label.text += self.number_1_button.text

    def number_2_button_press(self):
        self.number_button_press(self.number_2_button)

    def number_2_button_release(self):
        self.number_button_release(self.number_2_button)
        self.user_label.text += self.number_2_button.text

    def number_3_button_press(self):
        self.number_button_press(self.number_3_button)

    def number_3_button_release(self):
        self.number_button_release(self.number_3_button)
        self.user_label.text += self.number_3_button.text

    def point_button_press(self):
        self.number_button_press(self.point_button)

    def point_button_release(self):
        self.number_button_release(self.point_button)
        self.user_label.text += self.point_button.text

    def number_0_button_press(self):
        self.number_button_press(self.number_0_button)

    def number_0_button_release(self):
        self.number_button_release(self.number_0_button)
        self.user_label.text += self.number_0_button.text

    def plus_button_press(self):
        self.action_button_press(self.plus_button)

    def plus_button_release(self):
        self.action_button_release(self.plus_button)
        self.user_label.text += self.plus_button.text

    def minus_button_press(self):
        self.action_button_press(self.minus_button)

    def minus_button_release(self):
        self.action_button_release(self.minus_button)
        self.user_label.text += self.minus_button.text

    def multiply_button_press(self):
        self.action_button_press(self.multiply_button)

    def multiply_button_release(self):
        self.action_button_release(self.multiply_button)
        self.user_label.text += self.multiply_button.text

    def divide_button_press(self):
        self.action_button_press(self.divide_button)

    def divide_button_release(self):
        self.action_button_release(self.divide_button)
        self.user_label.text += self.divide_button.text

    def power_button_press(self):
        self.action_button_press(self.power_button)

    def power_button_release(self):
        self.action_button_release(self.power_button)
        self.user_label.text += self.power_button.text

    def root_button_press(self):
        self.action_button_press(self.root_button)

    def root_button_release(self):
        self.action_button_release(self.root_button)
        self.user_label.text += self.root_button.text

    def clear_button_press(self):
        self.control_button_press(self.clear_button)

    def clear_button_release(self):
        self.control_button_release(self.clear_button)
        self.draw_normal_color()
        if self.calculated:
            self.user_label.text = ''
            self.calculated = False
        else:
            self.user_label.text = self.user_label.text[:-1]

    def return_button_press(self):
        self.control_button_press(self.return_button)

    def return_button_release(self):
        self.control_button_release(self.return_button)
        if not self.calculated:
            if not self.calculate():
                self.draw_warning_color()

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

    def draw_warning_color(self):
        Window.clearcolor = [1, 0.8, 0.82, 1]
        self.user_label.color = [0.75, 0.22, 0.17, 1]

    def draw_normal_color(self):
        Window.clearcolor = [0.93, 0.94, 0.95, 1]
        self.user_label.color = [0.16, 0.5, 0.73, 1]


if __name__ == '__main__':
    Config.set('kivy', 'window_icon', 'icons8-math-100.ico')
    Window.clearcolor = [0.93, 0.94, 0.95, 1]
    JustCalcApp().run()
