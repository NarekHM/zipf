"""Plot wordcounts."""
import argparse
import pandas as pd

def main(args):
   """Run thecommandlineprogram."""
   df = pd.read_csv(args.infile, header=None,
                     names=('word', 'word_frequency'))
   df['rank'] = df['word_frequency'].rank(ascending=False,
										   method='max')
   df['inverse_rank'] = 1 / df['rank']

   ax = df.plot.scatter(x='word_frequency',
   y='inverse_rank',
   figsize=[12, 6],
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
	args = parser.parse_args()
	main(args)
