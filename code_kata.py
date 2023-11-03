# get_initials(name)
# 'Jordan Xiao' => 'J.X'

# 'Jordan Xiao' 
# 1. split the name in two (" ")
# 1.b identify which string manipulation method we need
# 2. pull out [0] from split name => 'Jordan'
# 3. pull out 'J' as well, using [0] on the string once again.
# 2b. pull out [1] from split name => 'Xiao'
# 3b. pull out 'X' as well, using [0] on the string once again.
# 4. add the variables together with a '.' in between
# 'J.X'
# + extra feature: Make sure to capitalize both first and last name

def get_initials(name):
    split_name = name.upper().split()
    first_name_initial = split_name[0][0]
    last_name_initial = split_name[1][0]
    return f"{first_name_initial}.{last_name_initial}"
    
print(get_initials('Jordan Xiao'))
print(get_initials('jordan xiao'))