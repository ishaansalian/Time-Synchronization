import socket
import csv
import time

# Server Configuration
HOST = "0.0.0.0"  # Listen on all interfaces
PORT = 8888
RESET_THRESHOLD = 0.1  # Max allowable time difference in seconds

# Data Storage
CSV_FILE = "sync_data.csv"
HEADER = ["pi_time_of_receipt_esp1", "esp1_sensor_data", "pi_time_of_receipt_esp2", "esp2_sensor_data", "time_difference"]

# Drift Monitoring
DRIFT_WINDOW = 10  # Number of recent samples to calculate drift
recent_differences = []

def write_delay_to_csv(deviceID, timestamp_sent, timestamp_received):
    """Logs network delay data into a CSV file."""
    filename = "network_delay.csv"
    delay = (timestamp_received - timestamp_sent) / 2.0

    # Create the file with headers if it doesn't exist
    try:
        with open(filename, 'r') as f:
            pass
    except FileNotFoundError:
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Device ID", "Timestamp Sent", "Timestamp Received", "Delay"])

    # Append delay data to the CSV file
    with open(filename, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([deviceID, timestamp_sent, timestamp_received, delay])

    print("Delay has been recorded.")

def log_data(pi_time_esp1, esp1_data, pi_time_esp2, esp2_data, diff):
    """Logs synchronization data into a CSV file."""
    with open(CSV_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([pi_time_esp1, esp1_data, pi_time_esp2, esp2_data, diff])

def calculate_drift():
    """Calculate drift trends from recent differences."""
    if len(recent_differences) < 2:
        return 0  # Not enough data to calculate drift

    drift_rate = (recent_differences[-1]["time_diff"] - recent_differences[0]["time_diff"]) / (
        recent_differences[-1]["pi_time"] - recent_differences[0]["pi_time"]
    )
    return drift_rate

def main():
    # Initialize UDP server
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((HOST, PORT))
    message = b"hi"

    # Initialize Data Log
    with open(CSV_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(HEADER)

    print("Raspberry Pi is running and listening...")

    # Variables to track state
    esp1_data, esp2_data = None, None
    pi_time_esp1, pi_time_esp2 = None, None
    reset_sent = False
    first_connection = True
    addr_dict = {}
    timestamp_sent = None
    target1 = "192.168.137.151"
    target2 = "192.168.137.210"

    while True:
        try:
            # Initial Handshake
            if first_connection:
                first_connection = False
                print("Devices are connected. Sending initial handshake command.")

                for _ in range(2):
                    print("Sending hi")
                    server.sendto(message, (target1, 8888))
                    server.sendto(message, (target2, 8888))
                timestamp_sent = time.time()

            # Receive Data
            data, addr = server.recvfrom(1024)
            decoded_data = data.decode("utf-8")
            print(f"Received: {decoded_data} from {addr}")

            # Parse Data
            try:
                device, sensor_data = decoded_data.split(", ")
                sensor_data = int(sensor_data.strip())
            except ValueError:
                print("Invalid data format received.")
                continue

            # Assign data based on device ID
            if device == "esp_1" and sensor_data == 9999:
                addr_dict["esp_1"] = addr
                write_delay_to_csv("esp1", timestamp_sent, time.time())
            elif device == "esp_2" and sensor_data == 9999:
                addr_dict["esp_2"] = addr
                write_delay_to_csv("esp2", timestamp_sent, time.time())
            elif device == "esp_1":
                esp1_data = sensor_data
                pi_time_esp1 = time.time()
                addr_dict["esp_1"] = addr
            elif device == "esp_2":
                esp2_data = sensor_data
                pi_time_esp2 = time.time()
                addr_dict["esp_2"] = addr
            else:
                print("Unknown device identifier.")
                continue

            # Reset handshake flag
            handshake = False

            # Check if both timestamps are available
            if pi_time_esp1 and pi_time_esp2:
                if reset_sent:
                    write_delay_to_csv("reset delay record", timestamp_sent, time.time())
                    reset_sent = False

                time_diff = abs(pi_time_esp1 - pi_time_esp2)

                # Log the Data
                log_data(pi_time_esp1, esp1_data, pi_time_esp2, esp2_data, time_diff)

                # Store time difference for drift calculation
                recent_differences.append({"pi_time": time.time(), "time_diff": time_diff})

                # Maintain a window of recent data
                if len(recent_differences) > DRIFT_WINDOW:
                    recent_differences.pop(0)

                # Calculate Drift
                drift_rate = calculate_drift()
                print(f"Current Drift Rate: {drift_rate} seconds/second")

                # Check Synchronization
                print(f"Time difference: {time_diff} seconds")

                if time_diff > RESET_THRESHOLD and not reset_sent:
                    print("Devices are out of sync. Sending reset command.")
                    timestamp_sent = time.time()
                    for device, device_addr in addr_dict.items():
                        print(f"Sending reset to {device} at {device_addr}")
                        server.sendto(b"reset", device_addr)
                    reset_sent = True

                # Reset timestamps after processing
                pi_time_esp1, pi_time_esp2 = None, None

        except KeyboardInterrupt:
            print("Exiting...")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
