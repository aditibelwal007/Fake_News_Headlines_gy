import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import random

# Categories and word banks
headlines_data = {
    "Tech": {
        "subjects": ["AI Robots", "Hackers", "Tech Billionaires", "Smartphones", "Quantum Computers"],
        "verbs": ["hack", "launch", "ban", "upgrade", "replace"],
        "objects": ["the internet", "blockchain", "social media", "digital wallets", "coding"],
        "locations": ["in Silicon Valley", "at CES", "in virtual reality", "on Mars", "in a garage"]
    },
    "Politics": {
        "subjects": ["Politicians", "Leaders", "Senators", "Presidents", "Governments"],
        "verbs": ["ban", "declare", "support", "leak", "censor"],
        "objects": ["free speech", "elections", "taxes", "fake news", "policies"],
        "locations": ["in the Parliament", "on live TV", "during a speech", "in the UN", "in a secret meeting"]
    },
    "Sci-Fi": {
        "subjects": ["Aliens", "Time Travelers", "Scientists", "Space Pirates", "Clones"],
        "verbs": ["invade", "create", "destroy", "manipulate", "reveal"],
        "objects": ["the moon", "a wormhole", "a black hole", "the multiverse", "time"],
        "locations": ["in a lab", "on Mars", "inside the sun", "in another dimension", "at NASA"]
    }
}

def generate_headline(category):
    """Generate a random headline for a given category."""
    data = headlines_data.get(category)
    return f"{random.choice(data['subjects'])} {random.choice(data['verbs'])} {random.choice(data['objects'])} {random.choice(data['locations'])}!"

def save_to_file(headlines):
    """Save headlines to a text file."""
    file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file:
        with open(file, "w") as f:
            f.write("\n".join(headlines))
        messagebox.showinfo("Saved", f"Headlines saved successfully to:\n{file}")

def main():
    current_headlines = []

    def on_generate():
        category = category_var.get()
        if category == "Select Category":
            messagebox.showwarning("Missing", "Please select a category.")
            return
        try:
            count = int(num_var.get())
            if count <= 0:
                raise ValueError
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a valid positive number.")
            return
        
        headlines = [generate_headline(category) for _ in range(count)]
        headlines_list.delete(0, tk.END)
        for hl in headlines:
            headlines_list.insert(tk.END, hl)
        current_headlines.clear()
        current_headlines.extend(headlines)

    def on_save():
        if not current_headlines:
            messagebox.showwarning("No headlines", "Generate headlines before saving.")
        else:
            save_to_file(current_headlines)

    # Root window
    root = tk.Tk()
    root.title("Fake News Headline Generator")
    root.geometry("550x450")
    root.resizable(False, False)
    root.configure(bg="#222222")

    # Title
    tk.Label(root, text="Fake News Headline Generator", font=("Helvetica", 16, "bold"), bg="#222222", fg="white").pack(pady=10)

    # Category dropdown
    category_var = tk.StringVar(value="Select Category")
    ttk.Combobox(root, textvariable=category_var, values=list(headlines_data.keys()), state="readonly").pack(pady=5)

    # Number of headlines
    num_var = tk.StringVar(value="5")
    tk.Label(root, text="Number of Headlines:", bg="#222222", fg="white").pack(pady=5)
    tk.Entry(root, textvariable=num_var, width=5).pack()

    # Buttons
    tk.Button(root, text="Generate Headlines", command=on_generate, bg="#4CAF50", fg="white", font=("Arial", 12)).pack(pady=5)
    tk.Button(root, text="Save Headlines", command=on_save, bg="#f44336", fg="white", font=("Arial", 12)).pack(pady=5)

    # Headlines listbox with scrollbar
    frame = tk.Frame(root)
    frame.pack(pady=10)
    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    headlines_list = tk.Listbox(frame, width=65, height=10, font=("Courier", 10), yscrollcommand=scrollbar.set)
    headlines_list.pack(side=tk.LEFT)
    scrollbar.config(command=headlines_list.yview)

    root.mainloop()

if __name__ == "__main__":
    main()
