import os
from flask import Flask, request, jsonify
from skyfield import api, almanac
from datetime import datetime

app = Flask(__name__)

def get_season_dates(year):
    ts = api.load.timescale()
    eph = api.load('de421.bsp')
    t0 = ts.utc(year, 1, 1)
    t1 = ts.utc(year+1, 1, 1)
    times, events = almanac.find_discrete(t0, t1, almanac.seasons(eph))
    season_names = {0: 'الربيع', 1: 'الصيف', 2: 'الخريف', 3: 'الشتاء'}
    results = {}
    for t, e in zip(times, events):
        dt = t.utc_datetime()
        results[season_names[e]] = dt.strftime('%Y-%m-%d')
    return results

@app.route('/seasons')
def seasons():
    year = request.args.get('year', default=datetime.utcnow().year, type=int)
    data = get_season_dates(year)
    return jsonify(data)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
