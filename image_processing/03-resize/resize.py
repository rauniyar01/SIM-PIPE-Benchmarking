import cv2
import time
import psutil

def measure_performance():
    process = psutil.Process()
    start_time = time.time()
    start_cpu_times = process.cpu_times()
    
    # Perform resizing
    img = cv2.imread('/out/rotated_image.jpg')
    if img is None:
        print("Error loading image")
        return
    height, width = img.shape[:2]
    resized_img = cv2.resize(img, (width // 2, height // 2))
    cv2.imwrite('/out/resized_image.jpg', resized_img)
    
    end_time = time.time()
    end_cpu_times = process.cpu_times()
    duration = end_time - start_time
    total_cpu_time = (end_cpu_times.user - start_cpu_times.user) + (end_cpu_times.system - start_cpu_times.system)
    cpu_usage_percentage = (total_cpu_time / duration) * 100 if duration > 0 else 0
    memory_usage = process.memory_info().rss / (1024 * 1024)
    
    with open('/out/performance_resize.txt', 'w') as f:
        f.write(f"Duration: {duration} seconds\n")
        f.write(f"CPU Usage: {cpu_usage_percentage} %\n")
        f.write(f"Memory Usage: {memory_usage} MB\n")

if __name__ == "__main__":
    measure_performance()
