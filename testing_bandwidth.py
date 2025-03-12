import time
import paho.mqtt.client as mqtt
from config import BROKER, PORT, TOPIC

# Kích thước tin nhắn (bytes)
MESSAGE_SIZE = 1024  # 1KB
# Số lượng tin nhắn sẽ gửi
NUM_MESSAGES = 1000

# Tạo một tin nhắn có kích thước cố định
def create_message(size):
    return 'x' * size

# Hàm kiểm tra băng thông tải lên
def test_upload_bandwidth():
    # Tạo MQTT client
    client = mqtt.Client()

    # Kết nối đến broker
    client.connect(BROKER, PORT, 60)
    print(f"Connected to MQTT Broker: {BROKER}:{PORT}")

    # Tạo tin nhắn
    message = create_message(MESSAGE_SIZE)

    # Bắt đầu đo thời gian
    start_time = time.time()

    # Gửi tin nhắn
    for i in range(NUM_MESSAGES):
        client.publish(TOPIC, message)
        if (i + 1) % 100 == 0:
            print(f"Sent {i + 1} messages")

    # Kết thúc đo thời gian
    end_time = time.time()

    # Ngắt kết nối
    client.disconnect()

    # Tính toán băng thông
    total_time = end_time - start_time
    total_data_sent = NUM_MESSAGES * MESSAGE_SIZE  # Tổng dữ liệu gửi (bytes)
    bandwidth = (total_data_sent / total_time) / (1024 * 1024)  # Băng thông (MB/s)

    print(f"Total messages sent: {NUM_MESSAGES}")
    print(f"Total data sent: {total_data_sent / (1024 * 1024):.2f} MB")
    print(f"Total time: {total_time:.2f} seconds")
    print(f"Upload bandwidth: {bandwidth:.2f} MB/s")

if __name__ == "__main__":
    test_upload_bandwidth()