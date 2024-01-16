import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

image = Image.open('dogs.jpeg')

image = np.array(image)
image = np.rot90(image)

plt.imshow(image)
plt.axis('off')
plt.savefig('dogs_rotated.jpeg')
