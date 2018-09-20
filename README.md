# PyTimecamp
Python wrapper for Timecamp API

## Installation

Install this library
> python setup.py install

## Documentation

### APIS

All Timecamp api can be found [here](https://github.com/timecamp/timecamp-api).
Moreover this application only support the following APIs/methods :

| API | Supported Methods |
| :---: | --- |
| account | list |
| currency | list |
| tax | list |
| users | list, get_current |
| group | list, get_settings, set_settings, add, update, delete |
| tasks | list, filter, add, update |
| entries | filter, add, update |
| entries_changes | filter |
| timer_running | list |
| activity | filter |
| application | filter |
| window_title | filter |
| client | filter, add, update |
| invoice | filter, add, update |
| attendance | filter |
| away_time | filter |

### Authentication

In order to get an authentication token, please refer to the [official documentation](https://github.com/timecamp/timecamp-api#authentication)

### Using the API

First of all build your wrapper :
```python
from ppytimecamp.ppytimecamp import PyTimeCamp
TOKEN = '<YOUR_TOKEN>'
pytimecamp = PyTimeCamp(TOKEN, response_format='json')
```

APIs and methods are listed below. Now you know that you the following syntax to use your object :

> pytimecamp.[api].[method]

### Samples

**Timecamp users**
```python
print pytimecamp.users.list()
print pytimecamp.users.get_current()
```
**Timecamp group**
```python
print pytimecamp.group.get_settings('xxxx')
print pytimecamp.group.set_settings('xxxx', reportTimeRounding=600)
```
**Timecamp tasks**
```python
print pytimecamp.tasks.filter(external_task_id='xxxx')
print pytimecamp.tasks.filter(external_task_id='xxxx', exclude_archived=0)
print pytimecamp.tasks.add(name='test', parent_id=12345)
```
**Timecamp tasks**
```python
from datetime import datetime
from pytimecamp.structtime import StructTime

print pytimecamp.entries.filter(date_to=datetime(2018, 9, 12), date_from=datetime(2018, 9, 12))
print pytimecamp.entries.filter(
    date_to=datetime(2018, 9, 12),
    date_from=datetime(2018, 9, 12),
    task_ids=['xxxx', 'yyyyy']
)
print pytimecamp.entries.add(
    date=datetime(2018, 9, 20),
    duration=3600,
    start_time=StructTime(10, 20, 00),
    end_time=StructTime(11, 20, 00)
)
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)