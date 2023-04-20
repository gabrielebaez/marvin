from marvin import ai_fn


@ai_fn
def categorize_data_exact(data: list[str], categories: list[str]) -> list[str]:
    """
    Assign each item in `data` to the value in `categories` that it matches most
    closely. Every item must be assigned to a category. Do not assign a `null`
    cateogry.
    """


@ai_fn
def categorize_data(data: list[str], category_description: str) -> list[str]:
    """
    Map each item in `data` to a value that matches the `category_description`
    as close as possible. For example, if the category_description is "pets",
    valid categories would be "cat", "dog", "fish", etc. The category
    description may include examples. Return a list of assigned categories the
    same length and order as `data`.
    """