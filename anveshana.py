from tkinter import *
from tkinter import messagebox
import random,os,tempfile,smtplib
#functionality part
def clear():

    cheeserollEntry.delete(0,END)
    babycorn65Entry.delete(0,END)
    eggrollEntry.delete(0,END)
    fingerchipsEntry.delete(0,END)
    gobi65Entry.delete(0,END)
    chickenlollipopEntry.delete(0,END)
    vegbiriyaniEntry.delete(0,END)
    jeerariceEntry.delete(0,END)
    palakriceEntry.delete(0,END)
    gheericeEntry.delete(0,END)
    masalariceEntry.delete(0,END)
    paneermasalaEntry.delete(0,END)
    kajumasalaEntry.delete(0,END)
    vegkoftaEntry.delete(0,END)
    palakpannerEntry.delete(0,END)
    daltadkaEntry.delete(0,END)
    dalfryEntry.delete(0,END)


    cheeserollEntry.insert(0,0)
    babycorn65Entry.insert(0,0)
    eggrollEntry.insert(0,0)
    fingerchipsEntry.insert(0,0)
    gobi65Entry.insert(0,0)
    chickenlollipopEntry.insert(0,0)
    vegbiriyaniEntry.insert(0,0)
    jeerariceEntry.insert(0,0)
    palakriceEntry.insert(0,0)
    gheericeEntry.insert(0,0)
    masalariceEntry.insert(0,0)
    paneermasalaEntry.insert(0,0)
    kajumasalaEntry.insert(0,0)
    vegkoftaEntry.insert(0,0)
    palakpannerEntry.insert(0,0)
    daltadkaEntry.insert(0,0)
    dalfryEntry.insert(0,0)

    starterpriceEntry.delete(0,END)
    ricepriceEntry.delete(0,END)
    maincourcepriceEntry.delete(0,END)
    servicetaxEntry.delete(0,END)
    servicechargeEntry.delete(0,END)
    vatEntry.delete(0,END)
    nameEntry.delete(0,END)
    phoneEntry.delete(0,END)
    billnumberEntry.delete(0,END)

    textarea.delete(1.0,END)


def send_email():
 def send_gmail():
     ob=smtplib.SMTP('smtp.gmail.com',587)
     ob.starttls()
     ob.login(senderEntry.get(),passwordEntry.get())
     message=email_textarea.get(1.0,END)
     ob.sendmail(senderEntry.get(),recieverEntry.get(),message)
     ob.quit()
     messagebox.showinfo('Success','Bill is Successfully sent')
 if textarea.get(1.0,END)=='\n':
  messagebox.showerror('Error','Bill is Empty')
 else:
     root1=Toplevel()
     
     root1.title('Send Gmail')
     root1.config(bg='grey20')

# Disable window resizing
     root1.resizable(0, 0)

# Create a LabelFrame for the sender information
     senderFrame = LabelFrame(root1,text='SENDER', font=('arial', 16, 'bold'), bg='purple2')
     senderFrame.grid(row=0, column=0,padx=40,pady=20)

     gmailIDLabel=Label(senderFrame,text="Sender's Email",font=('arial',14,'bold'))
     gmailIDLabel.grid(row=0,column=0)

# Create a Label for the sender's email
     senderLabel = Label(senderFrame, text="Sender's Email", font=('arial', 14, 'bold'))
     senderLabel.grid(row=0, column=0,padx=10,pady=8)

