import socket
import tkinter as tk
import threading
import time


def display_received_text(text):
    received_text_2 = "Done: " + text + "\n"
    return received_text_2


def receive_data():
    def clear_display(color):
        canvas.delete("all")
        canvas.configure(bg=color)

    def draw_pixel(x, y, color):
        canvas.create_rectangle(x, y, x + 1, y + 1, fill=color, outline=color)

    def draw_line(x0, y0, x1, y1, color):
        canvas.create_line(x0, y0, x1, y1, fill=color)

    def draw_rectangle(x0, y0, w, h, color):
        canvas.create_rectangle(x0, y0, x0 + w, y0 + h, fill=color, outline=color)

    def fill_rectangle(x0, y0, w, h, color):
        canvas.create_rectangle(x0, y0, x0 + w, y0 + h, fill=color, outline=color)

    def draw_ellipse(x0, y0, radius_x, radius_y, color):
        canvas.create_oval(x0 - radius_x, y0 - radius_y, x0 + radius_x, y0 + radius_y, fill=color, outline=color)

    def fill_ellipse(x0, y0, radius_x, radius_y, color):
        canvas.create_oval(x0 - radius_x, y0 - radius_y, x0 + radius_x, y0 + radius_y, fill=color, outline=color)

    def draw_circle(x0, y0, radius, color):
        canvas.create_oval(x0 - radius, y0 - radius, x0 + radius, y0 + radius, fill=color, outline=color)

    def fill_circle(x0, y0, radius, color):
        canvas.create_oval(x0 - radius, y0 - radius, x0 + radius, y0 + radius, fill=color, outline=color)

    def draw_rounded_rectangle(x0, y0, w, h, radius, color):
        canvas.create_rectangle(x0, y0, x0 + w, y0 + h, fill=color, outline=color)
        canvas.create_arc(x0, y0, x0 + 2 * radius, y0 + 2 * radius, start=90, extent=90, fill=color, outline=color)
        canvas.create_arc(x0 + w - 2 * radius, y0, x0 + w, y0 + 2 * radius, start=0, extent=90, fill=color,
                          outline=color)
        canvas.create_arc(x0, y0 + h - 2 * radius, x0 + 2 * radius, y0 + h, start=180, extent=90, fill=color,
                          outline=color)
        canvas.create_arc(x0 + w - 2 * radius, y0 + h - 2 * radius, x0 + w, y0 + h, start=270, extent=90, fill=color,
                          outline=color)

    def fill_rounded_rectangle(x0, y0, w, h, radius, color):
        canvas.create_rectangle(x0, y0, x0 + w, y0 + h, fill=color, outline=color)
        canvas.create_arc(x0, y0, x0 + 2 * radius, y0 + 2 * radius, start=90, extent=90, fill=color, outline=color)
        canvas.create_arc(x0 + w - 2 * radius, y0, x0 + w, y0 + 2 * radius, start=0, extent=90, fill=color,
                          outline=color)
        canvas.create_arc(x0, y0 + h - 2 * radius, x0 + 2 * radius, y0 + h, start=180, extent=90, fill=color,
                          outline=color)
        canvas.create_arc(x0 + w - 2 * radius, y0 + h - 2 * radius, x0 + w, y0 + h, start=270, extent=90, fill=color,
                          outline=color)

    def draw_text(x0, y0, color, font_number, length, text):
        font = ("Arial", font_number)
        canvas.create_text(x0, y0, fill=color, font=font, text=text)

    def draw_timer(seconds, color):
        degrees = int(360 / seconds)
        current_degrees = 0
        canvas.create_oval(100, 100, 500, 500, outline=color)
        for i in range(seconds + 1):
            canvas.delete("timer_arc")
            canvas.create_arc(100, 100, 500, 500, start=90, extent=-current_degrees, outline="", fill=color,
                              tags="timer_arc")
            root.update()
            time.sleep(1)
            current_degrees += degrees
            if current_degrees == 360:
                canvas.create_oval(100, 100, 500, 500, fill=color)

    while True:
        data, client_address = server_socket.recvfrom(1024)
        command = data.decode('utf-8')
        print(command)
        if command:
            try:
                eval(command)
                text_area.insert(tk.END, display_received_text(command))
            except Exception as e:
                print(f"Помилка виконання команди: {e}")
                text_area.insert(tk.END, e)
        else:
            print("Помилка розбору команди")
        root.update()


def main():
    global root, server_socket, text_area, canvas

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 3306)
    server_socket.bind(server_address)

    root = tk.Tk()
    root.title("Сервер")
    root.configure(bg="#8FBC8F")
    canvas_frame = tk.Frame(root, bd=2, relief=tk.GROOVE)
    canvas_frame.grid(row=0, column=0, padx=10, pady=10)

    canvas = tk.Canvas(canvas_frame, width=2500, height=600, bg="white")
    canvas.pack()

    text_frame = tk.Frame(root, bd=2, relief=tk.GROOVE)
    text_frame.grid(row=1, column=0, padx=10, pady=10)

    text_area = tk.Text(text_frame, height=25, width=50)
    text_area.pack()

    print("Сервер запущено")
    receive_thread = threading.Thread(target=receive_data)
    receive_thread.daemon = True
    receive_thread.start()

    root.mainloop()


if __name__ == "__main__":
    main()
