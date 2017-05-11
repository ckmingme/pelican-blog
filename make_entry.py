import sys
from datetime import datetime


TEMPLATE = """
title: {title}
date: {year}-{month}-{day} {hour}:{minute:02d}
category: 
slug: 
summary: 
status: draft


"""


def make_entry(title):
    today = datetime.today()
    slug = title.lower().strip().replace(' ', '-')
    f_create = 'content/{}_{:0>2}_{:0>2}_{}.md'.format(today.year, today.month, today.day, slug)
    t = TEMPLATE.lstrip().format(title=title,
                                 year=today.year,
                                 month=today.month,
                                 day=today.day,
                                 hour=today.hour,
                                 minute=today.minute)
    with open(f_create, 'w') as w:
        w.write(t)
    print('File created -->', f_create)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        make_entry(sys.argv[1])
    else:
        print('No title given')