# Create an Entry widget for the sender's email
     senderEntry = Entry(senderFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief='ridge')
     senderEntry.grid(row=0, column=1,padx=10,pady=8)

     passwordLabel = Label(senderFrame,text="Password",font=('arial',14,'bold'))
     passwordLabel.grid(row=1, column=0,padx=10,pady=8)


     passwordEntry = Entry(senderFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE,show='*')
     passwordEntry.grid(row=1, column=1,padx=10,pady=8)

     recipientFrame = LabelFrame(senderFrame,text="Recipient Name",font=('arial',14,'bold'))
     recipientFrame.grid(row=2, column=0,padx=60,pady=20)

     recieverLabel = Label(recipientFrame,text="Email Address",font=('arial',14,'bold'))
     recieverLabel.grid(row=0, column=0,padx=10,pady=8)


     recieverEntry = Entry(recipientFrame,font=('arial',14,'bold'),bd=2,width=23,relief='ridge')
     recieverEntry.grid(row=0, column=1,padx=10,pady=8)

     messageboxLabel = Label(recipientFrame,text="Message",font=('arial', 14, 'bold'))
     messageboxLabel.grid(row=1, column=0,padx=10,pady=8)

     email_textarea=Text(recipientFrame,font=('arial',14,'bold'),bd=2,relief=SUNKEN,
                     width=42,height=11)
     email_textarea.grid(row=2,column=0,columnspan=2)
     email_textarea.delete(1.0,END)
     email_textarea.insert(END,textarea.get(1.0,END).replace('=','').replace('-','').replace('\t\t\t','\t\t'))


     sendButton=Button(root1,text="Send",font=('arial', 16, 'bold'),width=15,command=send_gmail)
     sendButton.grid(row=2,column=0,pady=20)
 

# Run the main loop
     root1.mainloop()
      

def print_bill():
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is Empty')
    else:
        file=tempfile.mktemp('.txt')
        open(file,'w').write(textarea.get(1.0,END))
        os.starttls(file,'print')
        

def search_bill():
    for i in os.listdir('bills/'):
        if i.split('.')[0]==billnumberEntry.get():
            f=open(f'bills/{i}','r')
            textarea.delete(1.0,END)
            for data in f:
                textarea.insert(END,data)
            f.close()
            break
    
    else:
        messagebox.showerror('Error','invalid Bill Number')


if not os.path.exists('bills'):
    os.mkdir('bills')


def save_bill():
    global billnumber
    result=messagebox.askyesno('Confirm','Do you want to save the bill?')
    if result:
        bill_content=textarea.get(1.0,END)
        file=open('bills/{billnumber}.txt','w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Success',"bill number {}is saved successfully".format(billnumber))
        billnumber=random.int(500,1000)

