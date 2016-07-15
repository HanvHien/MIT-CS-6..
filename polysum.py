def polysum(n,s):
    """
    function called polysum that takes 2 arguments, n and s.
    This function should sum the area and square of the perimeter
    of the regular polygon.
    The function returns the sum, rounded to 4 decimal places."""
    import math
    area = (0.25 * n * s**2) / math.tan(math.pi / n)
    boundary = (s * n) ** 2
    return round(area + boundary, 4)
