from PIL import Image
import numpy as np
import subprocess
import json


# open as grayscale image 
image = Image.open('test_digit.png').convert("L")
# convert to np array (2D)
image = np.asarray(image)
# invert colors: white background with black digit to black background with white digit
# to match the MNIST dataset
image = (-1 * image + 255)
# convert to vector
flattened_vector = image.flatten()

# create the command line (query)
query = 'emulators\\NanoEdgeAI_Class_Emulator.exe neai_classification --knowledge_path emulators\\knowledge.dat --array '
for i in range(len(flattened_vector)):
        query += str(flattened_vector[i]) + ' '
        
# you can uncomment the following line to print the request made to the emulator
# print(query)

# execute the command in cmd
result = subprocess.check_output(query, shell=True)
dic_result = json.loads(result.decode('utf-8'))

# convert response as dictonnary and print the result
print('this digit is a',dic_result['results'][0]['class_name'][-1])

