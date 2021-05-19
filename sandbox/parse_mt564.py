import re

EXAMPLE_MT564 = """{1:F01FIDELITYXISO0001000002}{2:O5640949021005FIDELITYXISO00010000020210050949N}{4:
:16R:GENL
:20C::CORP//065648947
:20C::SEME//065648947400005
:23G:REPL
:22F::CAEV//CHAN
:22F::CAMV//MAND
:98A::PREP//20020117045443
:25D::PROC//COMP
:16R:LINK
:22F::LINK//AFTE
:13A::LINK//564
:20C::PREV//065648947400004
:16S:LINK
:16S:GENL
:16R:USECU
:35B:CUSIP 843899105
SOUTHERN TELECOMMUNICATIONS CO
:16R:FIA
:94B::PLIS//SECM/XNYS
:16S:FIA
:16R:ACCTINFO
:97A::SAFE//77933
:93A::ELIG//UNIT/1400,
:93A::SETT//UNIT/1400,
:16S:ACCTINFO
:16S:USECU
:16R:CADETL
:98A::EFFD//20020116
:98A::FDDT//20020116
:16S:CADETL
:16R:CAOPTN
:13A::CAON//011
:22F::CAOP//OTHE
:17B::DFLT//Y
:92D::NEWO//50,/0,5
:16S:CAOPTN
:16R:ADDINFO
:70E::ADTX///FIDELITY CORP_ACTION_TYPE/ADRBAS
:70E::ADTX///CORP_ACTION_STATUS_CODE/C
:70E::ADTX///PRIMARY_MARKET_INDICATOR/N
:70E::ADTX///COUNTRY_OF_ISSUE_ISO_CODE/US
:70E::ADTX///COUNTRY_OF_INCORPORATION_ISO_CODE/RU
:70E::ADTX///VENDOR_CANCEL_INDICATOR/N
:16S:ADDINFO -}"""


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

