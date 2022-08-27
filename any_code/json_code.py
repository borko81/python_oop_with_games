import json
from datetime import datetime
today = datetime.now()
print(today)

d = {
    'foo': 'bar',
    'alice': 1,
    'wonderland': [1, 2, 3],
    'today': str(today)
}

d_json = json.dumps(d, indent=2, sort_keys=True, separators=(',', ':'))

print(d_json)

s = '{"wonderland": [1, 2, 3], "foo": "bar", "alice": 1}'

s_to_dict = json.loads(s)
print(s_to_dict.get('foo1', 'Not Found foo1'))