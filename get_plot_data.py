import os


def get_data(name):

    outfile_lines = []
    val_losses = []

    with open(name, 'rt') as outfile:
        for line in outfile:
            outfile_lines.append(line)

    for line in outfile_lines:
        splitted = line.split()
        if "val_loss:" in splitted:
            ind = splitted.index("val_loss:")
            val_losses.append(float(splitted[ind+1]))

    return val_losses



def get_training_loss(name):
    outfile_lines = []
    losses = []

    with open(name, 'rt') as outfile:
        for line in outfile:
            outfile_lines.append(line)

    for line in outfile_lines:
        splitted = line.split()
        if "loss:" in splitted:
            ind = splitted.index("loss:")
            losses.append(float(splitted[ind+1]))

    return losses
def get_val_losses(path):
    val_losses_list = []
    val_losses_tuple = ()
    for file in os.listdir(path):
        if file[-4::]=='.log':
            #find FL index (always 2)
            splitted_name = file.split("_")
            fL = int(splitted_name[2][2::])
            #until "_" read name
            #convert to number
            val_losses_list.append((fL,get_data(path+file)))
    print(f"Done making losses list at {path+file}")
    return val_losses_list

def get_losses(path):
    losses_list = []
    for file in os.listdir(path):
        if file[-4::]=='.log':
            splitted_name = file.split("_")
            fL = int(splitted_name[2][2::])


            losses_list.append((fL,get_training_loss(path+file)))
    print(f"Done making losses list at {path+file}")
    if len(losses_list) == 0:
        print("Nothing was written")
    return losses_list

if __name__=="__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("-f","--file", dest="filename", default='',
                        help="name of the output file", type=str)
    args = parser.parse_args()


    name = args.filename

    data = get_data(name)

    print(data)


