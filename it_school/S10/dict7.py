colors = {
    "red": "#FF0000",
    "green": "#00FF00",
    "blue": "#0000FF",

}

for k, v in colors.items():
    colors[k] = colors[k].strip("#")

print(colors)

def noner(dict_in, key):
    dict_in[key] = None

noner(colors, "red")
print(colors)