class Evaluator:
    def zip_evaluate(coefs, words):
        if (type(coefs) != list) or (type(words) != list) or (len(coefs) != len(words)):
            print(-1)
            return
        res = 0
        for i, j in zip(coefs, words):
            if (type(i) != int and type(i) != float) or (type(j) != str):
                print(-1)
                return
            res += (i * len(j))
        print(res)

    def enumerate_evaluate(coefs, words):
        if (type(coefs) != list) or (type(words) != list) or (len(coefs) != len(words)):
            print(-1)
            return
        res = 0
        for i in enumerate(words):
            if (type(coefs[i[0]]) != int and type(coefs[i[0]]) != float) or (type(i[1]) != str):
                print(-1)
                return
            res += coefs[i[0]] * len(i[1])
        print(res)

words = ["Blue", "Green", "Pink", "White", "Purple"]
coefs = [1.5, 2.0, -4, 2.2, 0.0]
Evaluator.zip_evaluate(coefs, words)
Evaluator.enumerate_evaluate(coefs, words)
print()
words = ["Le", "Lorem", "Ipsum", "est", "simple"]
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
Evaluator.zip_evaluate(coefs, words)
Evaluator.enumerate_evaluate(coefs, words)
print()
words = ["Le", "Lorem", "Ipsum", "n'", "est", "pas", "simple"]
coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
Evaluator.zip_evaluate(coefs, words)
Evaluator.enumerate_evaluate(coefs, words)