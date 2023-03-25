from exercise5.utils import createFile, toUpperCaseInFile

createFile("exercise5/test.txt", "Qua ratione literae in Classe prima tractentur primum tibi scribam.\nLatinorum \
scriptorum Horatium, Quintiliani librum decimum, Plauti Trinummum et denique \
Taciti Annales legimus, quorum omnium maxime Horatii carmina mihi placent, quae \
Director, vel potius nos, Directore gubernante interpretamur.\nLocis vero \
obscurioribus, ut quisque suam proferat sententiam haud raro accidit."
)

toUpperCaseInFile("exercise5/test.txt", ["a", "e", "i", "o", "u"])