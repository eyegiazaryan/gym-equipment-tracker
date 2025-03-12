import json
import pandas as pd
import numpy as np
from datetime import datetime
from fpdf import FPDF
from openpyxl import load_workbook
from openpyxl.styles import Font, Alignment
from scrapers.scraper1 import scrape_gym1
from scrapers.scraper2 import scrape_gym2
from scrapers.scraper3 import scrape_gym3
from scrapers.scraper4 import scrape_gym4
from scrapers.scraper5 import scrape_gym5
from scrapers.scraper6 import scrape_gym6
from scrapers.scraper7 import scrape_gym7
from scrapers.scraper8 import scrape_gym8
from scrapers.scraper9 import scrape_gym9
from scrapers.scraper10 import scrape_gym10

def format_excel(filename="gym_data.xlsx"):
    """Format the Excel file for better readability and fix hyperlinks."""
    wb = load_workbook(filename)

    for sheet_name in wb.sheetnames:
        ws = wb[sheet_name]

        # Set column widths for better readability
        column_widths = {"A": 25, "B": 20, "C": 15, "D": 12, "E": 25, "F": 35}
        for col, width in column_widths.items():
            ws.column_dimensions[col].width = width

        # Bold headers and center align
        for cell in ws[1]:
            cell.font = Font(bold=True)
            cell.alignment = Alignment(horizontal="center")

        # Fix hyperlinks
        for row in ws.iter_rows(min_row=2, max_row=ws.max_row):
            if row[5].value and row[5].value != "NA":  # Product Page
                row[5].hyperlink = row[5].value
                row[5].font = Font(color="0000FF", underline="single")

            if row[4].value and row[4].value != "NA":  # Image URL
                row[4].hyperlink = row[4].value
                row[4].font = Font(color="0000FF", underline="single")

    # Save the formatted Excel file
    wb.save(filename)
    print(f"✅ Excel File Formatted & Links Fixed: {filename}")

def save_to_excel(data1, sheet1, data2, sheet2, filename="gym_data.xlsx"):
    """Save scraped data to an Excel file with multiple sheets."""
    writer = pd.ExcelWriter(filename, engine="openpyxl")

    # Convert data to Pandas DataFrame
    df1 = pd.DataFrame(data1)
    df2 = pd.DataFrame(data2)

    # Ensure correct column order
    column_order = ["name", "manufacturer", "price", "country", "image_url", "web_page"]
    df1 = df1[column_order]
    df2 = df2[column_order]

    # Replace None values with 'NA' for consistency
    df1.fillna("NA", inplace=True)
    df2.fillna("NA", inplace=True)

    # Rename Columns for Readability
    df1.columns = ["Product Name", "Manufacturer", "Price", "Country", "Image URL", "Product Page"]
    df2.columns = ["Product Name", "Manufacturer", "Price", "Country", "Image URL", "Product Page"]

    # Write Data to Excel Sheets
    df1.to_excel(writer, sheet_name=sheet1, index=False)
    df2.to_excel(writer, sheet_name=sheet2, index=False)

    # Save the File
    writer.close()
    print(f"✅ Data Saved to: {filename}")

    # Format Excel File to Fix Links
    format_excel(filename)

def safe_text(text):
    """Ensure text is safe for PDF encoding by removing unsupported characters."""
    if pd.isna(text):  # Handle NaN values
        return "NA"
    return str(text).encode("latin-1", "ignore").decode("latin-1")

def generate_pdf(excel_file="gym_data.xlsx", pdf_file="gym_report.pdf"):
    """Generates a PDF report summarizing the gym equipment data."""
    xl = pd.ExcelFile(excel_file)
    report_date = datetime.now().strftime("%B %d, %Y")

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)

    # **Cover Page**
    pdf.add_page()
    pdf.set_font("Arial", style="B", size=24)
    pdf.cell(200, 20, safe_text("🏋️ Gym Equipment Report"), ln=True, align="C")
    pdf.ln(10)

    pdf.set_font("Arial", style="I", size=16)
    pdf.cell(200, 10, safe_text(f"📅 Last Updated: {report_date}"), ln=True, align="C")
    pdf.ln(20)

    pdf.set_font("Arial", size=14)
    pdf.multi_cell(0, 10, safe_text(
        "🔹 This report provides an up-to-date listing of gym equipment, "
        "including squat racks and stands, along with pricing, manufacturer details, and product links.\n\n"
        "🔹 Data is collected from multiple leading gym equipment brands.\n\n"
        "🔹 Clickable product links are provided for quick access.\n\n"
        "📌 For the latest updates, please visit the respective manufacturer websites."
    ))

    pdf.ln(20)
    pdf.set_font("Arial", style="B", size=16)
    pdf.cell(200, 10, safe_text("⬇️ Scroll Down for Full Product Listings"), ln=True, align="C")

    for sheet_name in xl.sheet_names:
        df = xl.parse(sheet_name)
        df = df.replace({np.nan: "NA"})

        pdf.add_page()
        pdf.set_font("Arial", style="B", size=18)
        pdf.cell(200, 10, safe_text(sheet_name), ln=True, align="C")
        pdf.ln(10)

        for _, row in df.iterrows():
            pdf.set_font("Arial", style="B", size=12)
            pdf.cell(0, 10, safe_text(row["Product Name"]), ln=True)

            pdf.set_font("Arial", size=11)
            pdf.cell(0, 8, safe_text(f"💰 Price: {row['Price']}"), ln=True)
            pdf.cell(0, 8, safe_text(f"🏭 Manufacturer: {row['Manufacturer']}"), ln=True)
            pdf.cell(0, 8, safe_text(f"📍 Country: {row['Country']}"), ln=True)

            product_page = row["Product Page"]
            if product_page != "NA" and isinstance(product_page, str):
                pdf.set_text_color(0, 0, 255)
                pdf.cell(0, 8, safe_text(f"🔗 Product Link: {product_page}"), ln=True, link=product_page)
                pdf.set_text_color(0, 0, 0)

            pdf.ln(10)

    pdf.output(pdf_file, "F")
    print(f"✅ PDF Report Generated: {pdf_file}")

def main():
    print("Starting the Gym Scraper...\n")

    squat_racks = [
        scrape_gym1(), scrape_gym2(), scrape_gym3(), scrape_gym4(), scrape_gym5()
    ]
    squat_stands = [
        scrape_gym6(), scrape_gym7(), scrape_gym8(), scrape_gym9(), scrape_gym10()
    ]

    # Save Data to Excel
    save_to_excel(squat_racks, "4x4 Squat Racks", squat_stands, "Squat Stands", "gym_data.xlsx")

    # Generate PDF after scraping
    generate_pdf()

if __name__ == "__main__":
    main()
