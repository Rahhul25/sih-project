import os
import pickle

# Path to your dataset directory
dataset_dir = 'datsset-1'  # Change this to the path of your dataset

# Get a list of class names (assuming each subdirectory represents a class)
class_names = sorted(os.listdir(dataset_dir))

# Create a dictionary to map class names to class indices
class_indices = {class_name: index for index, class_name in enumerate(class_names)}

# Save the class indices to a pickle file
with open('class_new.pkl', 'wb') as file:
    pickle.dump(class_indices, file)

print("Class indices saved to 'class_indices.pkl'")
