import sys
import cv2

path = sys.argv[1] if len(sys.argv) > 1 else "image.jpg"
image = cv2.imread(path)
if image is None:
    sys.exit(f"Не удалось загрузить изображение: {path}")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(gray, (5, 5), 0)

edges = cv2.Canny(blurred, 50, 150)
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

result = image.copy()
cv2.drawContours(result, contours, -1, (0, 255, 0), 2)

cv2.imwrite("result.jpg", result)
print(f"Готово: найдено контуров - {len(contours)}, сохранено в result.jpg")
