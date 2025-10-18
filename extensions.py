mime_types = {
    ".gif": "image/gif",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".pdf": "application/pdf",
    ".txt": "text/plain",
    ".zip": "application/zip"
}

filename = input("Enter the filename: ").strip().lower()
for ext, mime in mime_types.items():
    if filename.endswith(ext):
        print(mime)
        break
else:
    print("application/octet-stream")
