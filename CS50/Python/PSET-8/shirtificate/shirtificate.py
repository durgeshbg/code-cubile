from fpdf import FPDF

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
name = input("Enter: ")
pdf.set_font("Helvetica",size=40)
pdf.text(50, 25,"CS50 Shirtificate")
pdf.image("shirtificate.png", x=5, y=55,h=pdf.eph * 0.75)
pdf.set_font(size=25)
pdf.set_text_color(255,255,255)
pdf.text(65, 130, f"{name} took CS50")
pdf.output("shirtificate.pdf")