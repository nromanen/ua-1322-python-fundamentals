def bool_to_yes_no(boolean: bool) -> str:
    """Convert a boolean value to 'Yes' or 'No' string.
 
    Args:
        boolean: The boolean value to convert

    Returns:
        'Yes' if the input is True, 'No' if False
    """
    return "Yes" if boolean else "No"