import csv
import time

from flask import Flask
import alphavantage

app = Flask(__name__)

symbol_list = ["APLE", "IBM", "META", "DDD", "XMTR"]

row_data = []

# Initial data population to prevent errors
for i in range(0, len(symbol_list)):
    symbol = alphavantage.time_series_intraday(symbol_list[i])
    symbol_csv = 'symbol_csv_dir/intraday_{}.csv'.format(symbol_list[i])
    with open(symbol_csv, 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        row_data = []
        for j in symbol.get('Time Series (5min)'):
            row_data.append([j, symbol['Time Series (5min)'][j].get('1. open'),
                             symbol['Time Series (5min)'][j].get('2. high'),
                             symbol['Time Series (5min)'][j].get('3. low'),
                             symbol['Time Series (5min)'][j].get('4. close'),
                             symbol['Time Series (5min)'][j].get('5. volume')])
        csv_writer.writerows(row_data)
        csv_file.close()
        time.sleep(12)


# Routing
@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/update', methods=['GET'])
def update_stocks():
    global symbol_list
    global row_data
    time.sleep(20)
    count = 0
    with open('count.txt', 'r') as f:
        for line in f:
            count = int(line.strip())
    f.close()
    print("count: {}".format(count))
    ret_sym = symbol_list[count]
    row_data = []

    symbol = alphavantage.time_series_intraday(symbol_list[count])
    symbol_csv = 'symbol_csv_dir/intraday_{}.csv'.format(symbol_list[count])
    with open(symbol_csv, 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        row_data = []
        for j in symbol.get('Time Series (5min)'):
            row_data.append([j, symbol['Time Series (5min)'][j].get('1. open'),
                             symbol['Time Series (5min)'][j].get('2. high'),
                             symbol['Time Series (5min)'][j].get('3. low'),
                             symbol['Time Series (5min)'][j].get('4. close'),
                             symbol['Time Series (5min)'][j].get('5. volume')])
        csv_writer.writerows(row_data)
        csv_file.close()
    if count >= (len(symbol_list) - 1):
        with open('count.txt', 'w') as f:
            f.write(str(0))
        f.close()
    else:
        with open('count.txt', 'w') as f:
            f.write(str(count + 1))
        f.close()

    return ret_sym


@app.route('/Date', methods=['GET'])
def date_date():
    data = []
    count = 0
    with open('count.txt', 'r') as f:
        for line in f:
            count = int(line.strip())
    f.close()
    if count == 0:
        count = len(symbol_list) - 1
    else:
        count -= 1
    symbol_csv = 'symbol_csv_dir/intraday_{}.csv'.format(symbol_list[count])
    with open(symbol_csv) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            data.append(row)
    stock_date, stock_time = str(data[0][0]).split(" ")
    form_string = "Date: {}".format(stock_date)
    return form_string


@app.route('/Time', methods=['GET'])
def date_time():
    data = []
    count = 0
    with open('count.txt', 'r') as f:
        for line in f:
            count = int(line.strip())
    f.close()
    if count == 0:
        count = len(symbol_list) - 1
    else:
        count -= 1
    symbol_csv = 'symbol_csv_dir/intraday_{}.csv'.format(symbol_list[count])
    with open(symbol_csv) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            data.append(row)
    stock_date, stock_time = str(data[0][0]).split(" ")
    form_string = "Time: {}".format(stock_time)
    return form_string


@app.route('/Open', methods=['GET'])
def stock_open():
    data = []
    count = 0
    with open('count.txt', 'r') as f:
        for line in f:
            count = int(line.strip())
    f.close()
    if count == 0:
        count = len(symbol_list) - 1
    else:
        count -= 1
    symbol_csv = 'symbol_csv_dir/intraday_{}.csv'.format(symbol_list[count])
    with open(symbol_csv) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            data.append(row)
    stock_open = str(data[0][1])
    form_string = "Open: {}".format(stock_open)
    return form_string


@app.route('/High', methods=['GET'])
def stock_high():
    data = []
    count = 0
    with open('count.txt', 'r') as f:
        for line in f:
            count = int(line.strip())
    f.close()
    if count == 0:
        count = len(symbol_list) - 1
    else:
        count -= 1
    symbol_csv = 'symbol_csv_dir/intraday_{}.csv'.format(symbol_list[count])
    with open(symbol_csv) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            data.append(row)
    stock_high = str(data[0][2])
    form_string = "High: {}".format(stock_high)
    return form_string


@app.route('/Low', methods=['GET'])
def stock_low():
    data = []
    count = 0
    with open('count.txt', 'r') as f:
        for line in f:
            count = int(line.strip())
    f.close()
    if count == 0:
        count = len(symbol_list) - 1
    else:
        count -= 1
    symbol_csv = 'symbol_csv_dir/intraday_{}.csv'.format(symbol_list[count])
    with open(symbol_csv) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            data.append(row)
    stock_low = str(data[0][3])
    form_string = "Low: {}".format(stock_low)
    return form_string


@app.route('/Close', methods=['GET'])
def stock_close():
    data = []
    count = 0
    with open('count.txt', 'r') as f:
        for line in f:
            count = int(line.strip())
    f.close()
    if count == 0:
        count = len(symbol_list) - 1
    else:
        count -= 1
    symbol_csv = 'symbol_csv_dir/intraday_{}.csv'.format(symbol_list[count])
    with open(symbol_csv) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            data.append(row)
    stock_close = str(data[0][4])
    form_string = "Close: {}".format(stock_close)
    return form_string


@app.route('/Volume', methods=['GET'])
def stock_volume():
    data = []
    count = 0
    with open('count.txt', 'r') as f:
        for line in f:
            count = int(line.strip())
    f.close()
    if count == 0:
        count = len(symbol_list) - 1
    else:
        count -= 1
    symbol_csv = 'symbol_csv_dir/intraday_{}.csv'.format(symbol_list[count])
    with open(symbol_csv) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            data.append(row)
    stock_volume = str(data[0][5])
    form_string = "Volume: {}".format(stock_volume)
    return form_string


@app.route('/UpDownOpen', methods=['GET'])
def up_down_open():
    data = []
    count = 0
    with open('count.txt', 'r') as f:
        for line in f:
            count = int(line.strip())
    f.close()
    if count == 0:
        count = len(symbol_list) - 1
    else:
        count -= 1
    symbol_csv = 'symbol_csv_dir/intraday_{}.csv'.format(symbol_list[count])
    with open(symbol_csv) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            data.append(row)
    stock_open0 = str(data[0][1])
    stock_open1 = str(data[2][1])
    stock_diff = 0
    if stock_open0 >= stock_open1:
        stock_diff = 1
    else:
        stock_diff = 0

    form_string = str(stock_diff)
    return form_string


@app.route('/UpDownHigh', methods=['GET'])
def up_down_high():
    data = []
    count = 0
    with open('count.txt', 'r') as f:
        for line in f:
            count = int(line.strip())
    f.close()
    if count == 0:
        count = len(symbol_list) - 1
    else:
        count -= 1
    symbol_csv = 'symbol_csv_dir/intraday_{}.csv'.format(symbol_list[count])
    with open(symbol_csv) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            data.append(row)
    stock_open0 = str(data[0][2])
    stock_open1 = str(data[2][2])
    stock_diff = 0
    if stock_open0 >= stock_open1:
        stock_diff = 1
    else:
        stock_diff = 0

    form_string = str(stock_diff)
    return form_string

@app.route('/UpDownLow', methods=['GET'])
def up_down_low():
    data = []
    count = 0
    with open('count.txt', 'r') as f:
        for line in f:
            count = int(line.strip())
    f.close()
    if count == 0:
        count = len(symbol_list) - 1
    else:
        count -= 1
    symbol_csv = 'symbol_csv_dir/intraday_{}.csv'.format(symbol_list[count])
    with open(symbol_csv) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            data.append(row)
    stock_open0 = str(data[0][3])
    stock_open1 = str(data[2][3])
    stock_diff = 0
    if stock_open0 >= stock_open1:
        stock_diff = 1
    else:
        stock_diff = 0

    form_string = str(stock_diff)
    return form_string

@app.route('/UpDownClose', methods=['GET'])
def up_down_close():
    data = []
    count = 0
    with open('count.txt', 'r') as f:
        for line in f:
            count = int(line.strip())
    f.close()
    if count == 0:
        count = len(symbol_list) - 1
    else:
        count -= 1
    symbol_csv = 'symbol_csv_dir/intraday_{}.csv'.format(symbol_list[count])
    with open(symbol_csv) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            data.append(row)
    stock_open0 = str(data[0][4])
    stock_open1 = str(data[2][4])
    stock_diff = 0
    if stock_open0 >= stock_open1:
        stock_diff = 1
    else:
        stock_diff = 0

    form_string = str(stock_diff)
    return form_string

@app.route('/UpDownVolume', methods=['GET'])
def up_down_volume():
    data = []
    count = 0
    with open('count.txt', 'r') as f:
        for line in f:
            count = int(line.strip())
    f.close()
    if count == 0:
        count = len(symbol_list) - 1
    else:
        count -= 1
    symbol_csv = 'symbol_csv_dir/intraday_{}.csv'.format(symbol_list[count])
    with open(symbol_csv) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            data.append(row)
    stock_open0 = str(data[0][5])
    stock_open1 = str(data[2][5])
    stock_diff = 0
    if stock_open0 >= stock_open1:
        stock_diff = 1
    else:
        stock_diff = 0

    form_string = str(stock_diff)
    return form_string


if __name__ == '__main__':
    app.run()

# Gadget CPU CODE


# -- Retro
# Gadgets
# local
# ret0 = gdt.Wifi0:WebGet("http://127.0.0.1:5000/update")
# local
# ret1 = gdt.Wifi1:WebGet("http://127.0.0.1:5000/Date")
# local
# ret2 = gdt.Wifi2:WebGet("http://127.0.0.1:5000/Time")
# local
# ret3 = gdt.Wifi3:WebGet("http://127.0.0.1:5000/Open")
# local
# ret4 = gdt.Wifi4:WebGet("http://127.0.0.1:5000/High")
# local
# ret5 = gdt.Wifi5:WebGet("http://127.0.0.1:5000/Low")
# local
# ret6 = gdt.Wifi6:WebGet("http://127.0.0.1:5000/Close")
# local
# ret7 = gdt.Wifi7:WebGet("http://127.0.0.1:5000/Volume")
# local
# ret8 = gdt.Wifi8:WebGet("http://127.0.0.1:5000/UpDownOpen")
# local
# ret9 = gdt.Wifi9:WebGet("http://127.0.0.1:5000/UpDownHigh")
# local
# ret10 = gdt.Wifi10:WebGet("http://127.0.0.1:5000/UpDownLow")
# local
# ret11 = gdt.Wifi11:WebGet("http://127.0.0.1:5000/UpDownClose")
# local
# ret12 = gdt.Wifi12:WebGet("http://127.0.0.1:5000/UpDownVolume")
#
# local
# lcd0 = gdt.Lcd0
# local
# lcd1 = gdt.Lcd1
# local
# lcd2 = gdt.Lcd2
# local
# lcd3 = gdt.Lcd3
# local
# lcd4 = gdt.Lcd4
# local
# lcd5 = gdt.Lcd5
# local
# lcd6 = gdt.Lcd6
# local
# lcd7 = gdt.Lcd7
# local
# lcd8 = gdt.Lcd8
# local
# lcd9 = gdt.Lcd9
# local
# lcd10 = gdt.Lcd10
# local
# lcd11 = gdt.Lcd11
# local
# lcd12 = gdt.Lcd12
# local
# lcd13 = gdt.Lcd13
# local
# lcd14 = gdt.Lcd14
# local
# lcd15 = gdt.Lcd15
#
# local
# led3 = gdt.Led3
# local
# led4 = gdt.Led4
# local
# led5 = gdt.Led5
# local
# led6 = gdt.Led6
# local
# led7 = gdt.Led7
#
# local
# led11 = gdt.Led11
# local
# led12 = gdt.Led12
# local
# led13 = gdt.Led13
# local
# led14 = gdt.Led14
# local
# led15 = gdt.Led15
#
# -- update
# function is repeated
# every
# time
# tick
#
# function
# eventChannel1(sender, response)
# local
# ret0 = gdt.Wifi0:WebGet("http://127.0.0.1:5000/update")
# handle = response.RequestHandle
# responseCode = response.ResponseCode
# isError = response.IsError
# errorType = response.ErrorType
# errorMsg = response.ErrorMessage
# contentType = response.ContentType
# text = response.Text
# type = response.Type
# log("handle: "..tostring(handle))
# log("responseCode: "..tostring(responseCode))
# log("isError: "..tostring(isError))
# log("errorType: "..tostring(errorType))
# log("errorMessage: "..tostring(errorMsg))
# log("contentType: "..tostring(contentType))
# log("text: "..tostring(text))
# lcd8.Text = lcd0.Text
# lcd9.Text = lcd1.Text
# lcd10.Text = lcd2.Text
# lcd11.Text = lcd3.Text
# lcd12.Text = lcd4.Text
# lcd13.Text = lcd5.Text
# lcd14.Text = lcd6.Text
# lcd15.Text = lcd7.Text
#
# led11.Color = led3.Color
# led12.Color = led4.Color
# led13.Color = led5.Color
# led14.Color = led6.Color
# led15.Color = led7.Color
# led11.State = led3.State
# led12.State = led4.State
# led13.State = led5.State
# led14.State = led6.State
# led15.State = led7.State
#
# lcd0.Text = text
# end
# function
# eventChannel2(sender, response)
# local
# ret1 = gdt.Wifi1:WebGet("http://127.0.0.1:5000/Date")
# text = response.Text
# type = response.Type
# stock_date = tostring(text)
# lcd1.Text = stock_date
# end
# function
# eventChannel3(sender, response)
# local
# ret2 = gdt.Wifi2:WebGet("http://127.0.0.1:5000/Time")
# text = response.Text
# type = response.Type
# stock_time = tostring(text)
# lcd2.Text = stock_time
# end
# function
# eventChannel4(sender, response)
# local
# ret3 = gdt.Wifi3:WebGet("http://127.0.0.1:5000/Open")
# text = response.Text
# type = response.Type
# stock_open = tostring(text)
# lcd3.Text = stock_open
# end
# function
# eventChannel5(sender, response)
# local
# ret4 = gdt.Wifi4:WebGet("http://127.0.0.1:5000/High")
# text = response.Text
# type = response.Type
# stock_high = tostring(text)
# lcd4.Text = stock_high
# end
# function
# eventChannel6(sender, response)
# local
# ret5 = gdt.Wifi5:WebGet("http://127.0.0.1:5000/Low")
# text = response.Text
# type = response.Type
# stock_low = tostring(text)
# lcd5.Text = stock_low
# end
# function
# eventChannel7(sender, response)
# local
# ret6 = gdt.Wifi6:WebGet("http://127.0.0.1:5000/Close")
# text = response.Text
# type = response.Type
# stock_close = tostring(text)
# lcd6.Text = stock_close
# end
# function
# eventChannel8(sender, response)
# local
# ret7 = gdt.Wifi7:WebGet("http://127.0.0.1:5000/Volume")
# text = response.Text
# type = response.Type
# stock_volume = tostring(text)
# lcd7.Text = stock_volume
#
# end
#
# function
# eventChannel9(sender, response)
# local
# ret8 = gdt.Wifi8:WebGet("http://127.0.0.1:5000/UpDownOpen")
# text = response.Text
# type = response.Type
# up_down = tostring(text)
# if up_down == "1" then led3.Color = color.green
# elseif
# up_down == "0"
# then
# led3.Color = color.red
# else led3.Color = color.yellow
# end
#
# end
#
# function
# eventChannel10(sender, response)
# local
# ret9 = gdt.Wifi9:WebGet("http://127.0.0.1:5000/UpDownHigh")
# text = response.Text
# type = response.Type
# up_down = tostring(text)
# if up_down == "1" then led4.Color = color.green
# elseif
# up_down == "0"
# then
# led4.Color = color.red
# else led4.Color = color.yellow
# end
#
# end
#
# function
# eventChannel11(sender, response)
# local
# ret10 = gdt.Wifi10:WebGet("http://127.0.0.1:5000/UpDownLow")
# text = response.Text
# type = response.Type
# up_down = tostring(text)
# if up_down == "1" then led5.Color = color.green
# elseif
# up_down == "0"
# then
# led5.Color = color.red
# else led5.Color = color.yellow
# end
#
# end
#
# function
# eventChannel12(sender, response)
# local
# ret11 = gdt.Wifi11:WebGet("http://127.0.0.1:5000/UpDownClose")
# text = response.Text
# type = response.Type
# up_down = tostring(text)
# if up_down == "1" then led6.Color = color.green
# elseif
# up_down == "0"
# then
# led6.Color = color.red
# else led6.Color = color.yellow
# end
#
# end
#
# function
# eventChannel13(sender, response)
# local
# ret12 = gdt.Wifi12:WebGet("http://127.0.0.1:5000/UpDownVolume")
# text = response.Text
# type = response.Type
# up_down = tostring(text)
# if up_down == "1" then led7.Color = color.green
# elseif
# up_down == "0"
# then
# led7.Color = color.red
# else led7.Color = color.yellow
# end
#
# end














