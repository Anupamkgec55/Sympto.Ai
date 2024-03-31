from django.shortcuts import render
from joblib import load

model=load('./Model/svc_model2.joblib')

def Home(request):
    return render(request,'index.html')

def Welcome(request):
    return render(request,'index123.html')

def About(request):
    return render(request,'about.html')

def Dept(request):
    return render(request,'departments.html')

def User(request):
    Age = float(request.GET['Age'])
    Gender = float(request.GET['Gender'])
    Total_Bilirubin = float(request.GET['TB'])
    Direct_Bilirubin = float(request.GET['DB'])
    Alkaline_Phosphotase = float(request.GET['Alkphos'])
    Alamine_Aminotransferase = float(request.GET['Alamine_Aminotransferase'])
    Aspartate_Aminotransferase = float(request.GET['Aspartate_Aminotransferase'])
    Total_Protiens = float(request.GET['Total_Protiens'])
    Albumin = float(request.GET['ALB'])
    Albumin_and_Globulin_Ratio = float(request.GET['A/G Ratio'])
    
    y_pred=model.predict([[Age,Gender,Total_Bilirubin,Direct_Bilirubin,Alkaline_Phosphotase,Alamine_Aminotransferase,Aspartate_Aminotransferase,Total_Protiens,Albumin,Albumin_and_Globulin_Ratio]])
    # knn_acc_score = accuracy_score(y_test, knn_predicted)

    return render(request,'user.html',{'name':y_pred})
