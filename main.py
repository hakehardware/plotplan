import psutil
DRIVE_PATH = "D://"

def get_free_disk_space(device_path):
    try:
        # Get disk usage information for the specified device
        usage = psutil.disk_usage(device_path)

        # Convert free space to gibibytes (GiB)
        free_space_in_gibibytes = usage.free / (1024 ** 3)  # GiB

        return free_space_in_gibibytes
    except Exception as e:
        print(f"Error: {e}")
        return None

# Get the free space on the storage device in GiB
free_space_in_gib = get_free_disk_space(DRIVE_PATH)

if free_space_in_gib is not None:
    print(f"Free space on {DRIVE_PATH}: {free_space_in_gib:.2f} GiB")

    # Calculate how many 64 GiB files can fit in the free space
    file_size_in_gib = 64  # Size of each file in GiB
    files_that_fit = free_space_in_gib // file_size_in_gib

    print(f"You can fit {int(files_that_fit)} SUs free space.")
else:
    print("Failed to retrieve free disk space.")
