import pytest
from swiftprocessor.iso15022.common import parse_swift


def test_load_swift():

    message = (
        "{1:F01ASDFJK20AXXX0987654321}"
        "{2:I103ASDFJK22XXXXN}"
        "{4: :20:20180101-ABCDEF :23B:GHIJ :32A:180117CAD5432,1 :33B:EUR9999,0 :50K:/123456-75901 SOMEWHERE New York 999999 GR :53B:/20100213012345 :57C://SC200123 :59:/201001020 First Name Last Name a12345bc6d789ef01a23 Nowhere NL :70:test reference test reason payment group: 1234567-ABCDEF :71A:SHA :77B:Test this -}"
    )

    message_dict = parse_swift(message)

    assert set(message_dict.keys()) == {"basic_header", "application_header", "user_header", "text", "trailer"}


def test_load_swift_fail():

    message_one = (
        "{1:F01ASDFJK20AXXX0987654321}"
        "{4: :20:20180101-ABCDEF :23B:GHIJ :32A:180117CAD5432,1 :33B:EUR9999,0 :50K:/123456-75901 SOMEWHERE New York 999999 GR :53B:/20100213012345 :57C://SC200123 :59:/201001020 First Name Last Name a12345bc6d789ef01a23 Nowhere NL :70:test reference test reason payment group: 1234567-ABCDEF :71A:SHA :77B:Test this -}"
    )

    message_dict = parse_swift(message_one)
    sum([1 if (value is not None) else 0 for value in message_dict.values()]) != 5

    message_two = (
        "{1:F01ASDFJK20AXXX0987654321"
        " :20:20180101-ABCDEF :23B:GHIJ :32A:180117CAD5432,1 :33B:EUR9999,0 :50K:/123456-75901 SOMEWHERE New York 999999 GR :53B:/20100213012345 :57C://SC200123 :59:/201001020 First Name Last Name a12345bc6d789ef01a23 Nowhere NL :70:test reference test reason payment group: 1234567-ABCDEF :71A:SHA :77B:Test this -}"
    )

    with pytest.raises(Exception) as excinfo:
        message_dict = parse_swift(message_two)

    assert "Invalid SWIFT message" in str(excinfo.value)