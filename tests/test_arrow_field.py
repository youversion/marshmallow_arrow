import arrow
from marshmallow import Schema, fields
from marshmallow_arrow import ArrowField


class CalendarEventSchema(Schema):
    name = fields.Str()
    start_datetime = ArrowField(required=False)


class CalendarEvent(object):

    def __init__(self, name, start_datetime=None):
        self.name = name
        self.start_datetime = start_datetime


def test_deserialization():
    birthday = arrow.utcnow().isoformat()
    schema = CalendarEventSchema()
    data, errors = schema.load({'name': 'Birthday Party', 'start_datetime': birthday})
    print(data)
    assert errors == {}
    assert isinstance(data['start_datetime'], arrow.Arrow)
    assert data['start_datetime'].isoformat() == birthday


def test_deserialization_falsy():
    schema = CalendarEventSchema()

    birthday = None
    data, errors = schema.load({'name': 'Birthday Party', 'start_datetime': birthday})
    assert errors == {'start_datetime': [u'Field may not be null.']}

    birthday = False
    data, errors = schema.load({'name': 'Birthday Party', 'start_datetime': birthday})
    assert errors == {'start_datetime': [u'Invalid arrow object.']}

    birthday = ''
    data, errors = schema.load({'name': 'Birthday Party', 'start_datetime': birthday})
    assert errors == {'start_datetime': [u'Invalid arrow object.']}


def test_deserialization_invalid_format():
    birthday = 'Invalid Datetime'
    schema = CalendarEventSchema()
    data, errors = schema.load({'name': 'Birthday Party', 'start_datetime': birthday})
    assert errors == {'start_datetime': [u'Unable to parse datetime.']}


def test_serialization():
    birthday = arrow.utcnow()
    birthday_event = CalendarEvent('Birthday Party', birthday)
    schema = CalendarEventSchema()
    result = schema.dump(birthday_event)
    print(result.data)
    assert result.data['start_datetime'] == birthday.isoformat()


def test_serialization_none():
    birthday_event = CalendarEvent('Birthday Party')
    schema = CalendarEventSchema()
    result = schema.dump(birthday_event)
    assert result.data['start_datetime'] is None