billnumber=random.randint(500,1000)
def bill_area():
    if nameEntry.get()=='' or phoneEntry.get()=='':
       messagebox.showerror('Error','customer Details Are Required')
    
    elif starterpriceEntry.get()=='' and ricepriceEntry.get()=='' and maincourcepriceEntry.get()=='' and servicetaxEntry.get()=='' and servicechargeEntry.get()=='' and vatEntry.get()=='':
         messagebox.showerror('Error','No Products are selected')

    elif starterpriceEntry.get()=='0Rs' and ricepriceEntry.get()=='0Rs' and maincourcepriceEntry.get=='0Rs' and servicetaxEntry.get()=='0.0Rs' and servicechargeEntry.get()=='0.0Rs' and vatEntry.get()=='0.0Rs':
         messagebox.showerror('Error','No Products are selected')
    textarea.delete(1.0,END)
    textarea.insert(END,'\t\t**Welcome Customer**\n')
    textarea.insert(END,f'\nBill Number: {billnumber}\n')
    textarea.insert(END,f'\nCostomer Name: {nameEntry.get()}\n')
    textarea.insert(END,f'\nCostomer Phnoe Number: {phoneEntry.get()}\n')
    textarea.insert(END,'\n=======================================================')
    textarea.insert(END,'Product\t\t\tQuantity\t\t\tPrice')
    textarea.insert(END,'\n=======================================================')
    if cheeserollEntry.get()!='0':
        textarea.insert(END,f'\nCheese Roll\t\t\t{cheeserollEntry.get()}\t\t\t{cheeseprice} Rs')
    if babycorn65Entry.get()!='0':
        textarea.insert(END,f'\nBaby Corn\t\t\t{babycorn65Entry.get()}\t\t\t{babycorn} Rs')
    if eggrollEntry.get()!='0':
        textarea.insert(END,f'\nEgg Roll\t\t\t{eggrollEntry.get()}\t\t\t{eggrol} Rs')
    if fingerchipsEntry.get()!='0':
        textarea.insert(END,f'\nFinger Chips\t\t\t{fingerchipsEntry.get()}\t\t\t{fingerchip} Rs')
    if gobi65Entry.get()!='0':
        textarea.insert(END,f'\nGobi 65\t\t\t{cheeserollEntry.get()}\t\t\t{gobi} Rs')
    if chickenlollipopEntry.get()!='0':
        textarea.insert(END,f'\nChicken Lollipop\t\t\t{cheeserollEntry.get()}\t\t\t{chicken} Rs')
    if vegbiriyaniEntry.get()!='0':
        textarea.insert(END,f'\nVeg Biriyani\t\t\t{cheeserollEntry.get()}\t\t\t{veg} Rs')

    if jeerariceEntry.get()!='0':
        textarea.insert(END,f'\nJeera Rice\t\t\t{jeerariceEntry.get()}\t\t\t{jeera} Rs')
    if palakriceEntry.get()!='0':
        textarea.insert(END,f'\nPalak Ricet\t\t\t{palakriceEntry.get()}\t\t\t{palak} Rs')
    if gheericeEntry.get()!='0':
        textarea.insert(END,f'\nGhee Rice\t\t\t{gheericeEntry.get()}\t\t\t{ghee} Rs')
    if masalariceEntry.get()!='0':
        textarea.insert(END,f'\nMasala Rice\t\t\t{masalariceEntry.get()}\t\t\t{masala} Rs')
    if friedriceEntry.get()!='0':
        textarea.insert(END,f'\nFried Rice\t\t\t{friedriceEntry.get()}\t\t\t{fried} Rs')
    if paneermasalaEntry.get()!='0':
        textarea.insert(END,f'\nPaneer Masala\t\t\t{paneermasalaEntry.get()}\t\t\t{paneer} Rs')
    if kajumasalaEntry.get()!='0':
        textarea.insert(END,f'\nKaju Masala\t\t\t{kajumasalaEntry.get()}\t\t\t{kaju} Rs')
    if vegkoftaEntry.get()!='0':
        textarea.insert(END,f'\nVeg Kofta\t\t\t{vegkoftaEntry.get()}\t\t\t{veg1} Rs')
    if palakpannerEntry.get()!='0':
        textarea.insert(END,f'\nPalak Paaneer\t\t\t{palakpannerEntry.get()}\t\t\t{palakp} Rs')
    if daltadkaEntry.get()!='0':
        textarea.insert(END,f'\nDal Tadka\t\t\t{daltadkaEntry.get()}\t\t\t{dal1} Rs')
    if dalfryEntry.get()!='0':
        textarea.insert(END,f'\nDal Fry\t\t\t{dalfryEntry.get()}\t\t\t{dal2} Rs')
    textarea.insert(END,'\n-------------------------------------------------------')
    
    if servicetaxEntry.get()!='0.0Rs':
        textarea.insert(END,f'\nService Tax\t\t\t{servicetaxEntry.get()}')
    if servicechargeEntry.get()!='0.0Rs':
        textarea.insert(END,f'\nService Charge\t\t\t{servicechargeEntry.get()}')
    if vatEntry.get()!='0.0Rs':
        textarea.insert(END,f'\nVAT\t\t\t{vatEntry.get()}')

    textarea.insert(END,f'\nTotal Bill\t\t\t{totalbill} Rs')
    textarea.insert(END,'\n-------------------------------------------------------')
    save_bill()


