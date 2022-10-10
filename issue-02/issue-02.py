
from morse import decode
import pytest


@pytest.mark.parametrize(
    "source_string,result",
    [('... --- ...', 'SOS'),
     ('SOS', 'SOS'),
     ('... --- ..', 'SOS'),
     pytest.param('SOS', 'SOS', marks=pytest.mark.xfail(raises=KeyError))]

)
def test_decode(source_string, result):
    assert decode(source_string) == result
