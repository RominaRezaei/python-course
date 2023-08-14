def word_counter():
    sentence = input("give me a sentence:")
    count = len( sentence.split(""))
    print ("number of words:", count)
    word_counter()