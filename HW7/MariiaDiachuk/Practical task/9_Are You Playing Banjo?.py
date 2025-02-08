def are_you_playing_banjo(name: str) -> str:
    """Determine if someone plays banjo based on their name.
 
    Args:
        name (str): Person's name
        
    Returns:
        str: Message indicating if person plays banjo
    """
    if not name:
        raise ValueError("Name cannot be empty")
    return f"{name} {'plays' if name[0].lower() == 'r' else 'does not play'} banjo"