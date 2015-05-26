
'''creates a list of all potential inputs'''
inputs = list()

'''loops all the inputs until it finds a 42'''
r = raw_input()
while( r != '42' ):
    inputs.append( r )
    r = raw_input()

'''needs to join to print a readable vertical string of numbers'''
print '\n%s' % '\n'.join( map(str, inputs) )


