import paho.mqtt.client as mqtt
from config import BROKER, PORT, TOPIC
import time

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
            time.sleep(2)
    return False

#Dữ liệu được download
def subscriber():
    def on_message(client, userdata, msg):
        print(f"Received: {msg.payload.decode()}")

    client = mqtt.Client("Subscriber")
    client.on_message = on_message

    if not connect_mqtt(client):
        print("Không thể kết nối MQTT, dừng tiến trình.")
        return

    client.subscribe(TOPIC)
    client.loop_forever()


if __name__ == "__main__":
    subscriber()