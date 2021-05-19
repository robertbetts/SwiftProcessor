import re


SWIFT_REGEX = re.compile(
    r"^"
    r"({1:(?P<basic_header>[^}]+)})?"
    r"({2:(?P<application_header>(I|O)[^}]+)})?"
    r"({3:"
    r"(?P<user_header>"
    r"({113:[A-Z]{4}})?"
    r"({108:[A-Z 0-9]{0,16}})?"
    r"({111:[0-9]{3}})?"
    r"({121:[a-zA-Z0-9]{8}-[a-zA-Z0-9]{4}-4[a-zA-Z0-9]{3}-[89ab][a-zA-Z0-9]{3}-[a-zA-Z0-9]{12}})?"  # NOQA: E501
    r")"
    r"})?"
    r"({4:\s*(?P<text>.+?)\s*-})?"
    r"({5:(?P<trailer>.+)})?"
    r"$",
    re.DOTALL,
)


def parse_swift(swift_message:str, validate=True):
    """ parse iso15022 message and return a dict splitting the message into the
        5 message parts

        An exception is raised if there are no regex matches, implying an invalid
        input swift message

    :param raw_message:
    :return: dict
    """
    match = SWIFT_REGEX.match(swift_message.strip())
    if match:
        if validate\
            and (
                set(match.groupdict().keys()) != {"basic_header", "application_header", "user_header", "text", "trailer"}\
                or match.group("text") is None):

            raise Exception("Invalid SWIFT message")
        return match.groupdict()
    else:
        raise Exception("Invalid SWIFT message")

