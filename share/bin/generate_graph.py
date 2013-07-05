import pygal                                                       # First import pygal
import cairosvg
import shutil
import tempfile
import os
import sys
import csv
from pygal.style import Style
from random import randrange
temp = tempfile.mkdtemp()

# # input
# 1 type
# 2 title
# 3 file
# 4 output dir
# 5 file_type
# # output
# png file name

# data loading
csv_reader = csv.reader(open(sys.argv[3]), delimiter=";")

head = []

data = []
colors = []
for row in csv_reader :
  if not head :
    head = row[1:]
  else :
    data.append({"title" :row[0], "data" : row[1:]})
    colors.append("#%s" % "".join(([hex(randrange(0,255))[2:] for i in range(3)])))

custom_style = Style(
  background='white',
  plot_background='white',
  foreground='black',
  foreground_light='blue',
  foreground_dark='black',
  opacity='.6',
  opacity_hover='.9',
  transition='400ms ease-in')


temp_1 = os.path.join(temp, 'result.svg')
bar_chart = pygal.Line(style=custom_style,legend_at_bottom=True)                                            # Then create a bar graph object
bar_chart.title = sys.argv[2]
bar_chart.x_labels = head #map(str, range(2002, 2013))
#bar_chart.add('Fibonacci', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])  # Add some values
#bar_chart.add('Padovan', [1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12])
for row in data :
  final_data = []
  for elem in row["data"] :
    final_data.append(float(elem))
  bar_chart.add(row["title"],final_data)
bar_chart.render_to_file(temp_1)                          # Save the svg to a file

aFile = os.path.join(sys.argv[4],"bar_chart." + sys.argv[5])
sys.stdout.write(aFile)
with open(temp_1, 'rb') as file_object:
    svg_content = file_object.read()
    with open( aFile, 'wb') as file_object:
        # Write to a real file object
        if sys.argv[5] == "pdf" :
          cairosvg.svg2pdf(svg_content, write_to=file_object)
        else :
          cairosvg.svg2png(svg_content, write_to=file_object)
shutil.rmtree(temp)