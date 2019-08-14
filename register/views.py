from django.shortcuts import render,get_object_or_404
from django.views.generic import CreateView
from .models import Saloon,Files
from django.http import HttpResponse
from .serializers import SaloonSearlizer,FileSerializer
# 
# from rest_framework.views import APIView
# from rest_framework.response import Response
from django.http import HttpResponse
import json
import mysql.connector

from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
# class Register(CreateView):
#     model=Saloon
#     fields=["name","ad_first","ad_second","city","country","pincode","image","password","email"]
# def index(request):
#     return HttpResponse("hijhsdfjgdsfds")


# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="debian-sys-maint",
#   passwd="mLQNLeD9B0n3xyiF"
# )
from .database import db
class Register(APIView):
    parser_class = (FileUploadParser,)
    
    # def get(self,request):
        
    #     saloon=Saloon.objects.all()
        
    #     serializer=SaloonSearlizer(saloon,many=True)
    #     return Response(serializer.data)
    def get(self,request):
        cur=db.mydb.cursor()
        cur.execute("use saloon")
        # print(request.GET)
        # data=request.GET['a']
        # # data=json.loads(data)
        # print(data)
        if 'id' in request.GET:
            cur.execute("SELECT * FROM saloon where saloon_id="+request.GET['id'])

        else:
            cur.execute("SELECT * FROM saloon")
        
        # print(cur)
        row_headers=[x[0] for x in cur.description]
        result=cur.fetchall()
        json_data=[]
        for r in result:
            json_data.append(dict(zip(row_headers,r)))

        # for x in result:
        #     print(x)
        # print(json_data)
        # print("\n\n",type(result))
        # return HttpResponse("hi")
        if 'id' in request.GET:
            id=request.GET['id']
            cur.execute("SELECT * from products where saloon_id="+id);
            row_headers=[x[0] for x in cur.description]
            result=cur.fetchall()
            json_data_sub=[]
            for r in result:
                json_data_sub.append(dict(zip(row_headers,r)))
            json_data[0]['item']=json_data_sub


        # print(json_data)

        return Response(json_data)


    
    def post(self,request):

        # print(request.FILES['image'])
        # # saloon=Saloon.objects.all()
        # 
        # # serializer=SaloonSearlizer(saloon,many=True)
        file_serializer = FileSerializer(data=request.data)
        # print(file_serializer)

        if file_serializer.is_valid():
        #   print("hello")
          file_serializer.save()
        #   print(get_object_or_404(Files,f.pk))
        #   print(f)
        file_name=file_serializer.data
        #   return Response(file_serializer.data, status=status.HTTP_201_CREATED)
    #   else:
    #       return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



        data=request.POST['Saloon']
        data=json.loads(data)
        cur=db.mydb.cursor()
        cur.execute("use saloon")
        # print(file_name)
        sql = "INSERT INTO saloon (name, ad_first,ad_second,city,country,pincode,password,email,image,phone_number) VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s,%s)"
        val = (data['name'],data['ad_first'],data['ad_second'],data['city'],data['country'],
                data['pincode'],data['password'],data['email'],file_name['image'],data['phone_number']
        )
        cur.execute(sql, val)
        db.mydb.commit()


        # print(cur.rowcount, "record inserted.")
        # return HttpResponse("hi")
        # string=""
        res=dict()
        res['status']='success'
        res['code']='200'
        # print(json.dumps)
        return Response([res])




class Product(APIView):
    parser_class = (FileUploadParser,)
    
    # def get(self,request):
        
    #     saloon=Saloon.objects.all()
        
    #     serializer=SaloonSearlizer(saloon,many=True)
    #     return Response(serializer.data)
    def get(self,request):
        res=dict()
        res['status']='success'
        res['code']='200'
        # print(json.dumps)
        return Response([res])


    
    def post(self,request):
        # print(request)
        if request.POST['user'] is not None:
            # print("yes")
            # print(request.POST['data'])
            data=request.POST['data']
            data=json.loads(data)
            cur=db.mydb.cursor()
            cur.execute("use saloon")
            sql="INSERT INTO `products`( `title`, `price`, `category`, `saloon_id`) VALUES (%s,%s,%s,%s)";
            val=(data['title'],data['price'],data['category'],22)
            # print(sql,val)
            cur.execute(sql, val)
            db.mydb.commit()


            print(cur.rowcount, "record inserted.")



            res=dict()
            res['status']='success'
            res['code']='200'
        else:
            res=dict()
            res['status']='error'
            res['code']='404'
        return Response([res])

       
class Order(APIView):

    def get(self,request):
        saloon_id=22
        cur=db.mydb.cursor()
        cur.execute("use saloon")
        cur.execute("SELECT * FROM ordered where saloon_id="+str(saloon_id)+" ORDER BY time desc ")

        row_headers=[x[0] for x in cur.description]

        result=cur.fetchall()
        json_data=[]
        for r in result:
            each_order=dict(zip(row_headers,r))
            pid=each_order['product_id']
            cur.execute("SELECT * FROM products where product_id="+str(pid))
            col_header=[x[0] for x in cur.description]
            col_result=cur.fetchall()
            col_json_data=[]
            for c in col_result:
                col_json_data.append(dict(zip(col_header,c)))

            each_order['product']=col_json_data
            json_data.append(each_order)
            
            # print()
            # json_data.append(dict(zip(row_headers,r)))
        # print(json_data)
        res=dict()
        res['status']='error'
        res['code']='404'
        return Response(json_data)













    def post(self,request):
        # print(request,request.POST)
        cur=db.mydb.cursor()
        cur.execute("use saloon")
        if 'order' in request.POST:

            data_order=request.POST['order']
            data_order=json.loads(data_order)
            data=request.POST['data']
            data=json.loads(data)

            
            count=0;
            for data_order_var in data_order:
                sql = "INSERT INTO ordered (name,city,email,phone_number,saloon_id,product_id) VALUES (%s, %s,%s, %s,%s, %s)"
                val = (data['name'],data['city'],data['email'],data['phone_number'],data_order_var['saloon_id'],data_order_var['product_id']
                )
                cur.execute(sql, val)
                print(sql, val)
                db.mydb.commit()
                count+=cur.rowcount


            # print(count, "record inserted.")
        if 'id' in request.POST:
            # print(request.POST['id'],request.data)
            cur.execute("UPDATE `ordered` SET is_visited=1 WHERE order_id="+request.POST['id'])
            print(cur.rowcount,"efected")
            # print("update table ordered set is_visited=1 where order_id="+request.POST['id'])

        res=dict()
        res['status']='success'
        res['code']='200'
        return Response([res])
    # def put(self,request):
        # print(request.PUT)
        # res=dict()
        # res['status']='success'
        # res['code']='200'
        # return Response([res])
      