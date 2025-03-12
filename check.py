import socket
import paho.mqtt.client as mqtt
from config import BROKER, PORT

def check_internet(host="8.8.8.8", port=53, timeout=3):
    #Kiểm tra kết nối Internet bằng cách ping Google DNS
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        print("Kết nối Internet ổn định.\n")
        return True
    except Exception as e:
        print(f"Không có kết nối Internet: {e}\n")
        return False

def check_broker():
    #Kiểm tra kết nối đến MQTT Broker
    client = mqtt.Client()
    try:
        client.connect(BROKER, PORT, 3)  # Timeout 3 giây
        client.disconnect()
        print("MQTT Broker hoạt động bình thường.\n")
        return True
    except Exception as e:
        print(f"Không thể kết nối đến MQTT Broker: {e}\n")
        return False

if __name__ == "__main__":
    print("Kiểm tra kết nối mạng và MQTT Broker...\n")
    internet_status = check_internet()
    broker_status = check_broker()

    if internet_status and broker_status:
        print("Mọi thứ đều hoạt động tốt!")
    elif internet_status:
        print("Internet hoạt động tốt, kiểm tra lại kết nối MQTT")
    else:
        print("Kiểm tra lại hệ thống.")