MT564_REGEX = re.compile(
    r"^(:16R[:]+GENL\s"
        r"(:20C[:]+(?P<reference1>[^\s:]+)\s*)?"
        r"(:20C[:]+(?P<reference2>[^\s:]+)\s*)?"
        r"(:20C[:]+(?P<reference3>[^\s:]+)\s*)?"
        r"(:23G[:]+(?P<function>[^\s:]+)\s*)?"
        r"(:22F[:]+(?P<indicator1>[^\s:]+)\s*)?"
        r"(:22F[:]+(?P<indicator2>[^\s:]+)\s*)?"
        r"(:22F[:]+(?P<indicator3>[^\s:]+)\s*)?"
        r"(:98A[:]+(?P<preperation_date>[^\s:]+)\s*)?"
        r"(:25D[:]+(?P<processing_status>[^\s:]+)\s*)?"
        r"(:16R[:]+LINK\s"
            r"(:22F[:]+(?P<link1_type>[^\s:]+)\s*)?"
            r"(:13A[:]+(?P<link1_message>[^\s:]+)\s*)?"
            r"(:20C[:]+(?P<link1_reference>[^\s:]+)\s*)?"
        r":16S[:]+LINK\s)?"
        r"(:16R[:]+LINK\s"
            r"(:22F[:]+(?P<link2_type>[^\s:]+)\s*)?"
            r"(:13A[:]+(?P<link2_message>[^\s:]+)\s*)?"
            r"(:20C[:]+(?P<link2_reference>[^\s:]+)\s*)?"
        r":16S[:]+LINK\s)?"
    r":16S:GENL\s)?"
    r"(:16R:USECU\s)?"
        r"(:35B:(?P<security1>[\s\S][^:]+))?"
        r"(:35B:(?P<security2>[\s\S][^:]+))?"
        r"(:35B:(?P<security3>[\s\S][^:]+))?"
        r"(:16R:FIA\s)?"
            r"(:94B[:]+(?P<place_of_listing>[^\s:]+)\s*)?"
            r"(:22F[:]+(?P<day_count>[^\s:]+)\s*)?"
            r"(:12A[:]+(?P<security_type>[^\s:]+)\s*)?"
            r"(:11A[:]+(?P<security_currency>[^\s:]+)\s*)?"
            r"(:98A[:]+(?P<security_date1>[^\s:]+)\s*)?"
            r"(:98A[:]+(?P<security_date2>[^\s:]+)\s*)?"
            r"(:98A[:]+(?P<security_date3>[^\s:]+)\s*)?"
            r"(:98A[:]+(?P<security_date4>[^\s:]+)\s*)?"
            r"(:98A[:]+(?P<security_date5>[^\s:]+)\s*)?"
            r"(:98A[:]+(?P<security_date6>[^\s:]+)\s*)?"
            r"(:98A[:]+(?P<security_date7>[^\s:]+)\s*)?"
            r"(:98A[:]+(?P<security_date8>[^\s:]+)\s*)?"
            r"(:98A[:]+(?P<security_date9>[^\s:]+)\s*)?"
            r"(:92A[:]+(?P<coupon_rate>[^\s:]+)\s*)?"
            r"(:36B[:]+(?P<tradable_quantity>[^\s:]+)\s*)?"
        r"(:16S:FIA\s)?"
        r"(:16R:ACCTINFO\s)?"
        r"(:95A[:]+(?P<account_owner>[\s\S][^:]+))?"
        r"(:97A[:]+(?P<safe_keeping_account>[^\s:]+)\s*)?"
        r"(:94A[:]+(?P<account_place_of_safe_keeping>[\s\S][^:]+))?"
        r"(:93A[:]+(?P<balance1>[\s\S][^:]+))?"
        r"(:93A[:]+(?P<balance2>[\s\S][^:]+))?"
        r"(:16S:ACCTINFO\s)?"
    r"(:16S:USECU\s)?"
    r"(:16R:INTSEC\s(.*?):16S:INTSEC\s)?"
    r"(:16R:CADETL\s)?"
        r"(:98A[:]+(?P<cadetl_date1>[^\s:]+)\s*)?"
        r"(:98A[:]+(?P<cadetl_date2>[^\s:]+)\s*)?"
        r"(:98A[:]+(?P<cadetl_date3>[^\s:]+)\s*)?"
        r"(:98A[:]+(?P<cadetl_date4>[^\s:]+)\s*)?"
        r"(:98A[:]+(?P<cadetl_date5>[^\s:]+)\s*)?"
        r"(:98A[:]+(?P<cadetl_date6>[^\s:]+)\s*)?"
        r"(:98A[:]+(?P<cadetl_date7>[^\s:]+)\s*)?"
        r"(:98A[:]+(?P<cadetl_date8>[^\s:]+)\s*)?"
        r"(:98A[:]+(?P<cadetl_period1>[^\s:]+)\s*)?"
        r"(:98A[:]+(?P<cadetl_period2>[^\s:]+)\s*)?"
        r"(:98A[:]+(?P<cadetl_period3>[^\s:]+)\s*)?"
        r"(:98A[:]+(?P<cadetl_period4>[^\s:]+)\s*)?"
        r"(:98A[:]+(?P<cadetl_period5>[^\s:]+)\s*)?"
        r"(:98A[:]+(?P<cadetl_period6>[^\s:]+)\s*)?"
        r"(:98A[:]+(?P<cadetl_period7>[^\s:]+)\s*)?"
        r"(:98A[:]+(?P<cadetl_period8>[^\s:]+)\s*)?"
    r":(16S:CADETL\s)?"
    r"(:16R:CAOPTN\s)?"
        r"(:13A[:]+(?P<caoptn_caon>[^\s:]+)\s*)?"
        r"(:22F[:]+(?P<caoptn_indicator1>[^\s:]+)\s*)?"
        r"(:22F[:]+(?P<caoptn_indicator2>[^\s:]+)\s*)?"
        r"(:94C[:]+(?P<caoptn_place1>[^\s:]+)\s*)?"
        r"(:94C[:]+(?P<caoptn_place2>[^\s:]+)\s*)?"
        r"(:11A[:]+(?P<caoptn_currency>[^\s:]+)\s*)?"
        r"(:17B[:]+(?P<caoptn_flag1>[^\s:]+)\s*)?"
        r"(:17B[:]+(?P<caoptn_flag2>[^\s:]+)\s*)?"
        r"(:17B[:]+(?P<caoptn_flag3>[^\s:]+)\s*)?"
        r"(:17B[:]+(?P<caoptn_flag4>[^\s:]+)\s*)?"
        r"(:17B[:]+(?P<caoptn_flag5>[^\s:]+)\s*)?"
        r"(:17B[:]+(?P<caoptn_flag6>[^\s:]+)\s*)?"
    r"(:16S:CAOPTN\s)?"
    r"(:16R:ADDINFO\s(.*?):16S:ADDINFO)?"
    r".*",
    re.DOTALL
)


