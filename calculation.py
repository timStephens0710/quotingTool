def calculate_quote(cost_price, margin, hours_spent, wage) -> float:
    '''
    The following functions takes in the following inputs to calculate the quote:
    - Cost price
    - Hours spent
    - Wage
    - Margin    
    '''
    calculated_quote = (cost_price * margin) + (hours_spent * wage)
    return calculated_quote