def total():
    #starter price calculation
    global cheeseprice
    cheeseprice=int(cheeserollEntry.get())*150
    global babycorn
    babycorn=int(babycorn65Entry.get())*120
    global eggrol
    eggrol=int(eggrollEntry.get())*100
    global fingerchip
    fingerchip=int(fingerchipsEntry.get())*110
    global gobi
    gobi=int(gobi65Entry.get())*100
    global chicken
    chicken=int(chickenlollipopEntry.get())*180

    totalstarterprice=cheeseprice+babycorn+eggrol+fingerchip+gobi+chicken
    starterpriceEntry.delete(0,END)
    starterpriceEntry.insert(0,f'{totalstarterprice}Rs')
    
    
    #rice itemes price calculation
    global veg
    veg=int(vegbiriyaniEntry.get())*200
    global jeera
    jeera=int(jeerariceEntry.get())*180
    global palak
    palak=int(palakriceEntry.get())*100
    global ghee
    ghee=int(gheericeEntry.get())*150
    global masala
    masala=int(masalariceEntry.get())*80
    global fried
    fried=int(friedriceEntry.get())*170

    totalriceprice=veg+jeera+palak+ghee+masala+fried
    ricepriceEntry.delete(0,END)
    ricepriceEntry.insert(0,f'{totalriceprice}Rs')
 
    #main cource price calculation
    global paneer
    paneer=int(paneermasalaEntry.get())*250
    global kaju
    kaju=int(kajumasalaEntry.get())*280
    global veg1
    veg1=int(vegkoftaEntry.get())*200
    global palakp
    palakp=int(palakpannerEntry.get())*180
    global dal1
    dal1=int(daltadkaEntry.get())*220
    global dal2
    dal2=int(dalfryEntry.get())*190

    totalmaincourceprice=paneer+kaju+veg1+palakp+dal1+dal2
    maincourcepriceEntry.delete(0,END)
    maincourcepriceEntry.insert(0,f'{totalmaincourceprice}Rs')
    global totalprice
    totalprice=totalstarterprice+totalriceprice+totalmaincourceprice
    servicetax=totalprice*0.05
    servicetaxEntry.delete(0,END)
    servicetaxEntry.insert(0,f'{servicetax}Rs')
    servicecharge=totalprice*0.03
    servicechargeEntry.delete(0,END)
    servicechargeEntry.insert(0,f'{servicecharge}Rs')
    vat=totalprice*0.04
    vatEntry.delete(0,END)
    vatEntry.insert(0,f'{vat}Rs')
    
    global totalbill
    totalbill=servicetax+servicecharge+vat+totalstarterprice+totalriceprice+totalmaincourceprice





#Gui part
root=Tk()
root.title('Restaurant Billing Management System')
root.geometry('1270x685')
root.iconbitmap('icon copy.ico')
headingLabel=Label(root,text='Restaurant Billing Management System',font=('times new roman',30,'bold')
                   ,bg='purple2',bd=12,relief=GROOVE)
headingLabel.pack(fill=X)

customer_details_frame=LabelFrame(root,text='Customer Details',font=('times new roman',15,'bold'),
                                  bd=8,relief=GROOVE,bg='purple2')

                                                                     
customer_details_frame.pack()
customer_details_frame.pack(fill=X,pady=10)

nameLabel=Label(customer_details_frame,text='Name',font=('times new roman',15,'bold'),bg='purple2')
nameLabel.grid(row=0,column=0,padx=20,pady=2)

nameEntry=Entry(customer_details_frame,font=('arial',15),bd=4,width=18)
nameEntry.grid(row=0,column=1,padx=8)

phoneLabel=Label(customer_details_frame,text='Phone Number',font=('times new roman',15,'bold'),bg='purple2')
phoneLabel.grid(row=0,column=2,padx=20,pady=2)

phoneEntry=Entry(customer_details_frame,font=('arial',15),bd=4,width=18)
phoneEntry.grid(row=0,column=3,padx=8)

billnumberLabel=Label(customer_details_frame,text='Bill Number',font=('times new roman',15,'bold'),bg='purple2')
billnumberLabel.grid(row=0,column=4,padx=20)

billnumberEntry=Entry(customer_details_frame,font=('arial',15),bd=4,width=18)
billnumberEntry.grid(row=0,column=5,padx=8)

searchButton=Button(customer_details_frame,text='SEARCH',
                    font=('arial',12,'bold'),bd=7,width=35,command=search_bill)
searchButton.grid(row=0,column=6,padx=20,pady=8)

productFrame=Frame(root)
productFrame.pack(fill=X)

starterFrame=LabelFrame(productFrame,text='Starter',font=('times new roman',15,'bold'),fg='grey1',bg='purple2',bd=8,relief=GROOVE)

starterFrame.grid(row=0,column=0)

cheeseroll=Label(starterFrame,text='Cheese Roll',font=('times new roman',15,'bold'),fg='grey1',bg='purple2')
cheeseroll.grid(row=0,column=0,pady=9,padx=10)

cheeserollEntry=Entry(starterFrame,font=('times new roman',15,'bold'),width=10,bd=5)
cheeserollEntry.grid(row=0,column=1,pady=9,padx=10)
cheeserollEntry.insert(0,0)
babycorn65=Label(starterFrame,text='Babycorn 65',font=('times new roman',15,'bold'),fg='grey1',bg='purple2')
babycorn65.grid(row=1,column=0,pady=9,padx=10)

