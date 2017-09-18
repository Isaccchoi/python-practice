first = re.findall(r'\ba\w{3}\b', story)

second = re.findall(r'\w+r\b', story)

third = re.findall(r'\w*[abcde]{3}\w*', story)

fourth = re.sub(r'(?P<before>\w+), (?P<after>\w+)', lambda before, after : r'(?P<before>\w+), (?P<after>\w+)'.format(match.group('before').upper(), r'(?P<before>\w+), (?P<after>\w+)'.format(mat)), story)

p = re.compile(r'(?P<before>\w+), (?P<after>\w+)')

re.sub(p, upper, story)


def upper(m):
    return m.group().upper()


def upper_first_groups(m):
    return '{} {}'.format(m.group(1).upper(), m.group().replace(m.group(1), ''))


re.sub(p, upper, story)


def upper_first_groups(m):
    return '{}, [{}]'.format(m.group(1).upper(), m.group(2))


re.sub(r'foo ([a-z]+) bar', lambda match: r'foo {} bar'.format(match.group(1).upper()), x)
