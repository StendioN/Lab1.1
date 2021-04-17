from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelHeader
from math import exp
from kivy_garden.graph import Graph, MeshLinePlot
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.label import Label

Builder.load_string('''
<LineCircle>:
    orientation: 'landscape'
    canvas:
        Color:
            rgba: 0, 1, 0, 1
        Line:
            width: 40
            cap: 'none'
            circle:
                (self.center_x, self.center_y, min(self.width, self.height) / 4, 0, 108)
        Color:
            rgba: 1, 0.45, 0, 1       
        Line:
            width: 40
            cap: 'none'
            circle:
                (self.center_x, self.center_y, min(self.width, self.height) / 4, 108, 216)               
        Color:
            rgba: 0, 0, 0, 1       
        Line:
            width: 40
            cap: 'none'
            circle:
                (self.center_x, self.center_y, min(self.width, self.height) / 4, 216, 360)
''')


class LineCircle(Widget):
    pass


class Lab2App(App):
    def graphic(self):
        graph = Graph(xlabel='X', ylabel='Y', x_ticks_minor=5,
                      x_ticks_major=1, y_ticks_major=1,
                      y_grid_label=True, x_grid_label=True, padding=5,
                      x_grid=True, y_grid=True, xmin=-6, xmax=6, ymin=-1, ymax=10)
        plot = MeshLinePlot(color=[1, 1, 0, 1])
        plot.points = [(x * 0.1, exp(x * 0.1)) for x in range(-60, 60)]
        graph.add_plot(plot)
        return graph
    def build(self):
        self.icon = 'icon.png'
        tb_panel = TabbedPanel()
        tb_panel.default_tab_text = 'Student'
        tb_panel.default_tab_content = Label(text = 'Лялін Ігор\n' \
                                                    'Група ІО-81\n' \
                                                    'ЗК ІО-8118')
        graph = Lab2App.graphic(self)
        th_text_head1 = TabbedPanelHeader(text='exp(x)')
        th_text_head1.content = graph
        tb_panel.add_widget(th_text_head1)
        th_text_head2 = TabbedPanelHeader(text='circle')
        th_text_head2.content = LineCircle()
        tb_panel.add_widget(th_text_head2)
        return tb_panel


if __name__ == '__main__':
    Lab2App().run()
