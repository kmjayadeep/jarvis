import lms
import argparse

def parse(script,input_args):
	parser = argparse.ArgumentParser(description='Jarvis assistant',prog='Jarvis')
	parser.add_argument('script',choices=['lms','others'])

	if(script=='lms'):
		lms.process(input_args,parser)
	