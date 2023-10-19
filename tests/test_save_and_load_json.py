from complaints import complaints

def test_complaint_to_json_and_back():

    complaint = complaints.Complaint(
        summary="Lots of garbage in the main street",
        category="pollution",
        location=complaints.Location(
            street="Main Street",
            number="",
            city="Amsterdam"
        ),
        conversation_id="1234"
    )

    complaint_as_json = complaint.to_json()

    assert type(complaint_as_json) == str

    parsed_complaint = complaints.Complaint.from_json(complaint_as_json)

    assert parsed_complaint.summary == "Lots of garbage in the main street"

def test_problem_to_json_and_back():

    problem = complaints.Problem(
        summary="Lots of garbage in the main street",
        category="pollution",
        location=complaints.Location(
            street="Main Street",
            number="",
            city="Amsterdam"
        ),
        conversations=["1234", "5678"],
        users=["1234", "5678"],
    )

    problem_as_json = problem.to_json()

    assert type(problem_as_json) == str

    parsed_problem = complaints.Problem.from_json(problem_as_json)

    assert parsed_problem.summary == "Lots of garbage in the main street"