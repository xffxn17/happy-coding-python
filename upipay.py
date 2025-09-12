import qrcode
import os

# Your UPI ID
upi_id = "9550822676@kotak811"

# Amount to be paid
amount = "100"

# Construct the UPI payment URL
upi_url = f"upi://pay?pa={upi_id}&pn=Receiver&am={amount}&cu=INR"

# Generate the QR code
qr = qrcode.make(upi_url)

# Define folder path
save_path = r"D:\Downloads Volume D"

# Ensure folder exists (optional safeguard)
os.makedirs(save_path, exist_ok=True)

# Full file path
file_path = os.path.join(save_path, "upi_payment_qr.png")

# Save the QR code
qr.save(file_path)

print(f"QR Code generated and saved at: {file_path}")
