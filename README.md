# MQTT Client Testing Suite
Dự án này bao gồm các script Python để kiểm tra kết nối MQTT, gửi/nhận tin nhắn, và đo lường băng thông tải lên của MQTT broker.

### Các thành phần chính

**1. config.py:**

Chứa các thông số cấu hình như địa chỉ broker, port, và topic.


**2. publisher.py:**

Kết nối đến MQTT broker và gửi tin nhắn đến một topic cụ thể.

Hỗ trợ lưu tin nhắn vào file backup nếu không thể kết nối hoặc gửi tin nhắn.


**3. subscriber.py:**

Kết nối đến MQTT broker và đăng ký nhận tin nhắn từ một topic cụ thể.

In ra tin nhắn nhận được từ broker.


**4. testing_bandwidth.py:**

Đo lường băng thông tải lên của MQTT broker bằng cách gửi một số lượng lớn tin nhắn.

Tính toán và hiển thị băng thông (MB/s).


**5. check.py:**

Kiểm tra kết nối Internet và kết nối đến MQTT broker.

Sử dụng socket để kiểm tra kết nối Internet.

Sử dụng thư viện paho-mqtt để kiểm tra kết nối đến MQTT broker.


### Cách sử dụng
**Yêu cầu:**

Python 3.x

**Các thư viện cần thiết:**

```
pip install paho-mqtt
```
**Cấu hình**

Chỉnh sửa file config.py để cập nhật thông tin broker, port, và topic:
```
BROKER = "broker.emqx.io"  # Hoặc "test.mosquitto.org"
PORT = 1883
TOPIC = "test/simple"
```

**Chạy các script**

 <ins>Lưu ý:</ins> Luôn luôn chạy Subcriber trước khi chạy Publisher.

**1.** Gửi tin nhắn (**Publisher**):
```
python publisher.py
```
**2.** Nhận tin nhắn (**Subscriber**):
```
python subscriber.py
```
**3.** Nếu cần kiểm tra kết nối:
```
python check.py
```
**4.** Nếu cần kiểm tra băng thông tải lên:
```
python testing_bandwidth.py
```
Cấu trúc thư mục

```
MQTT-Client-Testing/
│
├── check.py
├── config.py
├── publisher.py
├── subscriber.py
├── testing_bandwidth.py
└── README.md
```
