text = """
Aunque hoy cumplas
trescientos treinta y seis meses
la matusalénica edad no se te nota cuando
en el instante en que vencen los crueles
entrás a averiguar la alegría del mundo
y mucho menos todavía se te nota
cuando volás gaviotamente sobre las fobias
o desarbolás los nudosos rencores

buena edad para cambiar estatutos y horóscopos
para que tu manantial mane amor sin miseria
para que te enfrentes al espejo que exige
y pienses que estás linda
y estés linda

casi no vale la pena desearte júbilos y lealtades
ya que te van a rodear como ángeles o veleros

es obvio y comprensible
que las manzanas y los jazmines
y los cuidadores de autos y los ciclistas
y las hijas de los villeros
y los cachorros extraviados
y los bichitos de san antonio
y las cajas de fósforo
te consideren una de los suyos

de modo que desearte un feliz cumpleaños
podría ser tan injusto con tus felices
cumpledías
acordate de esta ley de tu vida
si hace algún tiempo fuiste desgraciada
eso también ayuda a que hoy se afirme
tu bienaventuranza

de todos modos para vos no es novedad
que el mundo
y yo
te queremos de veras
pero yo siempre un poquito más que el mundo
"""

list_text = text.split()

def lettersRepeat (list):
  maximum = 0
  max_word = ''
  words = {}
  for word in list:
    if word in words:
      words[word] += 1
    else:
      words[word] = 1
    if words[word] > maximum:
      maximum = words[word]
      max_word = word
  return max_word, maximum, words

print(lettersRepeat(list_text))