babycorn65Entry=Entry(starterFrame,font=('times new roman',15,'bold'),width=10,bd=5)
babycorn65Entry.grid(row=1,column=1,pady=9,padx=10)
babycorn65Entry.insert(0,0)
eggroll=Label(starterFrame,text='Egg Roll',font=('times new roman',15,'bold'),fg='grey1',bg='purple2')
eggroll.grid(row=2,column=0,pady=9,padx=10)

eggrollEntry=Entry(starterFrame,font=('times new roman',15,'bold'),width=10,bd=5)
eggrollEntry.grid(row=2,column=1,pady=9,padx=10)
eggrollEntry.insert(0,0)
fingerchips=Label(starterFrame,text='Finger Chips',font=('times new roman',15,'bold'),fg='grey1',bg='purple2')
fingerchips.grid(row=3,column=0,pady=9,padx=10)

fingerchipsEntry=Entry(starterFrame,font=('times new roman',15,'bold'),width=10,bd=5)
fingerchipsEntry.grid(row=3,column=1,pady=9,padx=10)
fingerchipsEntry.insert(0,0)
gobi65=Label(starterFrame,text='Gobi 65',font=('times new roman',15,'bold'),fg='grey1',bg='purple2')
gobi65.grid(row=4,column=0,pady=9,padx=10)

gobi65Entry=Entry(starterFrame,font=('times new roman',15,'bold'),width=10,bd=5)
gobi65Entry.grid(row=4,column=1,pady=9,padx=10)
gobi65Entry.insert(0,0)
chickenlollipop=Label(starterFrame,text='Chicken Lollipop',font=('times new roman',15,'bold'),fg='grey1',bg='purple2')
chickenlollipop.grid(row=5,column=0,pady=9,padx=10)

chickenlollipopEntry=Entry(starterFrame,font=('times new roman',15,'bold'),width=10,bd=5)
chickenlollipopEntry.grid(row=5,column=1,pady=9,padx=10)
chickenlollipopEntry.insert(0,0)
riceFrame=LabelFrame(productFrame,text='Rice Items',font=('times new roman',15,'bold'),fg='grey1',bg='purple2',bd=8,relief=GROOVE)

riceFrame.grid(row=0,column=1)

vegbiriyaniLable=Label(riceFrame,text='Veg Biriyani',font=('times new roman',15,'bold'),fg='grey1',bg='purple2')
vegbiriyaniLable.grid(row=0,column=0,pady=9,padx=10,sticky='w')

vegbiriyaniEntry=Entry(riceFrame,font=('times new roman',15,'bold'),width=10,bd=5)
vegbiriyaniEntry.grid(row=0,column=1,pady=9,padx=10)
vegbiriyaniEntry.insert(0,0)
jeerariceLable=Label(riceFrame,text='Jeera Rice',font=('times new roman',15,'bold'),fg='grey1',bg='purple2')
jeerariceLable.grid(row=1,column=0,pady=9,padx=10,sticky='w')

jeerariceEntry=Entry(riceFrame,font=('times new roman',15,'bold'),width=10,bd=5)
jeerariceEntry.grid(row=1,column=1,pady=9,padx=10)
jeerariceEntry.insert(0,0)
palakriceLable=Label(riceFrame,text='Palak Rice',font=('times new roman',15,'bold'),fg='grey1',bg='purple2')
palakriceLable.grid(row=2,column=0,pady=9,padx=10,sticky='w')

palakriceEntry=Entry(riceFrame,font=('times new roman',15,'bold'),width=10,bd=5)
palakriceEntry.grid(row=2,column=1,pady=9,padx=10)
palakriceEntry.insert(0,0)
gheericeLable=Label(riceFrame,text='Ghee Rice',font=('times new roman',15,'bold'),fg='grey1',bg='purple2')
gheericeLable.grid(row=3,column=0,pady=9,padx=10,sticky='w')

gheericeEntry=Entry(riceFrame,font=('times new roman',15,'bold'),width=10,bd=5)
gheericeEntry.grid(row=3,column=1,pady=9,padx=10)
gheericeEntry.insert(0,0)
masalariceLable=Label(riceFrame,text='Masala Rice',font=('times new roman',15,'bold'),fg='grey1',bg='purple2')
masalariceLable.grid(row=4,column=0,pady=9,padx=10,sticky='w')

