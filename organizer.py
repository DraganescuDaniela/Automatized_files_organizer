import os
import shutil
from datetime import datetime

reguli = {
    ".pdf": "PDF_Files",
    ".jpg": "Images",
    ".png": "Images",
    ".docx": "Word_Documents",
    ".txt": "Text_Files",
}

def organizare_fisiere(folder_test, folder_dest, fisier_mesaje):

    os.makedirs(folder_dest, exist_ok=True)

    lista = os.listdir(folder_test)

    for i in lista:
        cale_initiala = os.path.join(folder_test, i)

        # ignorăm folderele deja organizate
        if not os.path.isfile(cale_initiala):
            continue

        try:
            extensie = os.path.splitext(i)[1]
            nume_folder = reguli.get(extensie, "Others")

            cale_finala_folder = os.path.join(folder_dest, nume_folder)
            os.makedirs(cale_finala_folder, exist_ok=True)

            destinatie_finala = os.path.join(cale_finala_folder, i)

            # evită overwrite
            if os.path.exists(destinatie_finala):
                base, ext = os.path.splitext(i)
                destinatie_finala = os.path.join(
                    cale_finala_folder,
                    f"{base}_copy{ext}"
                )

            shutil.move(cale_initiala, destinatie_finala)

            with open(fisier_mesaje, "a", encoding="utf-8") as log_file:
                log_file.write(
                    f"{datetime.now()}: Moved {i} -> {nume_folder}\n"
                )

        except Exception as e:
            with open(fisier_mesaje, "a", encoding="utf-8") as log_file:
                log_file.write(
                    f"{datetime.now()}: ERROR with {i} -> {e}\n"
                )


# PATH-uri
folder_t = r"C:\Users\Lenovo\Desktop\python-document-automation\test_folder"
folder_dest = r"C:\Users\Lenovo\Desktop\python-document-automation\organized"
mesaj = r"C:\Users\Lenovo\Desktop\python-document-automation\log.txt"

organizare_fisiere(folder_t, folder_dest, mesaj)