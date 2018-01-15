"""Provides Arrow field for Marshmallow."""

import arrow
from marshmallow import fields


class ArrowField(fields.Field):
    """
    An isoformatted datetime string.

    Arrow objects are converted to and from isoformatted strings
    by `Schema.dump` and `Schema.load` respectively.
    """

    default_error_messages = {
        'invalid_object': 'Invalid arrow object.',
        'invalid_datetime': 'Unable to parse datetime.',
    }

    def _serialize(self, value, attr, obj):
        if value is None:
            return None

        return value.isoformat()

    def _deserialize(self, value, attr, data):
        if not value:
            raise self.fail('invalid_object')

        try:
            return arrow.get(value)
        except arrow.parser.ParserError:
            raise self.fail('invalid_datetime')