masalariceEntry=Entry(riceFrame,font=('times new roman',15,'bold'),width=10,bd=5)
masalariceEntry.grid(row=4,column=1,pady=9,padx=10)
masalariceEntry.insert(0,0)
friedriceLable=Label(riceFrame,text='Fried Rice',font=('times new roman',15,'bold'),fg='grey1',bg='purple2')
friedriceLable.grid(row=5,column=0,pady=9,padx=10,sticky='w')

friedriceEntry=Entry(riceFrame,font=('times new roman',15,'bold'),width=10,bd=5)
friedriceEntry.grid(row=5,column=1,pady=9,padx=10)
friedriceEntry.insert(0,0)
maincourceFrame=LabelFrame(productFrame,text='Main Cource',font=('times new roman',15,'bold'),fg='grey1',bg='purple2',bd=8,relief=GROOVE)

maincourceFrame.grid(row=0,column=2)

paneermasalaLable=Label(maincourceFrame,text='Paneer Masala',font=('times new roman',15,'bold'),fg='grey1',bg='purple2')
paneermasalaLable.grid(row=0,column=2,pady=9,padx=10,sticky='w')

paneermasalaEntry=Entry(maincourceFrame,font=('times new roman',15,'bold'),width=10,bd=5)
paneermasalaEntry.grid(row=0,column=3,pady=9,padx=10)
paneermasalaEntry.insert(0,0)
kajumasalaLable=Label(maincourceFrame,text='Kaju Masala',font=('times new roman',15,'bold'),fg='grey1',bg='purple2')
kajumasalaLable.grid(row=1,column=2,pady=9,padx=10,sticky='w')

kajumasalaEntry=Entry(maincourceFrame,font=('times new roman',15,'bold'),width=10,bd=5)
kajumasalaEntry.grid(row=1,column=3,pady=9,padx=10)
kajumasalaEntry.insert(0,0)
vegkoftaLable=Label(maincourceFrame,text='Veg Kofta',font=('times new roman',15,'bold'),fg='grey1',bg='purple2')
vegkoftaLable.grid(row=2,column=2,pady=9,padx=10,sticky='w')

vegkoftaEntry=Entry(maincourceFrame,font=('times new roman',15,'bold'),width=10,bd=5)
vegkoftaEntry.grid(row=2,column=3,pady=9,padx=10)
vegkoftaEntry.insert(0,0)
palakpaneerLable=Label(maincourceFrame,text='Palak Paneer',font=('times new roman',15,'bold'),fg='grey1',bg='purple2')
palakpaneerLable.grid(row=3,column=2,pady=9,padx=10,sticky='w')

palakpannerEntry=Entry(maincourceFrame,font=('times new roman',15,'bold'),width=10,bd=5)
palakpannerEntry.grid(row=3,column=3,pady=9,padx=10)
palakpannerEntry.insert(0,0)
daltadkaLable=Label(maincourceFrame,text='Dal Tadka',font=('times new roman',15,'bold'),fg='grey1',bg='purple2')
daltadkaLable.grid(row=4,column=2,pady=9,padx=10,sticky='w')

daltadkaEntry=Entry(maincourceFrame,font=('times new roman',15,'bold'),width=10,bd=5)
daltadkaEntry.grid(row=4,column=3,pady=9,padx=10)
daltadkaEntry.insert(0,0)
dalfryLable=Label(maincourceFrame,text='Dal Fry',font=('times new roman',15,'bold'),fg='grey1',bg='purple2')
dalfryLable.grid(row=5,column=2,pady=9,padx=10,sticky='w')

dalfryEntry=Entry(maincourceFrame,font=('times new roman',15,'bold'),width=10,bd=5)
dalfryEntry.grid(row=5,column=3,pady=9,padx=10)
dalfryEntry.insert(0,0)
billframe=LabelFrame(productFrame,bd=8,relief=GROOVE)
billframe.grid(row=0,column=3,padx=15)

billareaLabel=Label(billframe,text='Bill Area',font=('times new roman',15,'bold'),bd=7,relief=GROOVE)
billareaLabel.pack(fill=X)

