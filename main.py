import os
from module.compare import compare_pdf_content
from module.download import download_file
from datetime import datetime,timedelta

# Get the current date
today = datetime.now().date()
# Calculate yesterday's date
yesterday = today - timedelta(days=1)

url = "https://www.sinarmas-am.co.id/uploads/product/simas-saham-unggulan/simas-saham-unggulan-prospectus.pdf"
save_path = f"./file/{today}-simas-saham-unggulan-prospectus.pdf"

download_file(url, save_path)
# Specify the path to the folder
folder_path = './file/'

# Get the list of files in the folder
files = os.listdir(folder_path)

file1_path = f"./file/{files[0]}"
file2_path = f"{save_path}"

compare_pdf_content(file1_path, file2_path)
