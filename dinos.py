# Let's start by figuring out how many dinosaurs we have. Count the number of dinosaurs.

SELECT COUNT(id) FROM dinos;
331
# We want to open up our own version of Jurassic Park, but this time only with dinosaurs who are actually from the Jurassic period. Find all the dinosaurs from the Jurassic period.

SELECT name FROM dinos WHERE period = 'Jurassic';

 Yuanmousaurus
 Yinlong
 Yingshanosaurus
 Yimenosaurus
 Yangchuanosaurus
 Yandusaurus
 Vulcanodon
 Tuojiangosaurus
 Torvosaurus
 Yunnanosaurus
 Sinraptor
 Stegosaurus
 Seismosaurus
 Segisaurus
 Scutellosaurus
 Scelidosaurus
 Saurophaganax
 Sarcosaurus
 Shunosaurus
 Rhoetosaurus

# Jurassic Park was a huge success for us. Now we want to open up a sequel park: Cretaceous Park. This time though, we're a little more organized, and we want to know how much space all these dinosaurs are going to take up. Find the total sum length of all the dinosaurs from the Cretaceous period.

SELECT SUM(length) FROM dinos WHERE period ='Cretaceous';
1366.45

# Great news! Our board of investors recently secured us a large island where we can put all the dinosaurs from both Jurassic Park and Cretaceous Park. This new park will be called Juraceous Park, which according to our focus groups really rolls off the tongue. Find all the dinosaurs from either the Jurassic OR Cretaceous periods, and order them by their species name alphabetically.

SELECT name FROM dinos WHERE period ='Jurassic' OR period = 'Cretaceous' ORDER BY species;

 name           
-------------------------
 Afrovenator
 Spinosaurus
 Kentrosaurus
 Deltadromeus
 Lophostropheus
 Apatosaurus
 Dromaeosaurus
 Styracosaurus
 Becklespinax
 Hypacrosaurus
 Brachiosaurus
 Struthiomimus
 Dryosaurus
 Leaellynasaura
 Erlikosaurus
 Protoceratops
 Deinonychus
 Centrosaurus
 Dryptosaurus
 Jaxartosaurus

# Saurischians are the "lizard hipped" order of dinosaurs, and one of the two main branches. All carnivorous dinosaurs are Saurischians, but not all Saurischians are carnivorous. Find all the dinosaurs from the t_order Saurischia that are Herbivorous.

SELECT name, t_order FROM dinos WHERE diet = 'Herbivorous';

 name           |   t_order    
-------------------------+--------------
 Wuerhosaurus            | Ornithischia
 Yuanmousaurus           | Saurischia
 Yinlong                 | Ornithischia
 Yingshanosaurus         | Ornithischia
 Yimenosaurus            | Saurischia
 Yandusaurus             | Ornithischia
 Vulcanodon              | Saurischia
 Valdosaurus             | Ornithischia
 Tuojiangosaurus         | Ornithischia
 Tylocephale             | Ornithischia
 Tsagantegia             | Ornithischia
 Triceratops             | Ornithischia
 Torosaurus              | Ornithischia
 Thescelosaurus          | Ornithischia
 Zephyrosaurus           | Ornithischia
 Zalmoxes                | Ornithischia
 Udanoceratops           | Ornithischia
 Telmatosaurus           | Ornithischia
 Tarchia                 | Ornithischia
 Tanius                  | Ornithischia

# Dinosaur names are hard to remember. Find the shortest dinosaur, and rename it Shortie.

SELECT name, length FROM dinos ORDER BY length;
UPDATE dinos SET name = 'Shortie' WHERE name = 'Liaoxiornis';

name           | length 
-------------------------+--------
 Shortie                 |   0.08
 Confuciusornis          |   0.25
 Shanag                  |   0.45
 Microceratops           |    0.5
 Archaeopteryx           |    0.5
 Shuvuuia                |    0.6
 Micropachycephalosaurus |    0.6
 Compsognathus           |   0.65
 Microraptor             |    0.8
 Gasparinisaura          |    0.8
 Juravenator             |    0.8
 Podokesaurus            |    0.9
 Pisanosaurus            |    0.9
 Bambiraptor             |      1
 Nqwebasaurus            |      1
 Procompsognathus        |      1
 Eoraptor                |      1
 Lesothosaurus           |      1
 Urbacodon               |      1
 Sinosauropteryx         |      1

# It's the first day of Dino School, and we're doing roll call. Find the alphabetically first dinosaur, so we can make sure they're present for class.

SELECT name from dinos ORDER BY name;

 name           
-------------------------
 Aardonyx
 Abelisaurus
 Achelousaurus
 Achillobator
 Acrocanthosaurus
 Aegyptosaurus
 Afrovenator
 Agilisaurus
 Alamosaurus
 Albertaceratops
 Albertosaurus
 Alectrosaurus
 Alioramus
 Allosaurus
 Alvarezsaurus
 Amargasaurus
 Ammosaurus
 Ampelosaurus
 Amygdalodon
 Anatotitan
