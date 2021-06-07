import pandas as pd
import matplotlib.pyplot as plt

for data in ['bentham','iam','saintgall']:
    df=pd.read_excel(open('dane.xlsx', 'rb'),
                sheet_name='epochs_'+data)  


    plt.figure(1)
    plt.subplot(3,1,1)
    plt.title("bluche")
    df.plot(kind='line',x='epoch',y=['bluche_loss','bluche_val_loss'], label=['train_loss','val_loss'],ax=plt.gca())
    plt.gca().set_title('bluche')
    plt.xticks([0,10, 20, 30,40, 50,60,70,80,90])  
    plt.gca().axes.get_yaxis().set_visible(False)
    plt.subplot(3,1,2)
    df.plot(kind='line',x='epoch',y=['flor_loss','flor_val_loss'], label=['train_loss','val_loss'],ax=plt.gca())
    plt.gca().set_title('flor')
    plt.xticks([0,10, 20, 40, 50,60])  
    plt.gca().axes.get_yaxis().set_visible(False)
    plt.subplot(3,1,3)
    df.plot(kind='line',x='epoch',y=['pul_loss','pul_val_loss'], label=['train_loss','val_loss'],ax=plt.gca())
    plt.gca().set_title('puigcerver')
    plt.suptitle('Krzywe straty treningowej i walidacjinej zbiorze '+data, fontsize=12, fontweight='bold')  
    plt.show()

    plt.figure(1)
    plt.subplot(2,1,1)
    df.plot(kind='line',x='epoch',y=['bluche_loss','flor_loss','pul_loss'],ax=plt.gca(), label=['bluche','flor','puigcerver'])
    plt.gca().set_title('Treningowa')
    plt.gca().axes.get_xaxis().set_visible(False)
    plt.subplot(2,1,2)
    df.plot(kind='line',x='epoch',y=['bluche_val_loss','flor_val_loss','pul_val_loss'],ax=plt.gca(), label=['bluche','flor','puigcerver'])
    plt.gca().set_title('Walidacyjna')

    plt.suptitle('Zbiorcze krzywe straty treningowej i walidacjinej zbiorze '+data, fontsize=12, fontweight='bold')
    plt.show()