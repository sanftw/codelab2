from tkinter import *
from PIL import ImageTk, Image
import requests
from io import BytesIO
import pokebase as pb
#create the window and size
window = Tk()
window.title("pokedex")
window.geometry("600x700")
#picture for pokedex
img = ImageTk.PhotoImage(Image.open('original (1).png'))
banner = Label(window, image=img)
banner.image = img
banner.pack()

label1 = Label(window, text="Enter name of pokemon", fg="black", pady=20, font="Helvetica")
label1.pack()

#entry field to enter pokemon name
pokemon_input = Entry(window)
pokemon_input.pack(pady=20)

#function call to search pokemon
def search():
    details.delete('1.0', END)
    pokemon = pb.pokemon(pokemon_input.get())
    try:
        #get image from api
        response = requests.get(pokemon.sprites.front_default)
        image = ImageTk.PhotoImage(Image.open(BytesIO(response.content)))
        pokemon_image.config(image=image)
        pokemon_image.image = image

        #get info from api
        abilities = ', '.join(ability.ability.name for ability in pokemon.abilities)
        types = ', '.join(poketype.type.name for poketype in pokemon.types)

        #display details
        data = f"""{pokemon_input.get().capitalize()}
        \nHeight: {pokemon.height}
        \nWeight: {pokemon.weight}
        \nAbilities: {abilities}
        \nTypes: {types}
        """
        
        details.insert(END, data)
        
    except AttributeError:
        #if pokemon name is invalid
        details.insert(END, "not a valid pokemon")
        pokemon_image.config(image='')

#button code to search for pokemon
btn = Button(window, bd='4', text="submit", fg='red', bg='yellow', font="Helvetica", command=search)
btn.pack()

#display pokemon image retrieved from api
pokemon_image = Label(window)
pokemon_image.pack(pady=30)

#text box to display details
details = Text(window, bg='light blue')
details.pack()

#run 
window.mainloop()