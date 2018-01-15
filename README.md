# Marshmallow-Arrow

This library provides a Marshmallow field for Arrow objects.

## Usage

Create an ArrowField in your schema:

```python
from marshmallow_arrow import ArrowField


class CalendarEventSchema(Schema):
    name = fields.Str()
    start_datetime = ArrowField(required=False)
```

ArrowFields are deserialized from isoformatted strings

```python
    schema = CalendarEventSchema()
    data, _ = schema.load(
        {'name': 'Birthday Party', 'start_datetime': arrow.utcnow().isoformat()}
    )

    # data:
    # {'start_datetime': <Arrow [2018-01-15T22:22:22.155520+00:00]>, 'name': u'Birthday Party'}
```

and serialized to isoformatted strings

```python
    birthday = arrow.utcnow()
    birthday_event = CalendarEvent('Birthday Party', birthday)
    schema = CalendarEventSchema()
    result = schema.dump(birthday_event)

    # result.data
    # {u'start_datetime': '2018-01-15T22:23:55.861418+00:00', u'name': u'Birthday Party'}
```
