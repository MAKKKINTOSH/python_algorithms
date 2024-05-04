import tkinter as tk


class Visualizer:
    render_step = 10  # Количество пикселей в 1 значении координатной сетки

    def __init__(self, window_width: int, window_height: int):
        self.window = tk.Tk()
        self.window.geometry(f'{window_width}x{window_height}')
        self.canvas = tk.Canvas(self.window, width=window_width, height=window_height)
        self.canvas.grid()
        self.__draw_axis()

    def __draw_axis(self):
        self.canvas.update()
        x = self.canvas.winfo_width() // 2
        y = self.canvas.winfo_height() // 2
        self.canvas.configure(scrollregion=(-x, -y, x, y))
        self.canvas.create_line(x, 0, -x, 0)
        self.canvas.create_line(0, y, 0, -y)

    def draw_line(self, h1: list[int], h2: list[int]):
        self.canvas.create_line(
            h1[0] * self.render_step,
            -h1[1] * self.render_step,
            h2[0] * self.render_step,
            -h2[1] * self.render_step, fill='red'
        )

    def visualize_triangles(self, triangles: list[list[list[int]]]):
        for t in triangles:
            sides = [(t[i - 1], t[i]) for i in range(0, 3)]
            for s in sides:
                self.draw_line(s[0], s[1])
        self.canvas.mainloop()