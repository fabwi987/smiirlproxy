# smiirlproxy
Small webserver that that acts as a middleman between a smiirl and any other system.
Trigger the 'callback' URL in your system to increase the counter by one. There is also the option of setting the counter to a specific value.

## URL route that displays the value in json format: {'number': value}
@app.route('/')
Add this in the smirrl counter configuration ->  https://hosting_domain/

## URL route for increasing the value by one
@app.route('/callback')
Add this url in your sending system -> https://hosting_domain/callback

## URL route for setting a value between 0 and 99999
@app.route('/set?value=[value]')
Use this to set a value manually -> https://hosting_domain/set?value=[your_value]

