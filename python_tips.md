   for i in range(10):
       #print("{0}\r".format(i))
       sys.stdout.write("\r{0}".format(i))
       sys.stdout.flush()
       time.sleep(1)

