import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import fitz  # PyMuPDF kütüphanesi

# Ana uygulama penceresini oluştur
uygulama = tk.Tk()
uygulama.title("Pdf to Png")

# Ekranın tam ortasında görüntüle
pencere_genislik = 250
pencere_yukseklik = 55

ekran_genislik = uygulama.winfo_screenwidth()
ekran_yukseklik = uygulama.winfo_screenheight()

x_pozisyon = (ekran_genislik - pencere_genislik) // 2
y_pozisyon = (ekran_yukseklik - pencere_yukseklik) // 2

uygulama.geometry(f"{pencere_genislik}x{pencere_yukseklik}+{x_pozisyon}+{y_pozisyon}")

# Dosya seçme işlevi
def dosya_sec():
    dosya_yolu = filedialog.askopenfilename(filetypes=[("PDF Dosyaları", "*.pdf")])
    if dosya_yolu:
        print("Seçilen PDF Dosyası:", dosya_yolu)
        
        # Kullanıcıdan kayıt yeri ve dosya adı bilgilerini al
        kayit_yeri = filedialog.askdirectory()
        dosya_adi = "Sayfa"  # Varsayılan dosya adı (uzantısız)

        if not kayit_yeri:
            messagebox.showerror("Hata", "Geçerli bir kayıt yeri seçilmedi.")
        else:
            pdfden_jpg_kaydet(dosya_yolu, kayit_yeri, dosya_adi)

    else:
        messagebox.showerror("Hata", "Lütfen bir PDF dosyası seçin.")

# PDF dosyasını JPG olarak kaydetme işlevi
def pdfden_jpg_kaydet(pdf_dosya_yolu, kayit_yeri, dosya_adi):
    try:
        # PDF dosyasını açın
        pdf_belgesi = fitz.open(pdf_dosya_yolu)

        # Her sayfayı JPG olarak kaydedin
        for sayfa_no, sayfa in enumerate(pdf_belgesi):
            jpg_dosya_adi = f"{dosya_adi}_{sayfa_no + 1}.png"
            kayit_yolu = f"{kayit_yeri}/{jpg_dosya_adi}"
            pix = sayfa.get_pixmap()
            pix.save(kayit_yolu, "PNG")

        pdf_belgesi.close()

        messagebox.showinfo("Başarılı", "PDF dosyası PNG olarak kaydedildi.")
    except Exception as hata:
        messagebox.showerror("Hata", f"PDF dosyasını PNG olarak kaydederken bir hata oluştu:\n{str(hata)}")

def uygulamayi_kapat():
    uygulama.quit()

# "Dosya Seç" butonunu oluştur
dosya_sec_buton = tk.Button(uygulama, text="Dosya Seç", command=dosya_sec)
dosya_sec_buton.pack()

# "Kapat" butonunu oluştur
kapat_buton = tk.Button(uygulama, text="Kapat", command=uygulamayi_kapat)
kapat_buton.pack()

# Anahtarlamak için uygulama döngüsünü başlat
uygulama.mainloop()
