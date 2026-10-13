from talentminer.parsers.resume_parser import extract_email, extract_phone


def test_extract_email():
    assert extract_email("Contact: jane.doe@example.com | Ottawa") == "jane.doe@example.com"


def test_extract_phone_formats_ten_digits():
    assert extract_phone("Phone 613.555.0199") == "(613) 555-0199"
