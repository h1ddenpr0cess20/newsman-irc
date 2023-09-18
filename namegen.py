import random

def name_generator():
    first_names  =  ['Aurora', 'Grayson', 'Gianna', 'Layla', 'Mila', 'Benjamin', 'Stella', 'Nate', 'Alexa', 'Daniel', 'Mia', 'Avery', 'Zara', 'Scarlett', 
                    'Clara', 'Jaxon', 'Maria', 'Dylan', 'Logan', 'Isaac', 'Savannah', 'Amelia', 'Jackson', 'Gabriel', 'Lucas', 'Evan', 'Hunter', 'Jayden', 
                    'Michael', 'Leo', 'Austin', 'Nathan', 'Sofia', 'Cooper', 'Levi', 'Carter', 'Aria', 'Ariana', 'Emma', 'Zoe', 'Brooklyn', 'Chloe', 'Ryder', 
                    'Jordan', 'Lily', 'Elena', 'Olivia', 'Audrey', 'Ava', 'Evelyn', 'Violet', 'Adam', 'Owen', 'Liam', 'Faith', 'Harper', 'Brody', 'Emily', 
                    'Brandon', 'Wyatt', 'Alice', 'Luke', 'Natalie', 'Josiah', 'Max', 'Nolan', 'Abigail', 'Anthony', 'Tanner', 'Joshua', 'Sophia', 'Andrew', 
                    'Ella', 'Samuel', 'Hazel', 'Nora', 'Ruby', 'Penelope', 'Mason', 'Ethan', 'Henry', 'Victoria', 'Alexis', 'Jack', 'Camila', 'Grace', 'Naomi', 
                    'David', 'John', 'James', 'Madelyn', 'Elise', 'Ryan', 'William', 'Dustin']

    last_names = ['Williams', 'Adams', 'Taylor', 'Rogers', 'Young', 'Perez', 'Thompson', 'Miller', 'Scott', 'Thomas', 'Sanchez', 'Lee', 
                    'Fletcher', 'Russell', 'Martinez', 'Anderson', 'Stewart', 'Bailey', 'Johnson', 'Foster', 'Lopez', 'Garcia', 'Reyes', 
                    'Jackson', 'Simmons', 'Alexander', 'Cruz', 'Cook', 'Clark', 'James', 'Diaz', 'Brown', 'Wright', 'Allen', 'Bell', 'Hernandez', 
                    'Phillips', 'Stevens', 'Harris', 'Turner', 'Morgan', 'Hughes', 'Watson', 'Reed', 'White', 'Parker', 'Wilson', 'Davis', 'Gray', 
                    'Howard', 'Gonzalez', 'Jenkins', 'Gomez', 'Collins', 'Smith', 'Bennett', 'Ramirez', 'Robinson', 'Murillo', 'Hill', 'Carter', 
                    'Rivera', 'Mitchell', 'Baker', 'Evans', 'Green', 'Lewis', 'Fisher', 'Perry', 'Flores', 'Sullivan', 'Hall', 'Murphy', 'Roberts', 'Jones']
    
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)

    return f"{first_name} {last_name}"
