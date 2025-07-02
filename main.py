import img2pdf
import cv2
from tkinter import Tk,filedialog,messagebox
import tkinter as tk
import tkinter.simpledialog
from PyPDF2 import PdfReader,PdfWriter

root = tk.Tk()
root.withdraw()
final_img_byte=[]


def crop(r):
        choice= messagebox.askyesno("Crop","Do you wanna crop ?")
        if choice:
            global byte
            byte=1
            sel=cv2.selectROI("Crop the image",r,fromCenter=False,showCrosshair=True)
            x,y,w,h = sel

            crop=r[int(y):int(y+h),int(x):int(x+w)]
            cv2.imshow("Cropped Image",crop)
            cv2.waitKey(1)            
            
            process, encode_img = cv2.imencode(".jpg",crop)
            
            if process:
                final_img_byte.append(encode_img.tobytes())
            return (crop)
        
        else:
            process, encode_img = cv2.imencode(".jpg", r)
            if process:
                  final_img_byte.append(encode_img.tobytes())
            return r

def color(r):
        choice= messagebox.askyesno("Change Color","Do you wanna change color to grayscale ?")
        
        if choice:
               r=cv2.cvtColor(r,cv2.COLOR_BGR2GRAY)

               cv2.imshow("Grayscale image",r)
               cv2.waitKey(1) 

               process, encode_img = cv2.imencode(".jpg",r)
               if process:
                final_img_byte.append(encode_img.tobytes())
             
                
        cv2.imshow("Image",r)
        cv2.waitKey(5)
        return r
        
            
def password(save_path):
      choice= messagebox.askyesno("Password","Do you wanna Add Password to the File ?")

      if choice:
            password = None
            while not password:
                  password = tkinter.simpledialog.askstring("PDF Password","Enter the PDF Password !!",show='*')
                  if password is None:
                        exit()
            
            try:
                  reader = PdfReader(save_path)
                  writer = PdfWriter()

                  for pg in reader.pages:
                        writer.add_page(pg)
                    
                  writer.encrypt(password)                

                  with open(save_path,"wb") as f:
                        writer.write(f)
               
                  messagebox.showinfo("Success","Successfully Converted image to PDF and Encryted :)")
            
            except Exception as e:
                  messagebox.showerror("Failure","Encrytion Failed :(")
      else:
            messagebox.showinfo("Success","Successfully Converted image to PDF and Without Encryted :)")


def convert_pdf():

    file_path = filedialog.askopenfilenames(title="Select image(s)",
                filetypes=[("Image File",("*.jpg","*.jpeg","*.png"))]) 
    
    if not file_path:
         messagebox.showwarning("No Files","No Images were selected :( ")
    
    file_path=sorted(file_path)

    save_path = filedialog.asksaveasfilename(title="Save PDF as",
                filetypes=[("PDF File","*.pdf")],defaultextension=".pdf")
    if not save_path:
          messagebox.showwarning("No Destination","No Save Location Selected :( ")  

    for img in file_path:
          r = cv2.imread(img, 1)
          if r is None:
                messagebox.showerror("Image Error", f"Could not read image:\n{img}")
                continue

          cv2.imshow("Images", r)
          cropped_image = crop(r)
          color(cropped_image)
          cv2.destroyAllWindows()        
            
          key = cv2.waitKey(0)
          if key==27:
            break

    if final_img_byte:
            try:
                with open(save_path,'wb') as f:
                    f.write(img2pdf.convert(final_img_byte))
                    messagebox.showinfo("Success","Successfully Converted image to PDF and Saved :)")
            
                password(save_path)

            except Exception as e:
                    messagebox.showerror("Convertion Failed",str(e))

    else:
          messagebox.showerror("Empty PDF :(","No Image is added to list")

            
    cv2.destroyAllWindows()

convert_pdf()
