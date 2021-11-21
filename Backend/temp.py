a=10.324213412
def getFormatedFloat(s):
    val=float(s)

    formatted_float = "{:.2f}".format(val)
    return str(formatted_float)
print(getFormatedFloat("12.444324324"))