scrollbar=Scrollbar(billframe,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)
textarea=Text(billframe,height=18,width=55,yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)

billmenuFrame=LabelFrame(root,text='Bill Menu',font=('times new roman',15,'bold'),fg='grey1',bg='purple2',bd=8,relief=GROOVE)

billmenuFrame.pack(fill=X)
starterpriceLable=Label(billmenuFrame,text='Starter Price',font=('times new roman',15,'bold'),fg='grey1',bg='purple2')
starterpriceLable.grid(row=0,column=0,pady=6,padx=10,sticky='w')

starterpriceEntry=Entry(billmenuFrame,font=('times new roman',15,'bold'),width=10,bd=5)
starterpriceEntry.grid(row=0,column=1,pady=6,padx=10)

ricepriceLable=Label(billmenuFrame,text='Rice Items Price',font=('times new roman',15,'bold'),fg='grey1',bg='purple2')
ricepriceLable.grid(row=1,column=0,pady=6,padx=10,sticky='w')

ricepriceEntry=Entry(billmenuFrame,font=('times new roman',15,'bold'),width=10,bd=5)
ricepriceEntry.grid(row=1,column=1,pady=6,padx=10)

maincourcepriceLable=Label(billmenuFrame,text='Main Cource Price',font=('times new roman',15,'bold'),fg='grey1',bg='purple2')
maincourcepriceLable.grid(row=2,column=0,pady=6,padx=10,sticky='w')

maincourcepriceEntry=Entry(billmenuFrame,font=('times new roman',15,'bold'),width=10,bd=5)
maincourcepriceEntry.grid(row=2,column=1,pady=6,padx=10)

servicetaxLable=Label(billmenuFrame,text='Service Tax',font=('times new roman',15,'bold'),fg='grey1',bg='purple2')
servicetaxLable.grid(row=0,column=2,pady=6,padx=10,sticky='w')

servicetaxEntry=Entry(billmenuFrame,font=('times new roman',15,'bold'),width=10,bd=5)
servicetaxEntry.grid(row=0,column=3,pady=6,padx=10)

servicechargeLable=Label(billmenuFrame,text='Service Charge',font=('times new roman',15,'bold'),fg='grey1',bg='purple2')
servicechargeLable.grid(row=1,column=2,pady=6,padx=10,sticky='w')

servicechargeEntry=Entry(billmenuFrame,font=('times new roman',15,'bold'),width=10,bd=5)
servicechargeEntry.grid(row=1,column=3,pady=6,padx=10)

vatLable=Label(billmenuFrame,text='VAT',font=('times new roman',15,'bold'),fg='grey1',bg='purple2')
vatLable.grid(row=2,column=2,pady=6,padx=10,sticky='w')

vatEntry=Entry(billmenuFrame,font=('times new roman',15,'bold'),width=10,bd=5)
vatEntry.grid(row=2,column=3,pady=6,padx=10)

buttonFrame=Frame(billmenuFrame,bd=8,relief=GROOVE)
buttonFrame.grid(row=0,column=4,rowspan=3,padx=50)

totalButton=Button(buttonFrame,text='total',command=total,font=('arial',16,'bold'),bg='purple2',bd=5,width=8,pady=10)
totalButton.grid(row=0,column=0,pady=20,padx=5)

billButton=Button(buttonFrame,text='Bill',font=('arial',16,'bold'),bg='purple2',bd=5,width=8,pady=10,command=bill_area)
billButton.grid(row=0,column=1,pady=20,padx=5)

emailButton=Button(buttonFrame,text='Email',font=('arial',16,'bold'),bg='purple2',bd=5,width=8,pady=10,command=send_email)
emailButton.grid(row=0,column=2,pady=20,padx=5)

printButton=Button(buttonFrame,text='Print',font=('arial',16,'bold'),bg='purple2',bd=5,width=8,pady=10,command=print_bill)
printButton.grid(row=0,column=3,pady=20,padx=5)

clearButton=Button(buttonFrame,text='Clear',font=('arial',16,'bold'),bg='purple2',bd=5,width=8,pady=10,command=clear)
clearButton.grid(row=0,column=4,pady=20,padx=5)

root.mainloop()