def parse_message():
    raw = EXAMPLE_MT564.strip()
    m = SWIFT_REGEX.match(raw)

    raw = m.group("text").strip()
    print(raw)

    m = MT564_REGEX.match(raw)
    print(MT564_REGEX)
    print(m)
    if m:
        print(m.groups())
        for k, v in m.groupdict().items():
            print("%s->%r" % (k, v))


def parse_basic_header():
    """ {1:    F    01   BANKBEBB   2222   123456}

        group 1 Application ID as follows:
            F = FIN (financial application)
            A = GPA (general purpose application)
            L = GPA (for logins, and so on)

        group 2 Service ID:
            01 = FIN/GPA
            21 = ACK/NAK

        group 3 Logical terminal (LT) address. It is fixed at 12 characters

        group 4 Session number. It is generated by the user’s computer and is padded with zeros.

        group 5 Sequence number that is generated by the user’s computer. It is padded with zeros.
    """
    raw = EXAMPLE_MT564.strip()
    m = SWIFT_REGEX.match(raw)

    raw = m.group("basic_header").strip()
    print(raw)

    HEADER_REGEX = re.compile(
        r"^(F|A|L)(\d{2})(\w{12})(\d{4})(\d{6})"
    )
    m = HEADER_REGEX.match(raw)
    print(m.groups())


def parse_application_header():
    """ There are two types of application headers: Input and Output. Both are fixed-length and continuous with no field delimiters.

        {2:    I     100    BANKDEFFXXXX    U       3       003}

        group 1 Input Output

        group 2 Message type:

        group 3 receivers address. It is fixed at 12 characters

        group 4 message priority as follows:
            S = System
            N = Normal
            U = Urgent

        group 5 deliver monitoring field as follows:
            1 = Non delivery warning (MT010)
            2 = Delivery notification (MT011)
            3 = Both valid = U1 or U3, N2 or N

        group 6  Obsolescence period. It specifies when a non-delivery notification is generated as follows:
            Valid for U = 003 (15 minutes)
            Valid for N = 020 (100 minutes)
    """
    raw = EXAMPLE_MT564.strip()
    m = SWIFT_REGEX.match(raw)

    raw = m.group("application_header").strip()
    print(raw)


    # r"^((I)((\d{3})(\w{12})(S|N|U)(\d)(\d{3})))?"
    # r"((O)(\d{3})(\d{4})(\d{6})(\w{12})(\d{4})(\d{6})(\d{6})(\d{4})(S|N|U))?"

    raw = "O5640949021005FIDELITYXISO00010000020210050949N"

    HEADER_REGEX = re.compile(
        r"^(O|I)(\d{3})"
        r"((\d{4})(\d{6})(\w{12})(\d{4})(\d{6})(\d{6})(\d{4})(S|N|U))?"
        r"((\w{12})(S|N|U)(\d)(\d{3}))?"
    )
    m = HEADER_REGEX.match(raw)
    print(m.groups())


def search_addinfo_narrative():
    sample_raw = """:16R:CAOPTN
:13A::CAON//011
:22F::CAOP//OTHE
:17B::DFLT//Y
:92D::NEWO//50,/0,5
:16S:CAOPTN
:16R:ADDINFO
:70E::ADTX///FIDELITY CORP_ACTION_TYPE/ADRBAS
:70E::ADTX///CORP_ACTION_STATUS_CODE/C
:70E::ADTX///PRIMARY_MARKET_INDICATOR/N
:70E::ADTX///COUNTRY_OF_ISSUE_ISO_CODE/US
:70E::ADTX///COUNTRY_OF_INCORPORATION_ISO_CODE/RU
:70E::ADTX///VENDOR_CANCEL_INDICATOR/N
:16S:ADDINFO -}"""

    # regex = re.compile(
    #     r".*?(:17B[:]+([\s\S][^:]+))?"
    # )


    regex = re.compile(
        ":(\d{2}\w)[:]+(\w{4})//([\s\S][^:]+)"
    )

    regex = re.compile(
        ":(\d{2}\w)[:]+([\s\S][^:]+)"
    )

    result = regex.findall(EXAMPLE_MT564)
    clean = [(item[0].strip(), item[1].strip()) for item in result]
    print (clean)


if __name__ == "__main__":
    # search_addinfo_narrative()
    # parse_basic_header()
    parse_application_header()