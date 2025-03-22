import cv2
import time
import psutil
import os
import sys

def measure_performance():
    print("Starting filter image process")
    process = psutil.Process()
    start_time = time.time()
    start_cpu_times = process.cpu_times()
    
    # Check if input file exists
    input_path = '/in/input.jpg'
    output_path = '/out/filtered_image.jpg'
    
    print(f"Checking if input file exists at: {input_path}")
    if not os.path.exists(input_path):
        print(f"Error: Input file not found at {input_path}")
        print(f"Current directory contents: {os.listdir('.')}")
        print(f"Input directory contents: {os.listdir('/in') if os.path.exists('/in') else 'Directory not found'}")
        sys.exit(1)
    
    # Perform filtering
    print(f"Loading image from {input_path}")
    img = cv2.imread(input_path)
    if img is None:
        print(f"Error: Could not load image at {input_path}")
        sys.exit(1)
    
    print(f"Image loaded successfully, shape: {img.shape}")
    print("Applying Gaussian blur filter")
    blurred_img = cv2.GaussianBlur(img, (5, 5), 0)
    
    print(f"Writing filtered image to {output_path}")
    success = cv2.imwrite(output_path, blurred_img)
    if not success:
        print(f"Error: Failed to write output image to {output_path}")
        sys.exit(1)
    
    print(f"Verifying output file exists at: {output_path}")
    if not os.path.exists(output_path):
        print(f"Error: Output file was not created at {output_path}")
        sys.exit(1)
    
    print(f"Output file successfully created, size: {os.path.getsize(output_path)} bytes")
    
    end_time = time.time()
    end_cpu_times = process.cpu_times()
    duration = end_time - start_time
    total_cpu_time = (end_cpu_times.user - start_cpu_times.user) + (end_cpu_times.system - start_cpu_times.system)
    cpu_usage_percentage = (total_cpu_time / duration) * 100 if duration > 0 else 0
    memory_usage = process.memory_info().rss / (1024 * 1024)
    
    performance_path = '/out/performance_filter.txt'
    print(f"Writing performance metrics to {performance_path}")
    with open(performance_path, 'w') as f:
        f.write(f"Duration: {duration} seconds\n")
        f.write(f"CPU Usage: {cpu_usage_percentage} %\n")
        f.write(f"Memory Usage: {memory_usage} MB\n")
    
    print("Filter image process completed successfully")

if __name__ == "__main__":
    try:
        measure_performance()
    except Exception as e:
        print(f"Unexpected error in filter.py: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
