# Simple dataset without deepeval
goldens = [
    {
        "input": "I am user123, I would like a refund for the book and the pen",
        "expected_output": "A refund ticket for 30$ has been issued successfully",
    },
    {
        "input": "I am user123, I would like a refund for the book",
        "expected_output": "A refund ticket for 23$ has been issued successfully",
    },
    {
        "input": "I am user123, I would like no refund, I just want to know what I purchased",
        "expected_output": "no refund tickets were issued only a list of what they bought",
    },
    {
        "input": "I am user999, I would like a refund for the book",
        "expected_output": "tell the user that the username is not valid and ask for username again before giving info about a refund",
    },
    {
        "input": "I am user126, I would like a refund for the water_bottle",
        "expected_output": "no refund given because it is outside of the 30 days guideline",
    },
    {
        "input": "I am user126, I would like a refund for the backpack and water_bottle",
        "expected_output": "A refund ticket for 45$ has been issued successfully only for the backpack",
    },
    {
        "input": "I am user126, I would like a refund for the sneakers",
        "expected_output": "no refund was given because you didn't purchase this item",
    },
]
