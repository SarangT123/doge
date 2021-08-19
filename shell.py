import basic
import os
import subprocess

while True:
    text = input('Doge shell 0.1 (Beta) > ')
    if "import" in text:
        importing = text.split(" ")
        if importing[0] == "import":
            f = open(importing[1], 'r')
            imports = f.read()
            f2 = open(importing[2], 'r')
            toimp = f2.read()
            aimp = imports + "\n" + toimp
            print(aimp)
            f2 = open(importing[2], 'w')
            f2.truncate()
            f2.write(aimp)
            f2.close()
            f.close()
        else:
            if text.strip() == "":
                continue
            result, error = basic.run('<stdin>', text)

            if error:
                print(error.as_string())
            elif result:
                if len(result.elements) == 1:
                    print(repr(result.elements[0]))
                else:
                    print(repr(result))

    else:
        if text.strip() == "":
            continue
        result, error = basic.run('<stdin>', text)

        if error:
            print(error.as_string())
        elif result:
            if len(result.elements) == 1:
                print(repr(result.elements[0]))
            else:
                print(repr(result))
