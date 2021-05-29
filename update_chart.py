import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from datetime import date
import openpyxl
import seaborn as sns
import cv2
import os
from datetime import date, timedelta
from pathlib import Path
from threading import Thread
import send

class ChartThread(Thread):
    def __init__(self,email_from,email_to,password,emlcheck,ExlPATH):
        Thread.__init__(self)
        self.ExlPATH=ExlPATH;
        self.email_from=email_from;
        self.email_to=email_to;
        self.emlcheck=emlcheck;
        self.password=password;

    def run(self):
        file_name=self.ExlPATH;
        df = pd.read_excel(file_name, engine='openpyxl')
        today = date.today()
        prevday=str(today-timedelta(days=1))
        PATH='data_report/'+prevday;
        if(Path(PATH).is_dir()):
            ch=True;
        else:
            os.mkdir(PATH);
        #print(df.head())
        sns.set_theme(style="darkgrid")
        sns.lineplot(x=df["Time"], y=df["Numbers"],hue=df["Animal"],style=df["Animal"],markers=True,dashes=False,data=df)
        plt.xticks(rotation=35)
        plt.title("Animal Monitering "+str(prevday))
        plt.savefig(PATH+"/Line_"+str(prevday)+".jpg")
        image_path1=PATH+"/Line_"+str(prevday)+".jpg"
        sns.catplot(x="Time", y="Numbers", hue="Animal", kind="bar", data=df)
        plt.xticks(rotation=35)
        plt.title("Animal Monitering "+str(prevday))
        plt.savefig(PATH+"/Bar_"+str(prevday)+".jpg")
        image_path2=PATH+"/Bar_"+str(prevday)+".jpg"
        
        if(self.emlcheck):
            send.send1(self.email_from,self.email_to,self.password,file_name,image_path1,image_path2);

def uc(email_from,email_to,password,emlcheck,ExlPATH):
    ChartThread(email_from,email_to,password,emlcheck,ExlPATH).start()
