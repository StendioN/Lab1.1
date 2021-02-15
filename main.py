from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.tabbedpanel import TabbedPanelHeader
from kivy.uix.label import Label


class Lab1App(App):
    def build(self):
        self.icon = 'icon.png'
        tb_panel = TabbedPanel()
        tb_panel.default_tab_text = 'Student'
        tb_panel.default_tab_content = Label(text = 'Лялін Ігор\n' \
                                       'Група ІО-81\n' \
                                       'ЗК ІО-8118')
        th_text_head = TabbedPanelHeader(text='Tab')
        th_text_head.content = Label()
        tb_panel.add_widget(th_text_head)
        return tb_panel


if __name__ == '__main__':
    Lab1App().run()
