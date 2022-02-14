
#!/usr/bin/env python3

import emails
import os
import reports
import PySimpleGUI 

table_data=[
  ['Name', 'Amount', 'Value'],
  ['elderberries', 10, 0.45],
  ['figs', 5, 3],
  ['apples', 4, 2.75],
  ['durians', 1, 25],
  ['bananas', 5, 1.99],
  ['cherries', 23, 5.80],
  ['grapes', 13, 2.48]]

info = ['The Mercedes-Benz E-Class (2009) generated the most revenue: $22749529.02','The Acura Integra (1995) had the most sales: 1192','The most popular year was 2007 with 21534 sales.']
info = str(info)[1:-1]

info = info.replace(',',"<br/>\n")
info = info.replace("'", "")
print(info)

reports.generate("report.pdf", "A Complete Inventory of My Fruit", info, table_data)

# sender = "sender@example.com"
# receiver = "{}@example.com".format(os.environ.get('USER'))
# subject = "List of Fruits"
# body = "Hi\n\nI'm sending an attachment with all my fruit."
#
# message = emails.generate(sender, receiver, subject, body, "/tmp/report.pdf")
# emails.send(message)
