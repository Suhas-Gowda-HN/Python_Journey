signal = input("What is the signal: ")
signal.lower()

if signal=="red":
    print("STOP")
elif(signal=="yellow"):
    print("READY")
else:
    print("GO")