import os
import re

# Define the directory paths
posts_dir = "_posts"
pages_dir = "_pages"

# Define replacements for ingredients, dosages, and instructions
replacements = {
    # Ingredient replacements
    r"chilies|chili peppers": "chili",
    r"garlic, crushed or finely chopped": "garlic, minced",
    r"ginger, grated": "ginger, minced",
    r"coconut \(milk\)": "coconut milk",
    r"tomato, chopped or crushed": "chopped tomatoes",
    r"onion, chopped": "chopped onion",
    r"fenugreek leaves, crushed": "crushed fenugreek leaves",
    r"coriander powder": "ground coriander",
    r"cumin powder": "ground cumin",
    r"turmeric powder": "ground turmeric",
    r"garam masala powder": "garam masala",
    r"red chili powder": "ground red chili",
    r"black cardamon": "black cardamom",
    r"green cardamon": "green cardamom",
    r"bay leaf": "bay leaves",
    
    # Dosage replacements
    r"1tsp": "1 tsp",
    r"1tbsp": "1 tbsp",
    r"1/2 tsp": "½ tsp",
    r"1/4 tsp": "¼ tsp",
    r"1/2 cup": "½ cup",
    r"1 - 2 tsp": "1-2 tsp",
    r"2 - 4 tbsp": "2-4 tbsp",
    
    # Instruction replacements
    r"fry spices": "Heat oil and fry spices.",
    r"add chopped onions, fry until golden": "Add chopped onion and fry until golden.",
    r"add garlic and chilies, make paste": "Add garlic, chili, and ginger, and stir to form a paste.",
    r"add tomatoes, water and ginger, cook for 15\+ minutes": "Add chopped tomatoes, water, and ginger. Simmer for 15 minutes.",
    r"add lentils, cook until done": "Add lentils and cook until tender.",
    r"add cream, salt, and fresh cilantro to finish": "Stir in cream, salt, and fresh cilantro to finish."
}

# Function to apply replacements
def apply_replacements(file_path):
    with open(file_path, "r") as file:
        content = file.read()
    for pattern, replacement in replacements.items():
        content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)
    with open(file_path, "w") as file:
        file.write(content)

# Process all markdown files in the directories
for directory in [posts_dir, pages_dir]:
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                apply_replacements(os.path.join(root, file))

print("Changes applied successfully!")