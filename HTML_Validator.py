#!/bin/python3


def validate_html(html):
    '''
    This function performs a limited version of html validation by
    checking whether every opening tag has a corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''
    try:
        extracted = _extract_tags(html)
    except Exception:
        return False
    stack = []
    balanced = True
    for tag in extracted:
        if '/' not in tag:
            stack.append(tag)
        else:
            if stack == []:
                balanced = False
            else:
                last = stack.pop()
                if tag[2:] not in last[1:]:
                    balanced = False
    if balanced and (stack == []):
        return True
    else:
        return False

    # HINT:
    # use the _extract_tags function below to generate a list of html tags
    # without any extra text;
    # then process these html tags using the balanced parentheses algorithm
    # from the class/book
    # the main difference between your code and the code from class will be
    # that you will have to keep track of not just the 3 types of parentheses,
    # but arbitrary text located between the html tags


def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions that are not
    meant to be used directly by the user are prefixed with an underscore.

    This function returns a list of all the html tags
    contained in the input string, stripping out all text not contained
    within angle brackets.

    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''
    stack = []
    length = len(html) - 1
    if ('<' in html) and ('>' in html):
        for i in range(length):
            empty = ''
            if html[i] == '<':
                empty += html[i]
                i += 1

                while html[i] != '>' and i < length:
                    empty += html[i]
                    i += 1
                empty += '>'
                stack.append(empty)
        return stack
    elif ('<' in html):
        raise ValueError('found < without an >')
    else:
        return []
