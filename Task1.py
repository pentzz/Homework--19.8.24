oscar_winners = {"Leonardo DiCaprio", "Meryl Streep", "Denzel Washington", "Emma Stone",
                 "Tom Hanks", "Natalie Portman", "Robert De Niro", "Al Pacino"}

titanic_actors = {"Leonardo DiCaprio", "Kate Winslet", "Billy Zane", "Kathy Bates"}

dark_knight_actors = {"Christian Bale", "Heath Ledger", "Michael Caine", "Gary Oldman", "Aaron Eckhart"}

avengers_actors = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Mark Ruffalo",
                   "Chris Hemsworth", "Jeremy Renner"}

iron_man_actors = {"Robert Downey Jr.", "Gwyneth Paltrow", "Terrence Howard"}

legendary_actors = {"Al Pacino", "Robert De Niro", "Marlon Brando", "Jack Nicholson", "Dustin Hoffman"}

actor_list = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Leonardo DiCaprio", "Tom Hanks"}

movie_cast = {"Tom Hanks", "Tom Cruise", "Will Smith", "Matt Damon", "Brad Pitt"}


dark_knight_rises_actors = {"Christian Bale", "Michael Caine", "Gary Oldman",
"Tom Hardy", "Joseph Gordon-Levitt"}


# Task a
oscar_winners.add("Emma Watson")

# Task b
# oscar_winners.clear()

# Task c
oscar_winners2 = oscar_winners.copy()

# Task d
oscar_winners.remove("Meryl Streep")
print(oscar_winners)

# Task e
print(dark_knight_actors.intersection(titanic_actors))

# Task f
isdisj: bool = avengers_actors.isdisjoint(iron_man_actors)
print("Yes") if not isdisj else print("No")

# Task g
print(actor_list.issubset(oscar_winners))

# Task h
print(actor_list.issubset(oscar_winners))

# Task i
movie_cast.pop()

# Task j
movie_cast.discard("Matt Damon")

# Task k
print(titanic_actors.difference(oscar_winners))

# Task l
print(titanic_actors.symmetric_difference(dark_knight_actors))

# Task m
oscar_winners.update({"Lewis-Day Daniel", "Blanchett Cate"})

# Task n
print(titanic_actors.union(dark_knight_actors))

# Task o
all_actors_in_rises = dark_knight_actors <= dark_knight_rises_actors
print(all_actors_in_rises)

# Task p
legendary_includes_oscar = legendary_actors >= oscar_winners
print(legendary_includes_oscar)

# Task q
not_in_iron_man = avengers_actors - iron_man_actors
print(not_in_iron_man)

# Task r
only_in_one_movie = dark_knight_actors ^ avengers_actors
print(only_in_one_movie)

# Task s
all_actors_combined = dark_knight_actors | iron_man_actors
print(all_actors_combined)

# Task t
frozen_legendary_actors = frozenset(legendary_actors)
print(frozen_legendary_actors)