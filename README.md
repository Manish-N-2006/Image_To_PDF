# 🖼️ Image to PDF Converter with Crop, Grayscale & Password Protection

- A Python-based GUI application that allows users to:

- ✅ Select multiple images  
- ✂️ Crop selected regions using mouse  
- 🌑 Convert images to grayscale (optional)  
- 🔐 Export to a password-protected PDF  

- Built using **OpenCV**, **Tkinter**, and **PyPDF2**, this tool is great for automating PDF creation with customization options.

---

## 🛠️ Features

- 📂 Select multiple `.jpg`, `.jpeg`, `.png` images
- ✂️ Crop regions from each image using drag-to-select (OpenCV ROI)
- 🖤 Optional grayscale conversion
- 📄 Save all processed images into a single PDF file
- 🔐 Optionally password-protect the final PDF
- 🪟 User-friendly GUI dialogs (Tkinter)
- ❌ Gracefully handles missing files and exits with warnings

---

## 📌 Tech Stack

- **Python 3.10**
- **OpenCV** – image display and cropping
- **img2pdf** – convert byte images to PDF
- **PyPDF2** – add password encryption
- **Tkinter** – GUI file selection and dialogs

---

## 🚀 How to Run

- python main.py
