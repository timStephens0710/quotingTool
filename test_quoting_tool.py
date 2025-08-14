from calculation import calculate_quote

def test_calculate_quote():
    '''
    This test 
    '''
    calculated_quote = calculate_quote(200, 3, 16, 25)
    expected_quote = 1000
    assert calculated_quote == expected_quote

