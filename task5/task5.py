import matplotlib.pyplot as plt
import cv2

image=cv2.imread("a2.jpe")
b,g,r=cv2.split(image)

img1=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)

plt.figure(figsize=(11,7))

plt.subplot(231)
plt.title("FIGURE 1")
plt.imshow(b)
plt.imshow(img1,cmap="hot",vmin=0,vmax=255)

plt.subplot(232)
plt.title("FIGURE 2")
plt.imshow(b)

plt.subplot(233)
plt.title("FIGURE 3")
plt.imshow(g)

plt.subplot(234)
plt.title("FIGURE 3")
plt.imshow(g)

plt.subplot(234)
plt.title("FIGURE 4")
plt.imshow(r)

plt.subplot(235)
plt.title("FIGURE 5")
plt.imshow(img1)

plt.savefig("RGB.png")

plt.show()
