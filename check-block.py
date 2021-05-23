from block_functions.py import amount, exists_and_confirmed, get_prev, get_link, get_rep, account_to_id

flag = False
metablock =  <burn send id>
genesis = <genesis id>
code = amount(genesis)
open = “0000000000000000000000000000000000000000000000000000000000000000”

while not flag:
  if (exists_and_confirmed(metablock) == False) or (amount(metablock) != code): #code is defined in the contract and is a unique 64bit int
    flag = True

  elif get_type(metablock) == “receive”:
    metablock = get_link(metablock)

  elif get_type(metablock) == “send”:
    source = account_to_id(get_rep(metablock))
    prev = get_prev(metablock)

    while prev != source:
      if prev == open or amount(prev) == code:
        flag = True
        break
      else:
        prev = get_prev(prev)

    if source == genesis:
      break
    else:
      metablock = source

valid_transaction = not flag
