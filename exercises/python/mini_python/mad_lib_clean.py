# Madlib project
print ("Welcome to Pablo's Madlib exercise!")
#The following will prompt the user to enter words for the madlib.
girl = input("Type a common girls' name: ")
animal = input("Type a real or imaginary animal: ")
verb = input("Type a verb (eat, work, dance): ")
verb2 = input("Type another verb (sleep, run, sing): ")
obj =  input("Type an object (vase, desk,pen): ")
adjective = input("Type an adjective (floppy, dirty, loud): ")
past_verb = input("Type a past-tense verb (ran, died, laughed): ")
# The following will introduce the madlib and then print it out for the user.

print ("Thanks! Here's your madlib:")
print (
"Once upon a time there was a poor little girl named {} who lived in the forest with a(n) {}."
"She was forced to {} all day whole the {} sat around {}ing."
"But then one day the little girl found a magic {}.When {} picked up the {}, she found that anything she imagined came true."
"Soon, {} was making the {} {} while she chose to sit around and {}."
"After a while, the girl realized this was not a very {} thing to do and released the {} from her spell."
"They became best friends and {} every day, living happily ever after."
.format(girl, animal, verb, animal, verb2, obj, girl, obj, girl, animal, verb, verb2, adjective, animal, past_verb))
