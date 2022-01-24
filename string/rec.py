# def fun(n):
#   if n <= 1:
#     return 0
#   else:
#     return 1+fun(n/2)

def fun(n):
  if n == 0:
    return
  fun(n/2)
  print(n%2)

fun(13)