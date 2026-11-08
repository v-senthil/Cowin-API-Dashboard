# CoWIN API Dashboard

Small Flask app that looks up COVID-19 vaccination slots in India by pincode and date, using the public CoWIN API.

## How it works
- `/` shows a form for a pincode and a date.
- `/getpin` calls `https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin` with those params and renders the available centres/sessions in a table, or an error if none are open.

## Use
1. `pip install -r requirements.txt`
2. `python app.py`
3. Open the app, enter a pincode and date, and see available vaccination slots.

Built in 2021, during the CoWIN vaccine-booking rush. The public API this depends on may no longer be live.
