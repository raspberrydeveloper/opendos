import threading
import time
import requests
import tkinter as tk


class MyThread(threading.Thread):
    def __init__(self, domain):
        threading.Thread.__init__(self)
        self.domain = domain
        self.stop_event = threading.Event()

    def run(self):
        while not self.stop_event.is_set():
            try:
                response = requests.post(self.domain)
                print(response)
            except Exception as e:
                print(e)
            time.sleep(0.001)

    def stop(self):
        self.stop_event.set()


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Multi-Threaded POST Requests")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.domain_label = tk.Label(self, text="Enter Domain:")
        self.domain_label.pack(side="left")
        self.domain_entry = tk.Entry(self)
        self.domain_entry.pack(side="left")
        self.start_button = tk.Button(self, text="Start", command=self.start_threads)
        self.start_button.pack(side="left")
        self.stop_button = tk.Button(self, text="Stop", command=self.stop_threads)
        self.stop_button.pack(side="left")

    def start_threads(self):
        domain = self.domain_entry.get()
        self.threads = []
        for i in range(10):
            thread = MyThread(domain)
            thread.start()
            self.threads.append(thread)

    def stop_threads(self):
        for thread in self.threads:
            thread.stop()


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
