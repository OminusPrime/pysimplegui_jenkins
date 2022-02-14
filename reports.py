#!/usr/bin/env python3

#This allows you to import the style of the document in this case the pdf
from reportlab.platypus import SimpleDocTemplate

#This allows you to import the styles for each part to the document
from reportlab.platypus import Paragraph, Spacer, Table, Image

#Import a template that contains the style guide for each part of the document
from reportlab.lib.styles import getSampleStyleSheet

#Import a the color Library
from reportlab.lib import colors

#def generate(filename, table_data):
def generate(filename, title, additional_info, table_data):
    style = getSampleStyleSheet()
    report = SimpleDocTemplate(filename)
    report_title = Paragraph(title, style["h1"], )
    report_info = Paragraph(additional_info, style["BodyText"])
    table_style = [('GRID', (0,0), (-1,-1), 1, colors.white),
                   ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
                   ('ALIGN', (0,0), (-1,-1), 'CENTER')]
    report_table = Table(data=table_data, style=table_style, hAlign="LEFT")
    empty_line = Spacer(1,20)
    report.build([report_title, empty_line, report_info, empty_line, report_table])
    #report.build([report_table])
