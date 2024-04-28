def print_f(str):
    limit = 80
    if len(str)<80:
        print("\n"+"-"*len(str)+"\n"+str+"\n"+"-"*len(str))
    else:
        print("\n"+"-"*limit+"\n"+str+"\n"+"-"*limit)