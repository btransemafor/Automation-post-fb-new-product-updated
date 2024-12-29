# **Facebook Auto-Post Bot**

## **Description**
This project automates the process of posting on Facebook using **Selenium** and **Python**. It fetches product data from WordPress whenever a new product is added, enriches the content with **Gemini API**, and posts the final content to a Facebook page or profile.

---

## **Features**
- Automatically listens for new product additions on WordPress through webhooks.
- Fetches product descriptions and generates enriched content using **Gemini API**.
- Posts content to Facebook profiles or pages using **Selenium**.
- Configurable Facebook login credentials and customizable post formats.

---

## **Technologies Used**
- **Python**: Core programming language.
- **Selenium**: For browser automation.
- **Flask**: To handle WordPress webhooks.
- **Requests**: To interact with Gemini API.
- **WordPress Webhooks**: To trigger automation when a new product is added.

---

## **Prerequisites**
Ensure you have the following installed:
1. **Python**
2. **Google Chrome Browser**
3. **ChromeDriver** (compatible with your browser version)
4. WordPress site with webhook integration enabled.
5. **ngrok**
Install required Python packages:
```bash
pip install selenium requests flask
```

---

## **Usage**

### **1. Start the Flask Server**
Run the Flask server to listen for webhook events from WordPress:
```bash
python autopost.py
```

### **2. New Product Trigger**
Whenever a new product is added to WordPress:
1. WordPress sends a webhook payload to the Flask server.
2. The server fetches content from **Gemini API** using the product name.
3. Selenium opens Facebook and posts the generated content.

### **3. Example Workflow**
1. **Webhook Payload** (from WordPress):
   ```json
   {
       "product_name": "Awesome Product",
       "product_description": "This is a great product!"
   }
   ```
2. **Generated Facebook Post**:
   ```
   🎉 New Product Alert: Awesome Product

   Discover the best product in the market today. It's crafted with care and precision. Don't miss out!

   Buy now: [Your WordPress Store URL]
   ```
---
## **Testing**
1. Add a test product to WordPress and ensure the webhook sends the correct payload to the Flask server.
2. Verify the Facebook post is created with the correct content.

**Link Demo:** https://www.youtube.com/watch?v=yqDteBeSNoo
---


## **Contact**
For questions or support, reach out to me at:
- Email: vongocbaotran754@gmail.com
- GitHub: [btransemafor](https://github.com/btransemafor)

---

