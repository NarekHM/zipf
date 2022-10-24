
"""Ploting wordcounts."""

import argparse
import pandas as pd
import matplotlib as mpl
import yaml

def set_plot_params(param_file):
    if param_file:
        with open(param_file, 'r') as reader:
            param_dict = yaml.load(reader, Loader=yaml.BaseLoader)
    else:
        param_dict = {}

    for param, value in param_dict.items():
        mpl.rcParams[param] = value


def main(args):
   """Run the command line program."""
   set_plot_params(args.plotparams)

   df = pd.read_csv(args.infile, header=None,
                     names=('word', 'word_frequency'))
   df['rank'] = df['word_frequency'].rank(ascending=False,
										   method='max')

   ax = df.plot.scatter(x='rank',
   y='word_frequency',
   figsize=[12, 6], loglog = True,
   grid=True)
   ax.figure.savefig(args.outfile)


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument('infile', type=argparse.FileType('r'),
						nargs='?', default='-',
						help='Word countcsvfilename')
	parser.add_argument('--outfile', type=str,
						default='plotcounts.png',
						help='Output imagefilename')

	parser.add_argument('--plotparams', type=str, default=None, help='params yaml file')

	args = parser.parse_args()
	main(args)
