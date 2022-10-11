from what_is_year_now import what_is_year_now
import pytest
from unittest.mock import MagicMock, patch


@patch('urllib.request.urlopen')
def test_format_ymd(urlopen):
    mock = MagicMock()
    mock.read.return_value = '{"$id":"1",' \
                             '"currentDateTime":"2022-10-10T23:32Z",' \
                             '"utcOffset":"00:00:00",' \
                             '"isDayLightSavingsTime":false,' \
                             '"dayOfTheWeek":"Monday",' \
                             '"timeZoneName":"UTC",' \
                             '"currentFileTime":133099183602978015,' \
                             '"ordinalDate":"2022-283",' \
                             '"serviceResponse":null}'
    mock.__enter__.return_value = mock
    urlopen.return_value = mock

    year = what_is_year_now()
    assert year == 2022


@patch('urllib.request.urlopen')
def test_format_dmy(urlopen):
    mock = MagicMock()
    mock.read.return_value = '{"$id":"1",' \
                             '"currentDateTime":"10.10.2022T23:32Z",' \
                             '"utcOffset":"00:00:00",' \
                             '"isDayLightSavingsTime":false,' \
                             '"dayOfTheWeek":"Monday",' \
                             '"timeZoneName":"UTC",' \
                             '"currentFileTime":133099183602978015,' \
                             '"ordinalDate":"2022-283",' \
                             '"serviceResponse":null}'
    mock.__enter__.return_value = mock
    urlopen.return_value = mock

    year = what_is_year_now()
    assert year == 2022


@patch('urllib.request.urlopen')
def test_format_invalid(urlopen):
    mock = MagicMock()
    mock.read.return_value = '{"$id":"1",' \
                             '"currentDateTime":"10102022T23:32Z",' \
                             '"utcOffset":"00:00:00",' \
                             '"isDayLightSavingsTime":false,' \
                             '"dayOfTheWeek":"Monday",' \
                             '"timeZoneName":"UTC",' \
                             '"currentFileTime":133099183602978015,' \
                             '"ordinalDate":"2022-283",' \
                             '"serviceResponse":null}'
    mock.__enter__.return_value = mock
    urlopen.return_value = mock

    with pytest.raises(ValueError):
        what_is_year_now()


@patch('urllib.request.urlopen')
def test_response_invalid(urlopen):
    mock = MagicMock()
    mock.read.return_value = '{"$id":"1",' \
                             '"currentDateTimeInvalid":"10102022T23:32Z",' \
                             '"utcOffset":"00:00:00",' \
                             '"isDayLightSavingsTime":false,' \
                             '"dayOfTheWeek":"Monday",' \
                             '"timeZoneName":"UTC",' \
                             '"currentFileTime":133099183602978015,' \
                             '"ordinalDate":"2022-283",' \
                             '"serviceResponse":null}'
    mock.__enter__.return_value = mock
    urlopen.return_value = mock

    with pytest.raises(KeyError):
        what_is_year_now()
