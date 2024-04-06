from module.compare import compare_pdf_content
from module.download import download_file
from datetime import datetime,timedelta

# Get the current date
today = datetime.now().date()
# Calculate yesterday's date
yesterday = today - timedelta(days=1)

url = "https://www.sinarmas-am.co.id/uploads/product/simas-saham-unggulan/simas-saham-unggulan-prospectus.pdf"
save_path = f"./file/{today}.pdf"

download_file(url, save_path)

file1_path = f"./file/{yesterday}.pdf"
file2_path = f"./file/{today}.pdf"

compare_pdf_content(file1_path, file2_path)
