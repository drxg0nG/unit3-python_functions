# The raise syntax
# Basic Syntax
"""
raise ExceptionType("Your message!")
Examples:
raise ValueError("Quantity must be at least 1")
raise TypeError("Expected a player object, got a potato")
raise PermissionError("You are not a mod, nice try though")
"""

# Just Returning
def open_loot_box(player, qty):
    if qty <= 0:
        return None
    # Rest of code

# Raising Exception
def open_loot_box(player, qty):
    if qty <= 0:
        raise ValueError("Bad quantity")
    # Rest of code

VALID_PROTEINS = ['chicken', 'steak', 'barbacoa', 'carnitas']
VALID_RICE = ['white', 'brown', 'none']
VALID_BEANS = ['black', 'pinto', 'none']
MAX_FREE_EXTRAS = 3

def build_bowl(protein, rice, extras):
    """
    Build a Chipotle Bowl with validation
    
    ValueError: if protein is invalid
    TypeError: if extras is not a list
    """
    # Check if extras is a list
    if not isinstance(extras, list):
        raise TypeError("Extras must be a list")
    # Validate protein
    if protein.lower() not in VALID_PROTEINS:
        raise ValueError(f"'{protein}' isn't valid! Choose from: '{VALID_PROTEINS}'")
    return {
        "protein": protein.lower(),
        "rice": rice,
        "extras": extras,
        "price": 10.50,
    }

# Test the function
try:
    bowl = build_bowl("chicken", "brown", "corn")
    print(f"Created: {bowl}")
except Exception as e:
    print(f"Error: {e}")


