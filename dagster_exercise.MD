## 1. Tạo một dagster project tên hello_worlds

yêu cầu: dùng uv để tạo venv với python 3.10
bắt buộc: Dagster, Dagster-webserver

uv code để tạo template project:
```bash
uvx create-dagster@latest project project_name
```

Dùng:
```bash
uv add pandas numpy ....
```
để install các thư viện và lưu lại vào file uv.lock (thuận tiện để uv sync)

### 1.1 Tạo một pipeline gồm 2 asset: hello, worlds

cấu trúc:

	[hello] -> [worlds]

### 1.2: set lịch auto cho nó chạy vào lúc 6h sáng hàng ngày

### 1.3 dùng ntfy để thông báo tool chạy thành công/hoặc bị lỗi
- gửi thông báo tới: ntfy.sh/dagster_hello_worlds
- docs để tự tìm hiểu: https://docs.ntfy.sh/#__tabbed_1_6

