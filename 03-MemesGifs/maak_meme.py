
#Eerste tekst

from PIL import Image, ImageFont, ImageDraw

# Laad de achtergrond afeebdling in de variabele: achtergrond
achtergrond = Image.open("meme_background.jpg")

# Afmetingen opslaan in eigen variabelen
breedte = achtergrond.width
hoogte = achtergrond.height

# Laad het Impact lettertype
lettertype = ImageFont.truetype("impact.ttf", 40)
# Vraag aan de ImageDraw module om een tekengebied te maken op de achtergrond afbeelding
tekengebied = ImageDraw.Draw(achtergrond)

# Tekst schrijven
tekst = "Meedoen met de muziekles"

# ZET HIER DE CODE MET DE BEREKENINGEN 

tekengebied.multiline_text((525,200), tekst, font=lettertype, fill=(0,0,0))


# Tweede tekst


# Laad het Impact lettertype
lettertype = ImageFont.truetype("impact.ttf", 40)
# Vraag aan de ImageDraw module om een tekengebied te maken op de achtergrond afbeelding
tekengebied = ImageDraw.Draw(achtergrond)

# Tekst schrijven
tekst = "Zeggen dat je allergisch"

# ZET HIER DE CODE MET DE BEREKENINGEN 

tekengebied.multiline_text((550,720), tekst, font=lettertype, fill=(0,0,0))


# Derde Tekst


# Laad het Impact lettertype
lettertype = ImageFont.truetype("impact.ttf", 40)
# Vraag aan de ImageDraw module om een tekengebied te maken op de achtergrond afbeelding
tekengebied = ImageDraw.Draw(achtergrond)

# Tekst schrijven
tekst = "voor noten bent "

# ZET HIER DE CODE MET DE BEREKENINGEN 

tekengebied.multiline_text((605,760), tekst, font=lettertype, fill=(0,0,0))

# Het resultaat tonen
achtergrond.show()

# En opslaan onder een andere naam
achtergrond.save("meme_met_tekst.jpg")



