from flask import Flask, request, jsonify
import google.generativeai as genai
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    # Kiểm tra Content-Type
    if request.headers.get('Content-Type') != 'application/json':
        return "Unsupported Media Type", 415

    # Lấy dữ liệu JSON
    data = request.json
    print("Webhook data received:", data)

    # Kiểm tra các trường thông tin có trong request hay không
    required_fields = ['name', 'price', 'regular_price']
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400

    # Trích xuất thông tin từ dữ liệu JSON
    product_name = data["name"]
    current_price = data["price"]
    original_price = data["regular_price"]

    time.sleep(1)
    # Tạo prompt gửi đến AI
    genai.configure(api_key="AIzaSyBmkPvgG7grKcHsNVUUsqPZSmpA_31goqo")
    model = genai.GenerativeModel("gemini-1.5-flash")

    response = model.generate_content(f"""
    Viết bài quảng cáo sản phẩm mới.
    Tên sản phẩm: {product_name}
    Giá gốc: {original_price} VND
    Giá khuyến mãi: {current_price} VND
    Thông tin liên hệ (sdt: 033849849 WEBSITE: omgnice.id.vn) thì để đơn giản nha. 
    Hãy viết bài thật hấp dẫn và chuyên nghiệp. Đừng THÊM ICON DÔ NHA tại chrome nó ko biết . Không chú thích gì hết. Một bài hoàn chỉnh luôn. ko cần hình ảnhảnh
    """)
    generated_content = response.text.strip()  


     # Loại bỏ dấu * trong đoạn văn
    main_content = generated_content.replace('*', '')
    print("Generated content:", main_content)  
    
    time.sleep(10)
    chrome_driver_path = r"D:\UIT - Courses\EC312 - Design System\project\chromedriver\chromedriver.exe"

    service = Service(chrome_driver_path)
    options = Options()

    # Tắt thông báo cấp quyền
    prefs = {
        "profile.default_content_setting_values.notifications": 2  # 2 là chặn thông báo
    }
    options.add_experimental_option("prefs", prefs)

    # Khởi tạo WebDriver
    driver = webdriver.Chrome(service=service, options=options)

    try:
        # Mở trang Facebook
        driver.get('https://www.facebook.com')
                
        # Đặt kích thước cửa sổ là 1024x768
        driver.set_window_size(1024, 768)

        # Đợi và nhập email
        email = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="email"]'))
        )
        email.send_keys('0338498306')

        # Đọc mật khẩu từ tệp
        with open('password.txt', 'r') as myfile:
            password1 = myfile.read().strip()

        # Đợi mật khẩu
        password = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="pass"]'))
        )
        password.send_keys(password1)

        # Nhan nut dang nhap 
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "login"))
        )
        login_button.click()

        # Đợi và click vào phần tử trang cá nhân
        profile_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[name()='svg' and @aria-label='Trang cá nhân của bạn']"))
        )
        profile_button.click()

        # Đợi và click vào phần tử "Chuyển sang OmgNice" 
        omg_nice_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Chuyển sang OmgNice']"))
        )
        omg_nice_button.click()

        # Đợi và click vào phần tử có văn bản "OmgNice ơi, bạn đang nghĩ gì thế?"
        post_box = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'OmgNice ơi, bạn đang nghĩ gì thế?')]"))
        )
        post_box.click()
        
        # Wait for the button to be clickable and click it
        but_opt = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".xr9ek0c:nth-child(6) .x1b0d499:nth-child(1)"))
        )
        but_opt.click()

        # Wait for the message button to be clickable and click it
        but_mess = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[9]/div/div/div/div/div[2]/div/div/div/div/span"))
        )
        but_mess.click()
        editable_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[contenteditable='true']")) )
        
        editable_element.send_keys(main_content)
        
        # Đợi và click vào nút đăng
        post_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Đăng']"))
        )
        post_button.click()
        # Chờ thêm để xác minh bài viết đã được đăng
        time.sleep(10)  
        
        # Sau khi thực hiện, trả về kết quả
        return jsonify({"status": "success", "message": "Post successfully made!"})
    except Exception as e:
        print(f"Lỗi xảy ra: {str(e)}")
        return jsonify({"error": "An error occurred during the process", "details": str(e)}), 500

    finally:
        try:
            driver.quit()
        except:
            pass

if __name__ == '__main__':
    app.run(port=5000)
