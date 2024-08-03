import tkinter as tk
from time import time

class TripleClickApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Triple Click Detection")
        
        # Kreiranje okvira (frame) za centriranje labele
        frame = tk.Frame(root)
        frame.pack(expand=True)
        
        self.label = tk.Label(frame, text="Click here", font=("Arial", 24), bg="lightgrey", padx=20, pady=10)
        self.label.pack(pady=20)
        
        self.label.bind("<Button-1>", self.on_click)
        
        self.click_count = 0
        self.first_click_time = 0
    
    def on_click(self, event):
        current_time = time()
        
        if self.click_count == 0:
            self.first_click_time = current_time
            self.click_count += 1
        elif current_time - self.first_click_time <= 0.5: 
            self.click_count += 1
            if self.click_count == 3:
                print(f"Triple click detected! Total clicks: {self.click_count}")
                self.click_count = 0 
        else:
            self.click_count = 1  
            self.first_click_time = current_time

if __name__ == "__main__":
    root = tk.Tk()
    app = TripleClickApp(root)
    root.mainloop()
