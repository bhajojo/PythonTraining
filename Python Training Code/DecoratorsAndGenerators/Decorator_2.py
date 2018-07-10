def get_text(name):
   return name

def p_decorate(func):
   def func_wrapper(name):
       return name
   return func_wrapper

my_get_text = p_decorate(get_text)

print my_get_text("changing the value")