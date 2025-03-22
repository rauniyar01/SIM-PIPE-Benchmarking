import cv2
import time
import psutil
import os
import sys

def measure_performance():
    print("Starting rotate image process")
    process = psutil.Process()
    start_time = time.time()
    start_cpu_times = process.cpu_times()
    
    # Check if input directory exists and list its contents
    input_path = '/in/filtered_image.jpg'
    output_path = '/out/rotated_image.jpg'
    
    print(f"Current working directory: {os.getcwd()}")
    print(f"Listing directories:")
    print(f"Root directory: {os.listdir('/')}")
    print(f"Input directory: {os.listdir('/in') if os.path.exists('/in') else 'Directory not found'}")
    print(f"Output directory: {os.listdir('/out') if os.path.exists('/out') else 'Directory not found'}")
    
    # Check if input file exists
    print(f"Checking if input file exists at: {input_path}")
    if not os.path.exists(input_path):
        print(f"Error: Input file not found at {input_path}")
        sys.exit(1)
    
    # Perform rotation
    print(f"Loading image from {input_path}")
    img = cv2.imread(input_path)
    if img is None:
        print(f"Error: Could not load image at {input_path}")
        print(f"File exists: {os.path.exists(input_path)}")
        print(f"File size: {os.path.getsize(input_path) if os.path.exists(input_path) else 'N/A'}")
        sys.exit(1)
    
    print(f"Image loaded successfully, shape: {img.shape}")
    print("Rotating image 90 degrees clockwise")
    rotated_img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    
    print(f"Writing rotated image to {output_path}")
    success = cv2.imwrite(output_path, rotated_img)
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
    
    performance_path = '/out/performance_rotate.txt'
    print(f"Writing performance metrics to {performance_path}")
    with open(performance_path, 'w') as f:
        f.write(f"Duration: {duration} seconds\n")
        f.write(f"CPU Usage: {cpu_usage_percentage} %\n")
        f.write(f"Memory Usage: {memory_usage} MB\n")
    
    print("Rotate image process completed successfully")

if __name__ == "__main__":
    try:
        measure_performance()
    except Exception as e:
        print(f"Unexpected error in rotate.py: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
