


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
            val_losses.append(splitted[ind+1])

    return val_losses
if __name__=="__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("-f","--file", dest="filename", default='',
                        help="name of the output file", type=str)
    args = parser.parse_args()


    name = args.filename

    data = get_data(name)
