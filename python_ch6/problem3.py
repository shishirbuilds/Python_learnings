p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe now"
p5 = "Send me the otp"

msg = input("Enter your message: ")

if(p1 in msg or p2 in msg or p3 in msg or p5 in msg ):
    print("Spam msg")
    
else :
    print("valid msg")