#FRR
FRR_range = range(1,10+1,1) #[min,max,increment]

#Channel 1 - Buffer 
Buffer = [True, range(180,180+1,20)]

#Channel 2 - Lipid 1 in ethanol
#Lp1=[Active?,Name, MW, Range , Concentration]  
Lp1 = ["Lipid1_Name", 100, "Base",  10]  

#Channel 3 - Lipid 2 in ethanol - if not active, set range to 0
#Lp2= [Active?,Name, MW, Range , Concentration]  
Lp2 = ["Lipid2_Name", 50, range(0,(10+1),5), 5]  

#Channel 4 - Lipid 3 in ethanol - if not active, set range to 0
#Lp3= [Name, MW, Range , Concentration]  
Lp3 = ["Lipid3_Name", 50, range(0,(10+1),5), 5]   


exp_params, flow_rate  = [],[]
n = 0
def flow_calc(FRR_range, Buffer, Lp1, Lp2, Lp3):
    Lp2_Lipid_Mr_Ratio = Lp1[1]/Lp2[1]
    Lp3_Lipid_Mr_Ratio = Lp1[1]/Lp3[1]
    if Buffer[0] == True and Lp1[2] == "Base":
        for buffer_FR_total in Buffer[1]: 
            for FRR_value in FRR_range:
                lipid_FR_total = buffer_FR_total/FRR_value
                for a in Lp2[2]:
                    for b in Lp3[2]:
                        Lp1_const = (((100-a-b)/1000))/(Lp1[3]*0.001)
                        Lp2_const = ((a/1000)*Lp2_Lipid_Mr_Ratio)/(Lp2[3]*0.001)
                        Lp3_const = ((b/1000)*Lp3_Lipid_Mr_Ratio)/(Lp3[3]*0.001)
                        FR_const = Lp1_const + Lp2_const + Lp3_const
                        Lp1_flow_rate = (Lp1_const/FR_const)*lipid_FR_total 
                        Lp2_flow_rate = (Lp2_const/FR_const)*lipid_FR_total 
                        Lp3_flow_rate = (Lp3_const/FR_const)*lipid_FR_total 
                        totalFR = buffer_FR_total + lipid_FR_total
                        exp_params.append([totalFR,FRR_value,100-a-b,a,b])
                        flow_rate.append([buffer_FR_total,Lp1_flow_rate,Lp2_flow_rate,Lp3_flow_rate])
                        n=n+1
    return(exp_params,flow_rate)