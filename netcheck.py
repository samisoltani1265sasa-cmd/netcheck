import requests
import time

TEST_URL = "https://www.google.com"

def check_internet():
    print("در حال تست اتصال اینترنت...")
    start = time.time()
    try:
        r = requests.get(TEST_URL, timeout=5)
        delay = (time.time() - start) * 1000
        if r.status_code == 200:
            print("✅ اینترنت وصله.")
            print(f"⏱ پینگ تقریبی: {delay:.2f} ms")
        else:
            print("⚠ پاسخ غیرمنتظره از سرور.")
    except requests.exceptions.Timeout:
        print("⛔ تایم‌اوت! اینترنت ضعیفه یا قطعه.")
    except requests.exceptions.ConnectionError:
        print("❌ اتصال برقرار نشد.")
    except Exception as e:
        print("⚠ خطای ناشناخته:", e)

if __name__ == "__main__":
    check_internet()
