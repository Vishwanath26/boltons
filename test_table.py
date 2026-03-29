from boltons.tableutils import Table 
t = Table([['short', 'short'], ['very_long_value', 'x']]) 
print(t.to_text()) 
