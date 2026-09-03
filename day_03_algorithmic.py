class problem1:
    def threshole_check(self,speed:int,error_rate:float)->bool:
        if speed>100 and error_rate<0.02:
            return True
        else:
            return False
class problem2:
    def validition_bound(self,metric:int)->str:
        if metric>=40 and metric<=60:
            return "optimal"
        elif (metric>=10 and metric<=39) or (metric>=61 and metric<=90):
            return "warning"
        else:
            return"critical warning"
class problem3:
    def triplet_seclector(self,a=int,b=int,c=int)->str:
        if b>a and b>c:
            return "peak"
        elif b<a and b<c:
            return"valley"
        else:
            return"flat"
class problem4:
    def enterprise_pipeline(self,has_critical_anomaly=bool,override_active=bool,row_count=int,null_percentage=float)->str:
        if (has_critical_anomaly==True and override_active==True):
            return"rejected"
        elif(row_count>50000 and null_percentage<0.01):
            return"approved"
        elif (row_count>10000):
            return "manual review"
        else:
            return "shoutdown"
p1=problem1()
p2=problem2()
p3=problem3()
p4=problem4()
print("p1 Test Result:",p1.threshole_check(200,0.01))
print("p2 Test Result:",p2.validition_bound(50))
print("p3 Test Result:",p3.triplet_seclector(5,9,3))
print("p4 Test result:",p4.enterprise_pipeline(True,True,60000,0))

