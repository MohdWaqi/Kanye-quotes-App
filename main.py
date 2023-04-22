import tkinter
import requests


def new_quote():
    new_response = requests.get("https://api.kanye.rest")
    quote = new_response.json()["quote"]
    canvas.itemconfig(text, text=f"{quote}")


window = tkinter.Tk()
window.title("Kanye quotes")
window.config(padx=50, pady=50)
canvas = tkinter.Canvas(width=400, height=420)
message_image = tkinter.PhotoImage(file="background.png")
canvas.create_image(200, 200, image=message_image)
text = canvas.create_text(200, 200, text="", width=250, font=("Arial", 30, "bold"), fill="White")
canvas.grid(row=0, column=0)
emoji_image = tkinter.PhotoImage(file="kanye.png")
button = tkinter.Button(image=emoji_image, command=new_quote)
button.grid(row=1, column=0)
new_quote()
window.mainloop()
