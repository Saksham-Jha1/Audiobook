import PyPDF2

with open("C:\\Users\\SAKSHI\\OneDrive\\Desktop\\C++\\The Alchemist eBook.pdf",'rb') as file:
    reader = PyPDF2.PdfReader(file)
    num_pages = len(reader.pages)
    print(f"PDF has {num_pages} pages.")

# Loop to allow multiple reads
    while True:
        try:
            page_num = int(input("Enter page number (or -1 to exit): "))
            if page_num == -1:
                break
            elif 0 <= page_num < num_pages:
                page = reader.pages[page_num]
                print("\n" + page.extract_text() + "\n")
            else:
                print("Invalid page number.")
        except ValueError:
            print("Please enter a valid number.")
