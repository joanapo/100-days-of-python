from prettytable import PrettyTable

# Exploring prettytable to build a Pokemon table

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align= "l"

print(table)