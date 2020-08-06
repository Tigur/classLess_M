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
    X = []
    val_logs.sort(key=(lambda x: x[0]))
    for fL,lossList in val_logs:
        sv_losses.append(lossList[50])
        X.append(fL)

    p.plot(X,sv_losses)
    p.xlabel("fragment length")
    p.ylabel("best loss")

    print(X)


    p.show()


if __name__=="__main__":
    #plot_learning_curve(args.file)
    plot_best(args.file)






