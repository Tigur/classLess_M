import matplotlib
from matplotlib import pyplot as p

from get_plot_data import *
from argparse import ArgumentParser
import sys


parser = ArgumentParser()
parser.add_argument("file",
                    help="name of the output file", type=str)
parser.add_argument("-R", dest="isFolder",
                    help="Flag for folder paths", action='store_true')
args = parser.parse_args()

def plot_learning_curve(file):
    val_losses = get_data(file)
    epochs = range(1,301,1)

    p.plot(epochs,val_losses)
    p.xlabel("epoch")
    p.ylabel("validation loss")

    p.show()

def plot_best(path):
    val_logs = get_val_losses(path)
    train_loss_logs = get_losses(path)

    if (len(val_logs) or len(train_loss_logs)) == 0:
        print("NO DATA!! ")
        sys.exit()


    sv_losses = []
    Xv = []
    s_losses = []
    X = []
    val_logs.sort(key=(lambda x: x[0]))
    for fL,lossList in val_logs:
        sv_losses.append(lossList[50])
        Xv.append(fL)


    train_loss_logs.sort(key=(lambda x: x[0]))
    for fL,lossList in train_loss_logs:
        s_losses.append(lossList[50])
        X.append(fL)


    fig1 = p.figure(1)
    #ax1 = fig1.add_axes([0,0,0.9,0.9])
    ax1 = fig1.add_subplot(111)
    l_val = ax1.plot(Xv,sv_losses,'go-')
    fig2 = p.figure(2,linewidth=2)
    #ax2 = fig2.add_axes([0,0,1,1])
    ax2 = fig2.add_subplot(111)
    l_train = ax2.plot(X,s_losses,'go-')
    ax1.set_title("validation Losses")
    ax2.set_title("training Losses")
    ax1.set_xlabel("fragment Length")
    ax2.set_xlabel("fragment Length")
    ax1.set_ylabel("Loss")
    ax2.set_ylabel("Loss")
    ax1.grid(True)
    ax2.grid(True)

    ax1.spines['left'].set_linewidth(2)

    ax2.autoscale(enable=True, axis='both', tight=False)

    #p.plot(X,sv_losses)
    #p.xlabel("fragment length")
    #p.ylabel("best loss")

    print(X)


    p.show()


if __name__=="__main__":
    #plot_learning_curve(args.file)
    plot_best(args.file)






