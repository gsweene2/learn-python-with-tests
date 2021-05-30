def test_get_length_of_string():
    # Arrange
    input = 'some_string'
    output = 11

    # Act
    result = get_length_of_string(input)

    # Assert
    assert result == output

def get_length_of_string(input):
    return len(input)
