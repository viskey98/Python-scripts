import re
requested_name = '/games///arsenal////'
p = re.compile('/+')
requested_name = p.sub('/',requested_name)
print(requested_name)