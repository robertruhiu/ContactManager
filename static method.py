# class StringHelper:
#     @staticmethod
#     def abbreviate(string,size):
#         x=string
#         (list(x))
#         for i in range(size):
#             print(''.join(x[i]))
#
# arm=StringHelper()
# arm.abbreviate("hello",3)

# class Convertor:
#
#     @staticmethod
#     def convetor(cm,inch,farenheight,celcius):
#         print("{} degrees is {} farenheit".format(celcius, int(celcius + 32)))
#         print("{} farenheight is {} degrees".format(farenheight, int(farenheight -32)))
#         print("{} inches is {} centimenters".format(inch, float(inch * 2.54)))
#         print("{} centimeters is {} inches".format(cm, float(cm / 2.54)))
#     def cm2inches(self,inches):
#         cm=inches/2.54
#         print (cm)
#     def inches2cm(self,cm):
#         inches=cm*2.54
#         print (inches)
#
# trm=Convertor()
# trm.convetor(37,12,105,37)
# trm.cm2inches(37)
# trm.inches2cm(12)
class Apple:
    @staticmethod
    def apple( color):
        print("A 5 cedi {} apple".format(color))
    @staticmethod
    def set_price(price,color):
        print("A {} cedi {} apple".format(price,color))
trm=Apple()
trm.apple('red')
trm.set_price(6,'blue')
