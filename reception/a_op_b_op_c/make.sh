python math_work.py
moban -td ../../templates -e jj2=jinja2_time.TimeExtension -d name=$1 -c data.yml -t math_sheet.html.jj2 -o tmp.html > /dev/null
weasyprint tmp.html math-sheet.pdf
echo 'math-sheet.pdf is generated'
