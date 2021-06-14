def do_stuff(num = 0):
    try:
        if num != None:
            return int(num) + 10
        else:
            return 'Please enter a number'
    except ValueError as err:
        return err
