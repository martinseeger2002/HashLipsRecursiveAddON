import json

# Define file paths
traitindex_path = './build/json/traitindex.json'
metadata_path = './build/json/_metadata.json'
output_path = './build/json/childtraitindex.json'

# Load JSON files
with open(traitindex_path, 'r') as file:
    traitindex = json.load(file)

with open(metadata_path, 'r') as file:
    metadata = json.load(file)

# Function to get the index value from the traitindex
def get_trait_index(trait_type, trait_value):
    trait_type_key = trait_type.split()[1]  # Adjusting for splitting on space
    if trait_type_key in traitindex:
        for index, value in traitindex[trait_type_key].items():
            if value == trait_value:
                return index
    print(f"Trait not found: {trait_type} - {trait_value}")  # Debug statement
    return '00'

# Process the metadata
processed_metadata = []

for item in metadata:
    traits_index = ''.join([get_trait_index(attr['trait_type'], attr['value']) for attr in item.get('attributes', [])])
    processed_metadata.append({
        'name': item['name'],
        'traitindex': traits_index
    })

# Save the processed metadata to a new JSON file
with open(output_path, 'w') as file:
    json.dump(processed_metadata, file, indent=2)

print(f"Processed metadata saved to {output_path}")
