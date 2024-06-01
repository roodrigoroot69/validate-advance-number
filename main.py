from phones import check_number

phone_numbers = [
"+1 (234) 567-8901",
"+44 123 456 7890",
"+91-9876543210",
"+86 10 12345678",
"123-456-7890",
"+49 (0) 30 1234567"
]

print(check_number(phone_numbers))

# Final Result
# ['+12345678901', '+441234567890', '+919876543210', 'Invalid', 'Invalid', '+490301234567']
