import socket
import tkinter as tk


def send_command():
    user_command = entry.get()
    try:
        client_socket.sendto(user_command.encode('utf-8'), server_address)
        print("Done!")
    except Exception as e:
        print(f"Помилка відправки команди: {e}")


def main():
    global client_socket, server_address, entry

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 3306)

    root = tk.Tk()
    root.title("Кліент")
    root.configure(bg="#ADD8E6")

    entry_frame = tk.Frame(root, bd=2, relief=tk.GROOVE)
    entry_frame.pack(padx=10, pady=10)

    entry = tk.Entry(entry_frame, width=100)
    entry.pack(side=tk.LEFT)

    send_button = tk.Button(entry_frame, text="Send Command", command=send_command)
    send_button.pack(side=tk.LEFT, padx=5)

    root.mainloop()


if __name__ == "__main__":
    main()
