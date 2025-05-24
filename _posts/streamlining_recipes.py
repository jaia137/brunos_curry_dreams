import os
import re

# Define the directory paths
posts_dir = "_posts"
pages_dir = "_pages"

# Define replacements for ingredients, dosages, and instructions
replacements = {
    # Ingredient replacements
    r"\bchilies|chili peppers\b": "chili",
    r"\bgarlic, crushed or finely chopped\b": "garlic, minced",
    r"\bginger, grated\b": "ginger, minced",
    r"\bcoconut \(milk\)\b": "coconut milk",
    r"\btomato, chopped or crushed\b": "chopped tomatoes",
    r"\bonion, chopped\b": "chopped onion",
    r"\bfenugreek leaves, crushed\b": "crushed fenugreek leaves",
    r"\bcoriander powder\b": "ground coriander",
    r"\bcumin powder\b": "ground cumin",
    r"\bturmeric powder\b": "ground turmeric",
    r"\bgaram masala powder\b": "garam masala",
    r"\bred chili powder\b": "ground red chili",
    r"\bblack cardamon\b": "black cardamom",
    r"\bgreen cardamon\b": "green cardamom",
    r"\bbay leaf\b": "bay leaves",
    
    # Dosage replacements
    r"\b1tsp\b": "1 tsp",
    r"\b1tbsp\b": "1 tbsp",
    r"\b1/2 tsp\b": "½ tsp",
    r"\b1/4 tsp\b": "¼ tsp",
    r"\b1/2 cup\b": "½ cup",
    r"\b1 - 2 tsp\b": "1-2 tsp",
    r"\b1/2 - 1 tsp\b": "½-1 tsp",
    r"\b2 - 4 tbsp\b": "2-4 tbsp",
    
    # Instruction replacements
    r"\bfry spices\b(?!\.)": "Heat oil and fry spices.",
    r"\badd chopped onions, fry until golden\b": "Add chopped onion and fry until golden.",
    r"\badd garlic and chilies, make paste\b": "Add garlic, chili, and ginger, and stir to form a paste.",
    r"\badd tomatoes, water and ginger, cook for 15\+ minutes\b": "Add chopped tomatoes, water, and ginger. Simmer for 15 minutes.",
    r"\badd lentils, cook until done\b": "Add lentils and cook until tender.",
    r"\badd cream, salt, and fresh cilantro to finish\b": "Stir in cream, salt, and fresh cilantro to finish."
}

# Function to apply replacements
def apply_replacements(file_path):
    with open(file_path, "r") as file:
        content = file.read()
    for pattern, replacement in replacements.items():
        # Use re.sub with word boundaries to avoid repeated replacements
        content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)
    
    # Final cleanup for specific repetition issue
    content = re.sub(r"Heat oil and Heat oil and fry spices\.\.", "Heat oil and fry spices.", content)
    
    with open(file_path, "w") as file:
        file.write(content)

# Process all markdown files in the directories
for directory in [posts_dir, pages_dir]:
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                apply_replacements(os.path.join(root, file))

print("Changes applied successfully!")