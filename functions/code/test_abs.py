def test_abs():
    # Arrange
    input = -40
    output = 40

    # Act
    result = get_abs(input)

    # Assert
    assert result == output 

def get_abs(input):
    return abs(input)
