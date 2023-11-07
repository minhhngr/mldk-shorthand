import smtplib
import ssl

# Thay thế các giá trị sau đây bằng thông tin của bạn
smtp_server = ""
smtp_port = 465  # Cổng SMTP phù hợp với máy chủ của bạn (thông thường là 465 cho SSL)
smtp_username = ""
smtp_password = ""


# Địa chỉ email bạn muốn kiểm tra
email_to_verify = ""

# Tạo kết nối SMTP bằng SSL
context = ssl.create_default_context()
server = smtplib.SMTP_SSL(smtp_server, smtp_port, context=context)

# Đăng nhập (nếu cần)
server.login(smtp_username, smtp_password)

try:
    response = server.verify(email_to_verify)
    # muon hien thong bao tra ve o day
    if response == (250, "2.1.5 User known"):
        print(f"The email address {email_to_verify} is valid.")
    else:
        # muon hien thong bao tra ve o day
        print(f"The email address {email_to_verify} is not valid.")
except smtplib.SMTPServerDisconnected:
    print("Unable to verify email address. The SMTP server may not support VRFY.")
except smtplib.SMTPException as e:
    print(f"An error occurred: {e}")
finally:
    # Đóng kết nối SMTP
    server.quit()
