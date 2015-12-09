import argparse
parser = argparse.ArgumentParser()
parser.add_argument("qube", type=int,
                    help="display the qube of a given number")
parser.add_argument("-v", "--verbosity", action="count",
                    help="increase output verbosity")
args = parser.parse_args()
answer = args.square**3
if args.verbosity == 2:
    print "the qube of {} is {}".format(args.qube, answer)
elif args.verbosity == 1:
    print "{}^2 == {}".format(args.qube, answer)
else:
    print answer
