import paho.mqtt.client as mqtt
import time
import datetime
import os
from config import BROKER, PORT, TOPIC

    #Kết nối tới broker
def connect_mqtt(client, max_retries=5):
    retries = 0
    while retries < max_retries:
        try:
            client.connect(BROKER, PORT, 60)
            print("Kết nối thành công")
            return True
        except Exception as e:
            print(f"Kết nối thất bại ({retries + 1}/{max_retries}): {e}")
            retries += 1
            time.sleep(1)
    return False

    #Save file backup
def save_backup(message, backup_path):
        # Đảm bảo thư mục backup tồn tại
    os.makedirs(os.path.dirname(backup_path), exist_ok=True)
        # Lấy thời gian hiện tại
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Ghi dữ liệu vào file với timestamp
    with open(backup_path, "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] {message}\n")
    print(f"Dữ liệu đã được lưu vào {backup_path} lúc: {timestamp} ")

    #Dữ liệu upload
def publisher():
    client = mqtt.Client("Publisher")
    backup_path = r"C:\Users\trand\PycharmProjects\MQTT\Backup_Data.txt"  # Đường dẫn cụ thể
    message = f"Test message {1}"   #Data message

    if not connect_mqtt(client):
        print("Không thể kết nối MQTT, dừng tiến trình.")
        save_backup(message, backup_path)  # Lưu vào backup nếu không thể kết nối
        return

    client.loop_start()
    time.sleep(2)
    retries = 0
    sent = False

    while retries < 5 and not sent:
        try:
            result = client.publish(TOPIC, message)
            if result.rc == mqtt.MQTT_ERR_SUCCESS:
                print(f"Published: {message}")
                sent = True
            else:
                raise Exception("Lỗi khi gửi tin nhắn")
        except Exception as e:
            print(f"Gửi thất bại ({retries + 1}/5): {e}")
            retries += 1
            time.sleep(1)

    if not sent:
        print(f"Không thể gửi: {message}. Lưu vào backup.")
        save_backup(message, backup_path)

    client.loop_stop()
    client.disconnect()


if __name__ == "__main__":
    publisher()
