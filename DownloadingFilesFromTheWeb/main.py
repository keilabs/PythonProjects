from urllib import request

nintendo_url = 'http://real-chart.finance.yahoo.com/table.csv?s=NTDOY&d=6&e=15&f=2016&g=d&a=10&b=18&c=1996&ignore=.csv'

def download_stock_data(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest_url = r'nintendo.csv'
    fx = open(dest_url, 'w')
    for line in lines:
        fx.write(line + "\n")
    fx.close()

download_stock_data(nintendo_url)