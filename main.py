import math

# Öklid mesafesini hesaplayan fonksiyon
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

# 2D noktalardan oluşan liste
points = [(3, 3), (5, 8), (2, 9), (6, 3), (5, 4)]

# Mesafelerin saklanacağı liste
distances = []

# Her nokta çifti arasındaki mesafeyi hesapla ve distances listesine ekle
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)

# Minimum mesafeyi bul ve yazdır
min_distance = min(distances)
print("En kısa mesafe:", min_distance)
