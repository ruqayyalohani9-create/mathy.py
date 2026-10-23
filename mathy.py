import tkinter as tk

def calculate():
    numbers = entry.get().split(",")
    frequency = {}

    for n in numbers:
        n = n.strip()

        if n in frequency:
            frequency[n] += 1
        else:
            frequency[n] = 1

    result = ""

    for n in sorted(frequency):
        result += n + " = " + str(frequency[n]) + "\n"

    output.config(text=result)

    graph.delete("all")

    for i, n in enumerate(sorted(frequency)):
        x = frequency[n] * 30
        y = 30 + i * 40

        graph.create_text(20, y, text=n)
        graph.create_rectangle(
            40, y - 10, 40 + x, y + 10,
            fill="skyblue"
        )

root = tk.Tk()
root.title("Frequency and Bar Graph")
root.geometry("400x450")

tk.Label(root, text="Enter numbers separated by commas").pack()

entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Calculate", command=calculate).pack()

output = tk.Label(root, text="")
output.pack()

graph = tk.Canvas(root, width=350, height=250, bg="white")
graph.pack()

root.mainloop()