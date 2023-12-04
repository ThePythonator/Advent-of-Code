with open('in.txt') as f:
    lines = [line.strip() for line in f.readlines()]

passports = ['']
for line in lines:
    if line == '':
        passports.append('')
    else:
        passports[-1]+=' '+line

reqNames = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
validCount = 0
for passport in passports:
    req = reqNames.copy()
    fields = passport.strip().split(' ')
    for field in fields:
        name,val = field.split(':')
        if name in req:
            valid = False
            if name == 'byr':
                try:
                    num = int(val)
                    if num >= 1920 and num <= 2002 and len(val) == 4:
                        valid = True
                except ValueError:
                    pass

            elif name == 'iyr':
                try:
                    num = int(val)
                    if num >= 2010 and num <= 2020 and len(val) == 4:
                        valid = True
                except ValueError:
                    pass

            elif name == 'eyr':
                try:
                    num = int(val)
                    if num >= 2020 and num <= 2030 and len(val) == 4:
                        valid = True
                except ValueError:
                    pass
                
            elif name == 'hgt':
                try:
                    val,suf = val[:-2],val[-2:]
                    num = int(val)
                    if num >= 150 and num <= 193 and suf == 'cm':
                        valid = True
                    if num >= 59 and num <= 76 and suf == 'in':
                        valid = True
                except ValueError:
                    pass

            elif name == 'hcl':
                hexValid = True
                for c in val:
                    if c not in 'abcdef1234567890':
                        haxValid = False
                        break
                
                if val[0] == '#' and len(val) == 7 and hexValid:
                    valid = True

            elif name == 'ecl':
                if val in ['amb','blu','brn','gry','grn','hzl','oth']:
                    valid = True

            elif name == 'pid':
                try:
                    num = int(val)
                    if len(val) == 9:
                        valid = True
                except ValueError:
                    pass

            if valid:
                req.remove(name)

    if len(req) == 0:
        validCount += 1

print(validCount)
        
