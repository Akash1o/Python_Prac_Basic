import tkinter as tk

def sum():
    num1=int(input.get())
    num2=int(inputs.get())
    result_lab.config(text=f"Sum is  :{num1+num2}")

window=tk.Tk()
window.title("Sum of two")
window.geometry("400x300")

label=tk.Label(window,text="First Number:")
input=tk.Entry(window,width=30)
label.pack()
input.pack()


labels=tk.Label(window,text="Second Number:")
inputs=tk.Entry(window,width=30)
labels.pack()
inputs.pack()

button=tk.Button(window,text="Calculate Sum", command=sum)
button.pack()

result_lab=tk.Label(window,text="Sum is :")
result_lab.pack()

window.mainloop()