import string
def basket(product,rupee,gst,quantity):
     list :([product:'leather_wallete',rupee:1100,gst:18%,qunatity:1],
          [product:'umbrella',rupee:900,gst:12%,qunatity:4],
          [product:'cigartte',rupee:200,gst:28%,qunatity:3],
          [product:'honey',rupee:100,gst:0%,qunatity:2])
     if rupee >= 500:
         rupee=rupee-5%100
         print (max(gst))
         if max(gst):
             print(list(product))
             print(rupee)
             return rupee
         





