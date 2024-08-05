input = input("File name: ").lower().strip()

if '.gif' in input:
    print("image/gif")
elif '.jpg' in input:
    print("image/jpeg")
elif '.jpeg' in input:
    print("image/jpeg")
elif '.png' in input:
    print("image/png")
elif '.pdf' in input:
    print("application/pdf")
elif '.zip' in input:
    print("application/zip")
elif '.txt' in input:
    print("text/plain")
else:
    print("application/octet-stream")