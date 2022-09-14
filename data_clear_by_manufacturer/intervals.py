
        
class Intervals():
    
    def __init__(self,feature):
        
        self.feature = feature
        self.interval_range=[1.5,2,2.5,3.0,3.5,4]
        
    def Upper_Interval(self):
        
        import numpy as np
        
        mean,std = np.mean(self.feature),np.std(self.feature)
        
        for interval in self.interval_range:
            
            upper_interval= mean+interval*std
            upper_interval=np.round(upper_interval)
            
            print(f"Interval range STD {interval}: {upper_interval}")
        
    def Lower_Interval(self):
        
        import numpy as np
        
         
        mean,std = np.mean(self.feature),np.std(self.feature)
        
        for interval in self.interval_range:
            
            lower_interval=mean-interval*std
            lower_interval=np.round(lower_interval)
            
            print(f"Interval range STD {interval}: {lower_interval}")
            
            
            
class IntervalFit(Intervals):
    
    def __init__(self,feature):
        Intervals.__init__(self,feature)