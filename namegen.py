import random

def name_generator():
    first_names  =  ["Max",  "Alexa",  "Nate",  "Emma",  "Ryder",  "Ava",   "Jaxon",
                "Olivia",  "Dylan",  "Harper",  "Brody",  "Ella",  "Hunter",  "Mia",   "Tanner",
                "Sophia", "Jackson", "Chloe", "Cooper",  "Amelia",  "Austin",  "Lily",  "Logan",
                "Abigail", "Carter", "Emily",  "Grayson",  "Sofia",  "Jayden",  "Zoe",  "Mason",
                "Nora",  "Liam",  "Scarlett",  "Lucas",  "Hazel",  "Leo",  "Madelyn",   "Ethan",
                "Avery", "Owen", "Aria", "Wyatt", "Mila", "Henry",  "Layla",  "Jack",  "Evelyn",
                "Luke", "Grace", "Nathan", "Victoria",  "Ryan",  "Ariana",  "Evan",  "Penelope",
                "Joshua", "Brooklyn", "Brandon", "Audrey", "Jordan", "Clara", "Levi",  "Stella",
                "David", "Savannah", "Samuel", "Zara",  "Daniel",  "Violet",  "Isaac",  "Elena",
                "Andrew",  "Naomi",  "James",  "Camila",  "Nolan",  "Ruby",  "Josiah",  "Maria",
                "Gabriel", "Alice", "Anthony",  "Alexis",  "John",  "Elise",  "Adam",  "Gianna",
                "Michael", "Natalie", "Benjamin", "Faith", "William", "Aurora"]

    last_names = ["Williams", "Davis", "Anderson", "Gonzalez", "Martinez", "Harris",
                "Lopez", "Jackson", "Smith", "Johnson", "Brown",  "Wilson",  "Taylor",  "Clark",
                "Lewis", "Hall", "Adams", "Hill", "Turner", "White",  "Green",  "Allen",  "Lee",
                "Baker", "Murphy",  "Roberts",  "Cook",  "Carter",  "James",  "Gray",  "Rivera",
                "Collins", "Bell", "Wright", "Perez", "Stewart", "Bailey",  "Howard",  "Miller",
                "Davis", "Sullivan", "Rogers", "Reed", "Gomez", "Howard", "Robinson",  "Thomas",
                "Morgan", "Cruz", "Young", "Parker",  "Foster",  "Garcia",  "Reyes",  "Russell",
                "Simmons", "Mitchell", "Perry", "Sanchez", "Fisher", "Flores", "Evans",  "Diaz",
                "Simmons", "Murillo", "Ramirez", "Fletcher", "Alexander",  "Jones",  "Thompson",
                "Hernandez", "Hughes", "Phillips",  "Scott",  "Bennett",  "Jenkins",  "Stevens",
                "Watson",  "Robinson-Woods",  "Young-Bailey",  "Harris-Miller",  "Carter-Smith",
                "Williams-Cruz", "Bell-Wright", "Gomez-Davis"]
    
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)

    return f"{first_name} {last_name}"
